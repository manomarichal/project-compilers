from src.AST import AST
from src.AST.Visitor import Visitor
from io import StringIO

def check_if_void(ast: AST.Component):
    return ast.get_type().__repr__() == 'void'

def check_if_array(ast: AST.Component):
    return ast.get_type().__repr__()[0] == '['

def find_array_size(ast: AST.Variable):
    base = ast.get_type().__repr__().split('x')
    return int(base[1][0:len(base[1])-1])

def check_if_floating(ast: AST.Component):
    return ast.get_type().__repr__()[0:5] == 'float'

def get_math_instruction(op:AST.MathOp, floating: False):
    op_str = ''
    if isinstance(op, AST.Sum): op_str += 'add'
    elif isinstance(op, AST.Sub): op_str += 'sub'
    elif isinstance(op, AST.Prod): op_str += 'mul'
    elif isinstance(op, AST.Div): op_str += 'div'
    elif isinstance(op, AST.Mod): op_str += 'mod'
    elif isinstance(op, AST.Addi): op_str += 'addi'
    if floating: op_str += '.s'
    return op_str

def gen_comp_instruction_int(op:AST.CompOp):
    if isinstance(op, AST.Equal): return 'beq'
    elif isinstance(op, AST.NotEqual): return 'bne'
    elif isinstance(op, AST.MoreE): return'bge'
    elif isinstance(op, AST.More): return 'bgt'
    elif isinstance(op, AST.LessE): return 'ble'
    elif isinstance(op, AST.Less): return 'blt'

def get_logic_instruction(op:AST.LogicOp):
    op_str = ''
    if isinstance(op, AST.And):
        op_str += 'and'
    elif isinstance(op, AST.Or):
        op_str += 'or'
    return op_str

