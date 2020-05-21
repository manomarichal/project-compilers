from src.AST import AST
from src.AST.Visitor import Visitor
from termcolor import colored, cprint
from src.utility.TypeClass import TypeClass
from io import StringIO

def check_if_floating(ast: AST.Component):
    return ast.get_type().__repr__()[0:5] == 'float'

def get_math_instruction(op:AST.MathOp, floating: False):
    op_str = ''
    if isinstance(op, AST.Sum): op_str += 'add'
    elif isinstance(op, AST.Sub): op_str += 'subu'
    elif isinstance(op, AST.Prod): op_str += 'mul'
    elif isinstance(op, AST.Div): op_str += 'div'
    elif isinstance(op, AST.Mod): op_str += 'mod'
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
    _fcounter = 0
    _fpcounter = 0
    cur_func = ''
    exit_label_stack = []
    begin_label_stack = []
    scope_counter = 0

    def __init__(self, file):
        self.header_buf = StringIO()
        self.body_buf = StringIO()
        self.print_to_header(".data")
        self.print_to_header("fpzero: .float 0.0")
        self.print_to_header("fpone: .float 1.0")
        self.print_to_file(" .text")
        self.print_to_file(".globl main")
        self.file = file

    # HELPER FUNCTIONS
    def print_to_file(self, string, ws_str ='\n', modifier = 0):
        for a in range(self.scope_counter + modifier):
            ws_str += '\t'
        self.body_buf.write(ws_str + string)

    def print_to_header(self, string):
        self.header_buf.write(string + '\n')

    def close(self):
        self.file.write(self.header_buf.getvalue() + '\n')
        self.file.write(self.body_buf.getvalue() + '\n')
        self.file.close()
    
    def gen_fp_adress(self, value = 4) -> str:
        self._adress -= value
        return str(self._adress) + "($fp)"

    def reset_adress(self):
        self._adress = 0

    def get_reg(self, floating = False, incr = True):
        if self._tcounter > 8 or self._fcounter > 8:
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

    def reset_reg(self):
        self._tcounter = 0
        self._fcounter = 0

    def get_lname(self) -> str:
        self._lcounter += 1
        return 'l' + str(self._lcounter)

    def load_in_reg(self, ast: AST.Component):
        floating = check_if_floating(ast)
        reg = self.get_reg(floating)
        self.gen_load(reg, self.get_adress_of(ast), floating)
        return reg

    def get_adress_of(self, ast: AST.Component):
        if isinstance(ast, AST.Indir):
            reg = self.get_reg()
            self.gen_load(reg, self.get_adress_of(ast.get_child(0)))
            return '0(' + reg + ')'
        else:
            return ast.get_adress()
        
    # GENERATOR FUNCTIONS
    def print_label(self, label, label_comment):
        self.body_buf.write('\n\n# ' + label_comment)
        self.body_buf.write('\n' + label + ':')
        return label

    def gen_load(self, reg, adress, floating = False):
        if not floating:
            self.print_to_file('lw ' + reg + ', ' + adress)
        else:
            self.print_to_file('lwc1 ' + reg + ', ' + adress)

    def gen_global_var(self, name, value, floating = False):
        if floating:
            self.print_to_header(name + ': .float ' + str(value))
        else:
            self.print_to_header(name + ': .int ' + str(value))

    def gen_load_im(self, reg, value):
        self.print_to_file('li ' + reg + ', ' + str(value))

    def gen_load_adress(self, reg, adress):
        self.print_to_file('la ' + reg + ', ' + adress)

    def gen_load_dereference(self, reg, pointer):
        self.print_to_file('lw ' + reg + ', 0(' + str(pointer) + ')')

    def gen_sw(self, value, adress, floating = False):
        if not floating:
            self.print_to_file('sw ' + str(value) + ', ' + adress)
        else:
            self.print_to_file('swc1 ' + str(value) + ', ' + adress)

    def gen_move(self, from_reg, to_reg, floating = False):
        self.print_to_file('move ' + from_reg + ', ' + to_reg)
        if not floating:
            self.print_to_file('move ' + from_reg + ', ' + to_reg)
        else:
            self.print_to_file('move.s ' + from_reg + ', ' + to_reg)

    def gen_jal(self, func_name):
        self.print_to_file('jal ' + func_name)

    def gen_jr(self, reg):
        self.print_to_file('jr ' + reg)

    def gen_bne(self, lhs, rhs, label):
        self.print_to_file('bne ' + lhs + ', ' + rhs + ' ' + label)

    def gen_beq(self, lhs, rhs, label):
        self.print_to_file('beq ' + lhs + ', ' + rhs + ' ' + label)

    def gen_int_to_float(self, ireg, freg):
        self.print_to_file('mtc1 ' + ireg + ', ' + freg )
        self.print_to_file('cvt.s.w ' + freg + ', ' + freg)

    def gen_float_to_int(self, ireg, freg):
        self.print_to_file('cvt.s.w ' + freg + ', ' + freg)
        self.print_to_file('mfc1 ' + freg + ', ' + ireg )

    def gen_mflo(self, res):
        self.print_to_file('mflo ' + res)

    def gen_mfhi(self, res):
        self.print_to_file('mfhi ' + res)

    def gen_mult_or_div(self, res, lhs, rhs, op_str):
        self.print_to_file(op_str + ' ' + res + ', ' + str(lhs) + ', ' + str(rhs))
        self.gen_mflo(res)

    def gen_mod(self, res, lhs, rhs):
        self.print_to_file('div ' + ' ' + res + ', ' + str(lhs) + ', ' + str(rhs))
        self.gen_mfhi(res)

    def gen_binary_instruction(self, res, lhs, rhs, op_str):
        self.print_to_file(op_str + ' ' + res + ', ' + str(lhs) + ', ' + str(rhs))

    def gen_neg(self, lhs, rhs, floating = False):
        if not floating:
            self.print_to_file('neg ' + lhs + ', ' + rhs)
        else:
            self.print_to_file('neg.s ' + lhs + ', ' + rhs)

    def gen_not(self, res, lhs, type_of):
        self.print_to_file(res + ' = xor ' + type_of + ' ' + str(lhs) + ', 1')

    def gen_or(self, res, lhs, rhs):
        self.print_to_file('or ' +  str(res) + ', ' + str(lhs) + ', ' + str(rhs))

    def gen_and(self, res, lhs, rhs):
        self.print_to_file('and ' +  str(res) + ', ' + str(lhs) + ', ' + str(rhs))

    def gen_math_instr(self, res, lhs, rhs, op: AST.MathOp, floating = False):
        op_str = get_math_instruction(op, floating)
        if op_str == 'mul' or op_str == 'div':
            self.gen_mult_or_div(res, lhs, rhs, op_str)
        elif op_str == 'mod':
            self.gen_mod(res, lhs, rhs)
        else:
            self.gen_binary_instruction(res, lhs, rhs, op_str)

    def gen_comp_instr_float(self, lhs, rhs, op: AST.CompOp, label_true):
        if isinstance(op, AST.Less):
            self.gen_binary_instruction(lhs, rhs, label_true, "c.lt.s")
        elif isinstance(op, AST.LessE):
            self.gen_binary_instruction(lhs, rhs, label_true, "c.le.s")
        elif isinstance(op, AST.Equal):
            self.gen_binary_instruction(lhs, rhs, label_true, "c.eq.s")

    def gen_comp_instr(self, res, lhs, rhs, op: AST.CompOp, floating):
        # TODO less than or equal is broke
        label_false = self.get_lname()
        label_true = self.get_lname()
        label_continue = self.get_lname()

        if not floating:
            self.gen_binary_instruction(lhs, rhs, label_true, gen_comp_instruction_int(op))
            self.gen_branch_uncon(label_false)
        else:
            self.gen_comp_instr_float(res, lhs, rhs, op)
            self.gen_branch_float(label_true, True)
            self.gen_branch_uncon(label_false)

        self.print_label(label_false, 'not true')
        if floating: self.gen_load(res, "$fpzero", True)
        else: self.gen_load_im(res, 0)
        self.gen_branch_uncon(label_continue)

        self.print_label(label_true, 'true')
        if floating: self.gen_load(res, "$fpone", True)
        else: self.gen_load_im(res, 1)
        self.gen_branch_uncon(label_continue)

        self.print_label(label_continue, 'exit comparison')

    def gen_logic_instr(self, res, lhs, rhs, op: AST.LogicOp):
        op_str = get_logic_instruction(op)
        self.gen_binary_instruction(res, lhs, rhs, op_str)

    def gen_syscall(self):
        self.print_to_file('syscall')

    def gen_branch_uncon(self, label, floating = False): # unconditional branch
        self.print_to_file('beq $zero, $zero, ' + label)

    def gen_branch_con(self, label1, label2, reg): # conditional branch
        self.gen_beq(reg, '$zero', label2)
        self.gen_branch_uncon(label1)

    def gen_branch_float(self, label, type_of: bool):
        if type_of: self.print_to_file('bc1t ' + label)
        else: self.print_to_file('bc1f ' + label)

    def gen_function_def(self, name, args: {AST.Variable}, frame_size):
        self.reset_adress()
        self.print_label(name, "define function " + name)
        self.gen_sw('$ra', self.gen_fp_adress())

        a_counter = 0
        for arg in args:
            adress = self.gen_fp_adress()
            arg.set_adress(adress)
            self.gen_sw('$a' + str(a_counter), adress)
            a_counter += 1

    def gen_function_call(self, func_name):
        self.print_to_file('jal ' + func_name)

    # VISITOR FUNCTIONS
    def visitComposite(self, ast: AST.Composite):
        self.visitChildren(ast)

    def visitLiteral(self, ast: AST.Literal):
        self.reset_reg()
        reg = self.get_reg(check_if_floating(ast))

        if check_if_floating(ast):
            name = self.get_fp_name()
            self.gen_global_var(name, ast.get_value(), True)
            self.gen_load(reg, name, True)
        else:
            self.gen_load_im(reg, ast.get_value())

        adress = self.gen_fp_adress()
        ast.set_adress(adress)
        self.gen_sw(reg,adress, check_if_floating(ast))

    def visitDecl(self, ast: AST.Decl):
        # TODO gvar
        var: AST.Variable = ast.get_child(0)
        var.set_adress(self.gen_fp_adress())

    def visitAssignOp(self, ast: AST.AssignOp):
        # TODO gvar
        self.visitChildren(ast)
        if isinstance(ast.get_child(0), AST.Decl):
            var: AST.Variable = ast.get_child(0).get_child(0)
        else:
            var: AST.Variable = ast.get_child(0)

        self.gen_sw(self.load_in_reg(ast.get_child(1)), self.get_adress_of(var), check_if_floating(ast))
        self.reset_reg()

    def visitPrintf(self, ast: AST.Printf):  #
        self.visitChildren(ast)
        if check_if_floating(ast.get_child(0)):
            self.gen_load_im('$v0', 2)
            self.gen_load('$f12', self.get_adress_of(ast.get_child(0)), True)
        else:
            self.gen_load_im('$v0', 1)
            self.gen_load('$a0', self.get_adress_of(ast.get_child(0)))
        self.gen_syscall()

    def visitNeg(self, ast: AST.Neg):
        self.visitChildren(ast)
        adress = self.gen_fp_adress()
        ast.set_adress(adress)

        reg = self.get_reg()
        self.gen_neg(reg, reg, check_if_floating(ast))
        self.gen_sw(reg, adress, check_if_floating(ast))

        self.reset_reg()

    def visitNot(self, ast: AST.Not):
        pass

    def visitPos(self, ast: AST.Neg):
        self.visitChildren(ast)
        ast.set_adress(self.get_adress_of(ast.get_child(0)))

    def visitBinaryOp(self, ast: AST.BinaryOp):
        self.visitChildren(ast)
        reg = self.get_reg(check_if_floating(ast))
        lhs, rhs = self.load_in_reg(ast.get_child(0)), self.load_in_reg(ast.get_child(1))
        floating = check_if_floating(ast)

        if isinstance(ast, AST.MathOp):
            self.gen_math_instr(reg, lhs, rhs, ast, floating)
        elif isinstance(ast, AST.CompOp):
            self.gen_comp_instr(reg, lhs, rhs, ast, floating)
        elif isinstance(ast, AST.LogicOp):
            self.gen_logic_instr(reg, lhs, rhs, ast)


        adress = self.gen_fp_adress()
        ast.set_adress(adress)
        self.gen_sw(reg, adress, check_if_floating(ast))
        self.reset_reg()

    def visitAdress(self, ast: AST.Adress):
        self.visitChildren(ast)
        adress = self.gen_fp_adress()
        reg = self.get_reg()
        ast.set_adress(adress)
        self.gen_load_adress(reg, self.get_adress_of(ast.get_child(0)))
        self.gen_sw(reg, adress)
        self.reset_reg()

    def visitIndir(self, ast: AST.Indir):
        self.visitChildren(ast)

    def visitFunctionDeclaration(self, ast: AST.FunctionDeclaration):
        pass

    # TODO default returns
    def visitFunctionDefinition(self, ast: AST.FunctionDefinition):
        self.scope_counter += 1
        args = []
        frame_size = 4 * (len(args) + 1)
        for a in range(1, ast.get_child_count()):
            self.visit(ast.get_child(a).get_child(0))
            args.append(ast.get_child(a).get_child(0))

        self.cur_func = ast.get_name() # for array definitions
        self.gen_function_def(ast.get_name(), args, frame_size)
        self.visit(ast.get_child(0))
        print(self.gen_fp_adress())
        self.scope_counter -= 1

    def visitReturnStatement(self, ast:AST.ReturnStatement):
        self.visitChildren(ast)
        self.gen_load('$v0', self.get_adress_of(ast.get_child(0)))
        self.gen_load('$ra', '-8($fp)')
        # self.gen_jr('$ra')

    def visitFunctionCall(self, ast:AST.FunctionCall):
        self.visitChildren(ast)
        adress = self.gen_fp_adress()
        ast.set_adress(adress)
        a_counter = 0
        for a in range(ast.get_child_count()):
            self.gen_load('$a' + str(a_counter), self.get_adress_of(ast.get_child(0)))
            a_counter += 1
        self.gen_function_call(ast.get_name())
        self.gen_sw('$v0', adress)

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

        if ast.get_conversion_type() in {AST.conv_type.BOOL_TO_INT, AST.conv_type.BOOL_TO_CHAR, AST.conv_type.CHAR_TO_INT, AST.conv_type.INT_TO_CHAR}:
            ast.set_adress(ast.get_child(0).get_adress())
            return

        adress = self.gen_fp_adress()
        reg = self.get_reg(check_if_floating(ast))
        ast.set_adress(adress)
        var_reg = self.load_in_reg(ast.get_child(0))

        if ast.get_conversion_type() == AST.conv_type.INT_TO_BOOL:
            self.gen_comp_instr(reg, var_reg, '$zero', AST.NotEqual())
        elif ast.get_conversion_type() in {AST.conv_type.INT_TO_FLOAT, AST.conv_type.BOOL_TO_FLOAT, AST.conv_type.CHAR_TO_FLOAT}:
            self.gen_int_to_float(var_reg, reg)
        elif ast.get_conversion_type() in {AST.conv_type.FLOAT_TO_INT, AST.conv_type.FLOAT_TO_CHAR}:
            self.gen_float_to_int(reg, var_reg)

        self.gen_sw(reg, adress, check_if_floating(ast))
        self.reset_reg()