class MIPSVisitor(Visitor):
    file = None
    _lcounter = 0 # counter to keep track of labels used
    _adress = 0
    _tcounter = 0
    _t_help_counter = 0
    _f_help_counter = 0
    _scounter = 0
    _fcounter = 1
    _fpcounter = 0
    function_label_stack = []
    frame_size_stack = []
    exit_label_stack = []
    begin_label_stack = []
    buffer_stack = []
    scope_counter = 0

    def __init__(self, file):
        self.header_buf = StringIO()
        self.function_buffers = []
        self.print_to_header(".data")
        self.print_to_header("\tfpzero: .float 0.0")
        self.print_to_header("\tfpone: .float 1.0")
        self.print_to_header("\tfpminone: .float -1.0")
        self.file = file


    # HELPER FUNCTIONS
    def print_to_buffer(self, string, ws_str ='\n\t', modifier = 0):
        self.buffer_stack[-1].write(ws_str + string)

    def print_to_header(self, string):
        self.header_buf.write(string + '\n')

    def close(self):
        self.print_to_header(".text")
        self.print_to_header(".globl main")
        self.print_to_header("\njal main")
        self.print_to_header('beq $zero, $zero, exit')
        self.file.write(self.header_buf.getvalue())
        for buffer in self.function_buffers:
            self.file.write(buffer.getvalue())
        self.file.write("\n\nexit:")
        self.file.close()

    def gen_stack_adress(self, value = 4) -> str:
        adress = str(self._adress) + "($sp)"
        self._adress += value
        self.frame_size_stack[-1] += value
        return adress

    def reset_adress(self):
        self._adress = 0

    def get_reg(self, floating = False, incr = True):
        if self._tcounter > 8 or self._fcounter > 8 or self._tcounter < 0:
            print("max temp registers reached")

        if floating:
            reg = self._fcounter
            if incr is True:
                self._fcounter += 1
            return '$f' + str(reg)
        else:
            reg = self._tcounter
            if incr is True:
                self._tcounter += 1
            return '$t' + str(reg)

    def get_fp_name(self):
        name = "fp" + str(self._fpcounter)
        self._fpcounter += 1
        return name

    def get_string_name(self):
        name = "s" + str(self._scounter)
        self._scounter += 1
        return name

    def decrease_reg(self, value, floating):
        if floating:
            self._fcounter -= value
        else:
            self._tcounter -= value

    def store_rcounter(self, floating):
        if floating:
            self._f_help_counter = self._fcounter
        else:
            self._t_help_counter = self._tcounter

    def restore_tcounter(self, floating):
        if floating:
            self._fcounter = self._f_help_counter
        else:
            self._tcounter = self._t_help_counter

    def reset_reg(self):
        self._tcounter = 0
        self._fcounter = 1

    def get_lname(self) -> str:
        self._lcounter += 1
        return 'l' + str(self._lcounter)

    def load_in_reg(self, ast: AST.Component):
        floating = check_if_floating(ast)
        reg = self.get_reg(floating=floating)
        self.gen_load(reg, self.get_adress_of(ast), floating)
        return reg

    def get_adress_of(self, ast: AST.Component):
        if isinstance(ast, AST.Indir):
            reg = self.get_reg()
            self.gen_load(reg, self.get_adress_of(ast.get_child(0)))
            return '0(' + reg + ')'
        elif isinstance(ast, AST.Index):
            self.visitChildren(ast)
            reg = self.get_reg()
            reg2 = self.get_reg()
            self.gen_load_im(reg, 4)
            self.gen_load(reg2, ast.get_child(1).get_adress())
            self.gen_math_instr(reg, reg, reg2, AST.Prod())
            self.gen_load_adress(reg2, self.get_adress_of(ast.get_child(0)))
            self.gen_math_instr(reg, reg, reg2, AST.Sum())
            self.decrease_reg(1, floating=False)
            return '0(' + reg + ')'
        else:
            return ast.get_adress()

    # GENERATOR FUNCTIONS
    def print_label(self, label, label_comment):
        self.buffer_stack[-1].write('\n\n# ' + label_comment)
        self.buffer_stack[-1].write('\n' + label + ':')
        return label

    def gen_load(self, reg, adress, floating = False):
        if not floating:
            self.print_to_buffer('lw ' + reg + ', ' + adress)
        else:
            self.print_to_buffer('lwc1 ' + reg + ', ' + adress)

    def gen_global_string(self, name, value):
        self.print_to_header("\t" + name + ": .asciiz " + str(value) )

    def gen_global_var(self,ast: AST.Variable, name, value = None):
        if check_if_array(ast):
            self.print_to_header("\t" + name + ": .space " + str(find_array_size(ast)*4))
        else:
            if value is None and check_if_floating(ast): value = 0.0
            elif value is None and not check_if_floating(ast): value = 0
            if check_if_floating(ast):
                self.print_to_header("\t" + name+ ': .float ' + str(value))
            else:
                self.print_to_header("\t" + name + ': .word ' + str(value))

    def gen_load_im(self, reg, value):
        self.print_to_buffer('li ' + reg + ', ' + str(value))

    def gen_load_adress(self, reg, adress):
        self.print_to_buffer('la ' + reg + ', ' + adress)

    def gen_load_dereference(self, reg, pointer):
        self.print_to_buffer('lw ' + reg + ', 0(' + str(pointer) + ')')

    def gen_sw(self, value, adress, floating = False):
        if not floating:
            self.print_to_buffer('sw ' + str(value) + ', ' + adress)
        else:
            self.print_to_buffer('swc1 ' + str(value) + ', ' + adress)

    def gen_move(self, from_reg, to_reg, floating = False):
        self.print_to_buffer('move ' + from_reg + ', ' + to_reg)
        if not floating:
            self.print_to_buffer('move ' + from_reg + ', ' + to_reg)
        else:
            self.print_to_buffer('move.s ' + from_reg + ', ' + to_reg)

    def gen_jal(self, func_name):
        self.print_to_buffer('jal ' + func_name)

    def gen_jr(self, reg):
        self.print_to_buffer('jr ' + reg)

    def gen_bne(self, lhs, rhs, label):
        self.print_to_buffer('bne ' + lhs + ', ' + rhs + ' ' + label)

    def gen_beq(self, lhs, rhs, label):
        self.print_to_buffer('beq ' + lhs + ', ' + rhs + ' ' + label)

    def gen_int_to_float(self, ireg, freg):
        self.print_to_buffer('mtc1 ' + ireg + ', ' + freg )
        self.print_to_buffer('cvt.s.w ' + freg + ', ' + freg)

    def gen_float_to_int(self, ireg, freg):
        self.print_to_buffer('cvt.w.s ' + freg + ', ' + freg)
        self.print_to_buffer('mfc1 ' + ireg + ', ' + freg )

    def gen_mflo(self, res):
        self.print_to_buffer('mflo ' + res)

    def gen_mfhi(self, res):
        self.print_to_buffer('mfhi ' + res)

    def gen_mult_or_div(self, res, lhs, rhs, op_str):
        self.print_to_buffer(op_str + ' ' + res + ', ' + str(lhs) + ', ' + str(rhs))
        self.gen_mflo(res)

    def gen_mod(self, res, lhs, rhs):
        self.print_to_buffer('div ' + ' ' + res + ', ' + str(lhs) + ', ' + str(rhs))
        self.gen_mfhi(res)

    def gen_binary_instruction(self, res, lhs, rhs, op_str):
        self.print_to_buffer(op_str + ' ' + res + ', ' + str(lhs) + ', ' + str(rhs))

    def gen_neg(self, lhs, rhs, floating = False):
        if not floating:
            self.print_to_buffer('neg ' + lhs + ', ' + rhs)
        else:
            self.print_to_buffer('neg.s ' + lhs + ', ' + rhs)

    def gen_not(self, res, lhs, type_of):
        self.print_to_buffer(res + ' = xor ' + type_of + ' ' + str(lhs) + ', 1')

    def gen_or(self, res, lhs, rhs):
        self.print_to_buffer('or ' +  str(res) + ', ' + str(lhs) + ', ' + str(rhs))

    def gen_and(self, res, lhs, rhs):
        self.print_to_buffer('and ' +  str(res) + ', ' + str(lhs) + ', ' + str(rhs))

    def gen_math_instr(self, res, lhs, rhs, op: AST.MathOp, floating = False):
        op_str = get_math_instruction(op, floating)
        if op_str == 'mod':
            self.gen_mod(res, lhs, rhs)
        else:
            self.gen_binary_instruction(res, lhs, rhs, op_str)

    def gen_comp_instr_float(self, lhs, rhs, op: AST.CompOp) -> bool:
        if isinstance(op, AST.Less) or isinstance(op, AST.MoreE):
            self.print_to_buffer("c.lt.s " + lhs + " " + rhs)
        elif isinstance(op, AST.LessE) or isinstance(op, AST.More):
            self.print_to_buffer("c.le.s " + lhs + " " + rhs)
        elif isinstance(op, AST.Equal) or isinstance(op, AST.NotEqual):
            self.print_to_buffer("c.eq.s " + lhs + " " + rhs)
        return isinstance(op, AST.Less) or isinstance(op, AST.LessE) or isinstance(op, AST.Equal)

    def gen_comp_instr(self, res, lhs, rhs, op: AST.CompOp, floating):
        label_false = self.get_lname()
        label_true = self.get_lname()
        label_continue = self.get_lname()

        if not floating:
            self.gen_binary_instruction(lhs, rhs, label_true, gen_comp_instruction_int(op))
            self.gen_branch_uncon(label_false)
        else:
            flag_val = self.gen_comp_instr_float(lhs, rhs, op)
            self.gen_branch_float(label_true, flag_val)
            self.gen_branch_uncon(label_false)

        self.print_label(label_false, 'not true')
        self.gen_load_im(res, 0)
        self.gen_branch_uncon(label_continue)

        self.print_label(label_true, 'true')
        self.gen_load_im(res, 1)
        self.gen_branch_uncon(label_continue)

        self.print_label(label_continue, 'exit comparison')

    def gen_logic_instr(self, res, lhs, rhs, op: AST.LogicOp):
        op_str = get_logic_instruction(op)
        self.gen_binary_instruction(res, lhs, rhs, op_str)

    def gen_syscall(self):
        self.print_to_buffer('syscall')

    def gen_branch_uncon(self, label, floating = False): # unconditional branch
        self.print_to_buffer('beq $zero, $zero, ' + label)

    def gen_branch_con(self, label1, label2, reg): # conditional branch
        self.gen_beq(reg, '$zero', label2)
        self.gen_branch_uncon(label1)

    def gen_branch_float(self, label, type_of: bool):
        if type_of: self.print_to_buffer('bc1t ' + label)
        else: self.print_to_buffer('bc1f ' + label)

    def gen_function_call(self, func_name):
        self.print_to_buffer('jal ' + func_name)

    # VISITOR FUNCTIONS
    def visitComposite(self, ast: AST.Composite):
        self.visitChildren(ast)

    def visitLiteral(self, ast: AST.Literal):
        if self.scope_counter == 0: return

        adress = self.gen_stack_adress()
        ast.set_adress(adress)
        if check_if_void(ast): return

        reg = self.get_reg(check_if_floating(ast))
        if check_if_floating(ast):
            name = self.get_fp_name()
            self.gen_global_var(ast, name, ast.get_value())
            self.gen_load(reg, name, True)
        else:
            self.gen_load_im(reg, ast.get_value())

        self.gen_sw(reg,adress, check_if_floating(ast))
        self.decrease_reg(1, check_if_floating(ast))

    def visitDecl(self, ast: AST.Decl):
        var: AST.Variable = ast.get_child(0)
        if self.scope_counter == 0:
            var.set_adress(var.get_name())
            if ast.get_child_count() != 2:
                self.gen_global_var(var, var.get_name())
            else:
                self.gen_global_var(var, var.get_name(), ast.get_child(1).get_value)

        elif check_if_array(ast): var.set_adress(self.gen_stack_adress(find_array_size(var) * 4))
        else: var.set_adress(self.gen_stack_adress())

    def visitAssignOp(self, ast: AST.AssignOp):
        # TODO gvar
        self.visitChildren(ast)
        if self.scope_counter == 0: return
        if isinstance(ast.get_child(0), AST.Decl):
            var: AST.Variable = ast.get_child(0).get_child(0)
        else:
            var: AST.Variable = ast.get_child(0)

        self.gen_sw(self.load_in_reg(ast.get_child(1)), self.get_adress_of(var), check_if_floating(ast))
        self.reset_reg()

    def visitPrintf(self, ast: AST.Printf):
        self.visitChildren(ast)
        meta = ast.get_meta()
        meta = meta.replace("\\0A", "\\n")
        meta = meta.replace("\\09", "\\t")
        if ast.get_child_count() == 0:
            name = self.get_string_name()
            self.gen_global_string(name, meta)
            self.gen_load_adress("$a0", name)
            self.gen_load_im("$v0", 4)
            self.gen_syscall()
            return

        meta = meta[1:len(ast.get_meta())-1]
        parts = meta.split("%")

        for i in range(len(parts)):
            if parts[i] == '': continue
            string = ''
            if i != 0:
                char = parts[i][0]
                string = "\"" + parts[i][1:] + "\""
                if char == 'd':
                    self.gen_load_im("$v0", 1)
                    self.gen_load('$a0', self.get_adress_of(ast.get_child(i-1)))
                elif char == 'f':
                    self.gen_load_im("$v0", 2)
                    self.gen_load('$f12', self.get_adress_of(ast.get_child(i-1)), True)
                elif char == 'c':
                    self.gen_load_im("$v0", 11)
                    self.gen_load('$a0', self.get_adress_of(ast.get_child(i-1)))
                self.gen_syscall()
            else:
                string = "\"" + parts[i] + "\""

            name = self.get_string_name()
            self.gen_global_string(name, string)
            self.gen_load_adress("$a0", name)
            self.gen_load_im("$v0", 4)
            self.gen_syscall()

            self.reset_reg()

    def visitScanf(self, ast: AST.Scanf):
        self.visitChildren(ast)

        meta = ast.get_meta()[1:len(ast.get_meta()) - 1]
        parts = meta.split("%")

        for i in range(len(parts)):
            if i != 0:
                char = parts[i][0]
                string = "\"" + parts[i][1:] + "\""
                if char == 'd':
                    self.gen_load_im("$v0", 5)
                    self.gen_syscall()
                    self.gen_sw('$v0', '0(' + self.load_in_reg(ast.get_child(i-1)) + ')')
                elif char == 'f':
                    self.gen_load_im("$v0", 6)
                    self.gen_syscall()
                    reg = self.get_reg()
                    self.gen_load(reg, self.get_adress_of(ast.get_child(i-1)))
                    self.gen_sw('$f0', '0(' + reg + ')', True)
                elif char == 'c':
                    self.gen_load_im("$v0", 12)
                    self.gen_syscall()
                    self.gen_sw('$v0', '0(' + self.load_in_reg(ast.get_child(i-1)) + ')')
        self.reset_reg()

    def visitNeg(self, ast: AST.Neg):
        self.visitChildren(ast)
        self.store_rcounter(check_if_floating(ast))
        adress = self.gen_stack_adress()
        ast.set_adress(adress)

        reg = self.get_reg()
        self.gen_neg(reg, reg, check_if_floating(ast))
        self.gen_sw(reg, adress, check_if_floating(ast))

        self.restore_tcounter(check_if_floating(ast))

    def visitNot(self, ast: AST.Not):
        self.visitChildren(ast)
        self.store_rcounter(check_if_floating(ast))
        adress = self.gen_stack_adress()
        ast.set_adress(adress)

        reg = self.get_reg()
        self.gen_load_im(reg, 1)
        self.gen_comp_instr(reg, reg, self.load_in_reg(ast.get_child(0)), AST.NotEqual(), False)
        self.gen_sw(reg, adress, False)

        self.restore_tcounter(floating=check_if_floating(ast))

    def visitPos(self, ast: AST.Neg):
        self.visitChildren(ast)
        ast.set_adress(self.get_adress_of(ast.get_child(0)))

    def visitBinaryOp(self, ast: AST.BinaryOp):
        self.visitChildren(ast)
        reg = self.get_reg(check_if_floating(ast))
        lhs, rhs = self.load_in_reg(ast.get_child(0)), self.load_in_reg(ast.get_child(1))
        floating = check_if_floating(ast.get_child(0))

        if isinstance(ast, AST.MathOp):
            self.gen_math_instr(reg, lhs, rhs, ast, floating)
        elif isinstance(ast, AST.CompOp):
            self.gen_comp_instr(reg, lhs, rhs, ast, floating)
        elif isinstance(ast, AST.LogicOp):
            self.gen_logic_instr(reg, lhs, rhs, ast)

        adress = self.gen_stack_adress()
        ast.set_adress(adress)
        self.gen_sw(reg, adress, check_if_floating(ast))
        self.reset_reg()

    def visitAdress(self, ast: AST.Adress):
        self.visitChildren(ast)
        self.store_rcounter(check_if_floating(ast))

        adress = self.gen_stack_adress()
        reg = self.get_reg()
        ast.set_adress(adress)
        self.gen_load_adress(reg, self.get_adress_of(ast.get_child(0)))
        self.gen_sw(reg, adress)

        self.restore_tcounter(floating=check_if_floating(ast))


    def visitFunctionDeclaration(self, ast: AST.FunctionDeclaration):
        pass

    def visitFunctionDefinition(self, ast: AST.FunctionDefinition):
        buffer = StringIO()
        label_return = self.get_lname()

        self.reset_adress()
        self.frame_size_stack.append(0)
        self.buffer_stack.append(buffer)
        self.function_label_stack.append(label_return)
        self.gen_sw("$ra", self.gen_stack_adress())
        self.scope_counter += 1

        for a in range(1, ast.get_child_count()):
            arg = ast.get_child(a).get_child(0)
            self.visit(arg)
            adress = self.gen_stack_adress()
            arg.set_adress(adress)
            self.gen_sw('$a' + str(a-1), adress)

        self.visit(ast.get_child(0))
        self.scope_counter -= 1

        # returning
        frame_size = self.frame_size_stack.pop()
        self.print_label(label_return, "return from function " + ast.get_name())
        self.gen_load('$ra', '0($sp)')
        self.print_to_buffer("addi $sp, $sp, " + str(frame_size))
        self.gen_jr('$ra')

        # printing the function correctly
        new_buffer = StringIO()
        old_buffer = self.buffer_stack.pop()

        self.buffer_stack.append(new_buffer)
        self.print_label(ast.get_name(), "define function " + ast.get_name())

        new_buffer = self.buffer_stack.pop()
        new_buffer.write("\n\taddi $sp, $sp, " + str(frame_size*-1))
        new_buffer.write(old_buffer.getvalue())

        self.function_buffers.append(new_buffer)

    def visitReturnStatement(self, ast:AST.ReturnStatement):
        self.visitChildren(ast)
        if not check_if_void(ast):
            self.gen_load('$v0', self.get_adress_of(ast.get_child(0)))
        self.gen_branch_uncon(self.function_label_stack[-1])

    def visitFunctionCall(self, ast:AST.FunctionCall):
        self.visitChildren(ast)
        self.store_rcounter(check_if_floating(ast))

        adress = self.gen_stack_adress()
        ast.set_adress(adress)
        a_counter = 0
        for a in range(ast.get_child_count()):
            self.gen_load('$a' + str(a_counter), self.get_adress_of(ast.get_child(a)))
            a_counter += 1
        self.gen_function_call(ast.get_name())
        self.gen_sw('$v0', adress)
        self.restore_tcounter(floating=check_if_floating(ast))

    def visitForStatement(self, ast: AST.ForStatement):
        loop_check = self.get_lname()
        loop_body = self.get_lname()
        loop_update = self.get_lname()
        loop_end = self.get_lname()

        self.begin_label_stack.append(loop_update)
        self.exit_label_stack.append(loop_end)

        self.visit(ast.get_child(0))
        self.gen_branch_uncon(loop_check)

        self.print_label(loop_check, 'for check')
        self.visit(ast.get_child(1))
        self.gen_branch_con(loop_body, loop_end, self.load_in_reg(ast.get_child(1)))

        self.print_label(loop_update, 'for update')
        self.visit(ast.get_child(2))
        self.gen_branch_uncon(loop_check)

        self.print_label(loop_body, 'for body')
        self.visit(ast.get_child(3))
        self.gen_branch_uncon(loop_update)

        self.begin_label_stack.pop()
        self.exit_label_stack.pop()
        self.print_label(loop_end, 'exit')

    def visitIfStatement(self, ast: AST.IfStatement):
        label_true = self.get_lname()
        label_false = self.get_lname()
        label_end = self.get_lname()

        self.visit(ast.get_child(0))
        if ast.get_child_count() == 3:
            self.gen_branch_con(label_true, label_false, self.load_in_reg(ast.get_child(0)))
        else:
            self.gen_branch_con(label_true, label_end, self.load_in_reg(ast.get_child(0)))

        self.print_label(label_true, 'if true')
        self.visit(ast.get_child(1))
        self.gen_branch_uncon(label_end)

        if ast.get_child_count() == 3:
            self.print_label(label_false, 'if false')
            self.visit(ast.get_child(2))
            self.gen_branch_uncon(label_end)

        self.print_label(label_end, 'exit')

    def visitWhileStatement(self, ast: AST.WhileStatement):
        loop_check = self.get_lname()
        loop_body = self.get_lname()
        loop_end = self.get_lname()

        self.begin_label_stack.append(loop_check)
        self.exit_label_stack.append(loop_end)
        self.gen_branch_uncon(loop_check)

        self.print_label(loop_check, 'while header')
        self.visit(ast.get_child(0))
        self.gen_branch_con(loop_body, loop_end, self.load_in_reg(ast.get_child(0)))

        self.print_label(loop_body, 'while body')
        self.visit(ast.get_child(1))
        self.gen_branch_uncon(loop_check)

        self.begin_label_stack.pop()
        self.exit_label_stack.pop()
        self.print_label(loop_end, 'exit')

    def visitBreak(self, ast: AST.Break):
        self.gen_branch_uncon(self.exit_label_stack[-1])

    def visitContinue(self, ast: AST.Continue):
        self.gen_branch_uncon(self.begin_label_stack[-1])

    def visitCastOp(self, ast: AST.CastOp):
        self.visitChildren(ast)
        conv_type = ast.get_conversion_type()

        if conv_type in {AST.conv_type.BOOL_TO_INT, AST.conv_type.BOOL_TO_CHAR, AST.conv_type.CHAR_TO_INT, AST.conv_type.INT_TO_CHAR}:
            ast.set_adress(self.get_adress_of(ast.get_child(0)))
            return

        adress = self.gen_stack_adress()
        reg = self.get_reg(check_if_floating(ast))
        ast.set_adress(adress)
        var_reg = self.load_in_reg(ast.get_child(0))

        if conv_type == AST.conv_type.INT_TO_BOOL:
            self.gen_comp_instr(reg, var_reg, '$zero', AST.NotEqual(), False)
        elif conv_type in {AST.conv_type.INT_TO_FLOAT, AST.conv_type.BOOL_TO_FLOAT, AST.conv_type.CHAR_TO_FLOAT}:
            self.gen_int_to_float(var_reg, reg)
        elif conv_type in {AST.conv_type.FLOAT_TO_INT, AST.conv_type.FLOAT_TO_CHAR}:
            self.gen_float_to_int(reg, var_reg)
        elif conv_type == AST.conv_type.FLOAT_TO_BOOL:
            freg = self.get_reg(floating=True)
            self.gen_load(freg, self.get_fp_constant(0), True)
            self.gen_comp_instr(reg, var_reg, freg, AST.NotEqual(), True)

        self.gen_sw(reg, adress, check_if_floating(ast))
        self.reset_reg()


    # unary operator
    def get_fp_constant(self, value):
        if value == 0: return "fpzero"
        elif value == 1: return "fpone"
        elif value == -1: return "fpminone"

    def gen_addi(self, reg, lhs, rhs, floating: bool):
        if floating:
            imm_reg = self.get_reg(floating)
            self.gen_load(imm_reg, self.get_fp_constant(rhs), floating)
            self.gen_binary_instruction(reg, lhs, imm_reg, "add.s")
        else: self.print_to_buffer('addi' + ' ' + reg + ', ' + str(lhs) + ', ' + str(rhs))

    def visitIncrPre(self, ast: AST.IncrPre):
        self.visitChildren(ast)
        self.store_rcounter(check_if_floating(ast))

        adress = self.gen_stack_adress()
        floating = check_if_floating(ast.get_child(0))
        reg = self.get_reg(floating)
        var_reg = self.get_reg(floating)

        self.gen_load(var_reg, self.get_adress_of(ast.get_child(0)), floating)
        self.gen_addi(reg, var_reg, 1, floating)
        self.gen_sw(reg, self.get_adress_of(ast.get_child(0)), floating)
        self.gen_sw(reg, adress, floating)
        self.reset_reg()

        ast.set_adress(adress)
        self.restore_tcounter(floating=floating)

    def visitIncrPost(self, ast: AST.IncrPost):
        self.visitChildren(ast)
        self.store_rcounter(check_if_floating(ast))

        adress = self.gen_stack_adress()
        floating = check_if_floating(ast.get_child(0))
        reg = self.get_reg(floating)
        var_reg = self.get_reg(floating)

        self.gen_load(reg, self.get_adress_of(ast.get_child(0)), floating)
        self.gen_addi(var_reg, reg, 1, floating)
        self.gen_sw(var_reg, self.get_adress_of(ast.get_child(0)), floating)
        self.gen_sw(reg, adress, floating)
        self.reset_reg()

        ast.set_adress(adress)
        self.restore_tcounter(floating=floating)

    def visitDecrPre(self, ast: AST.DecrPre):
        self.visitChildren(ast)
        self.store_rcounter(check_if_floating(ast))

        adress = self.gen_stack_adress()
        floating = check_if_floating(ast.get_child(0))
        reg = self.get_reg(floating)
        var_reg = self.get_reg(floating)

        self.gen_load(var_reg, self.get_adress_of(ast.get_child(0)), floating)
        self.gen_addi(reg, var_reg, -1, floating)
        self.gen_sw(reg, self.get_adress_of(ast.get_child(0)), floating)
        self.gen_sw(reg, adress, floating)
        self.reset_reg()

        ast.set_adress(adress)
        self.restore_tcounter(floating=floating)

    def visitDecrPost(self, ast: AST.DecrPost):
        self.visitChildren(ast)
        self.store_rcounter(check_if_floating(ast))

        adress = self.gen_stack_adress()
        floating = check_if_floating(ast.get_child(0))
        reg = self.get_reg(floating)
        var_reg = self.get_reg(floating)

        self.gen_load(reg, self.get_adress_of(ast.get_child(0)), floating)
        self.gen_addi(var_reg, reg, -1, floating)
        self.gen_sw(var_reg, self.get_adress_of(ast.get_child(0)), floating)
        self.gen_sw(reg, adress, floating)

        ast.set_adress(adress)
        self.restore_tcounter(floating=floating)

