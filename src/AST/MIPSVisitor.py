from src.AST import AST
from src.AST.Visitor import Visitor
from termcolor import colored, cprint
from src.utility.TypeClass import TypeClass
from io import StringIO

def get_math_instruction(op:AST.MathOp, floating: bool):

    # if floating:
    #     op_str = ' f'
    # else:
    #     op_str = ''
    op_str = ''
    op_com = 'error in get_math_instruction'

    if isinstance(op, AST.Sum):
        op_str += 'addu '
        op_com = ' + '
    elif isinstance(op, AST.Sub):
        op_str += 'subu '
        op_com = ' - '
    elif isinstance(op, AST.Prod):
        op_str += 'mult '
        op_com = ' * '
    elif isinstance(op, AST.Div):
        op_str += 'div '
        op_com = '/'
    elif isinstance(op, AST.Mod):
        op_str += 'mod '
        op_com = ' % '

    return op_str, op_com

def get_comp_instruction(op:AST.CompOp, floating: bool):

    op_str = ''
    op_com = 'error in get_comp_instruction'

    if isinstance(op, AST.More):
        if floating:
            op_str += 'ogt '
        else:
            op_str += 'sgt '
        op_com = ' > '
    elif isinstance(op, AST.MoreE):
        if floating:
            op_str += 'oge '
        else:
            op_str += 'sge '
        op_com = ' >= '
    elif isinstance(op, AST.Less):
        if floating:
            op_str += 'olt '
        else:
            op_str += 'slt '
        op_com = ' < '
    elif isinstance(op, AST.LessE):
        if floating:
            op_str += 'ole '
        else:
            op_str += 'sle '
        op_com = ' <= '
    elif isinstance(op, AST.Equal):
        if floating:
            op_str += 'oeq '
        else:
            op_str += 'eq '
        op_com = ' == '
    elif isinstance(op, AST.NotEqual):
        if floating:
            op_str += 'one '
        else:
            op_str += 'ne '
        op_com = ' != '

    return op_str, op_com

def get_logic_instruction(op:AST.LogicOp):

    op_com = 'error in get_logic_instruction'
    op_str = ''

    if isinstance(op, AST.And):
        op_str += ' and '
        op_com = 'and '
    elif isinstance(op, AST.Or):
        op_str += ' or '
        op_com = 'or '

    return op_str, op_com

def check_for_pointers(node_type, base):
    ptr_depth = 0
    for a in range(len(node_type)-1, -1, -1):
        if node_type[a] == ']':
            break
        if node_type[a] == '*':
            ptr_depth += 1

    for i in range(int(ptr_depth)):
        base += '*'
    return base

def to_array_type(node_type: str, farg = False):
    node_type = node_type[1:len(node_type)-1]
    strs = node_type.split('x')
    strs[0] = strs[0][0:len(strs[0])-1]
    if farg:
        return to_base_type(strs[0]) + '*'
    base = '[' + strs[1] + ' x '
    base += to_base_type(strs[0])
    return check_for_pointers(strs[0], base) + ']'

def to_base_type(node_type):
    if node_type[0:3] == 'int':
        return '4'
    elif node_type[0:5] == 'float':
        return 'float'
    elif node_type[0:4] == 'char':
        return '1'
    elif node_type[0:4] == 'bool':
        return '4'

# TODO void
def to_mips_size(node, farg = False) -> str:
    node_type = node.get_type().__repr__()
    base = ''
    base += to_base_type(node_type)

    # llvm_type = check_for_pointers(node_type, base)
    return base

def get_constant(type_of):
    if type_of == 'i32' or type_of == 'i8':
        return '0'
    elif type_of == 'float':
        return '0.0'
    elif type_of[0] == '[':
        return "zeroinitializer"
    elif is_pointer(type_of):
        return "null"
    else:
        print("oof")

def is_pointer(type_of):
    return type_of[len(type_of)-1] == '*'

class MIPSVisitor(Visitor):
    file = None
    _rcounter = 0 # counter to keep track of registers used
    _lcounter = 0 # counter to keep track of labels used
    _scounter = 0 # counter to keep track of strings used
    _offset = 0
    _tcounter = 0
    cur_func = ''
    exit_label_stack = []
    begin_label_stack = []
    scope_counter = 0

    def __init__(self, file):
        self.header_buf = StringIO()
        self.body_buf = StringIO()
        self.print_to_header(" .text")
        self.print_to_header(".globl main")
        self.file = file

    # HELPER FUNCTIONS
    def print_to_file(self, string, comment=None, ws_str ='\n', ws_comment='\t\t#', modifier = 0):
        for a in range(self.scope_counter + modifier):
            ws_str += '\t'
        self.body_buf.write(ws_str + string)

    def print_to_header(self, string):
        self.header_buf.write('\n' + string)

    def close(self):
        self.file.write(self.header_buf.getvalue() + '\n')
        self.file.write(self.body_buf.getvalue() + '\n')
        self.file.close()

    def get_rname(self) -> str:
        self._rcounter += 1
        return '%t' + str(self._rcounter)
    
    # TODO multiple types
    def incr_sp(self, value = 4):
        self._offset -= value
        return self._offset

    def reset_offset(self):
        self._offset = 0

    def get_treg(self, incr = True):
        reg = self._tcounter
        if incr is True:
            self._tcounter += 1
        if self._tcounter > 8:
            print("max temp registers reached")
        return '$t' + str(reg)

    def reset_treg(self):
        self._tcounter = 0

    def get_lname(self) -> str:
        self._lcounter += 1
        return 'l' + str(self._lcounter)

    def get_strname(self) -> str:
        self._scounter += 1
        return '@.str.' + str(self._scounter)

    def get_register_of(self, ast: AST.Component):
        if isinstance(ast, AST.Index):
            reg = self.get_rname()
            self.gen_getelemntptr_offset(reg, to_mips_size(ast.get_child(0)), ast.get_child(0).get_register(), 0, self.load_in_reg(ast.get_child(1)))
            return reg
        return ast.get_register()

    def load_in_reg(self, ast: AST.Component):
        reg = self.get_treg()
        self.gen_load(reg, ast.get_offset())
        return reg


    # GENERATOR FUNCTIONS
    def print_label(self, label, label_comment):
        self.body_buf.write('\n\n# ' + label_comment)
        self.body_buf.write('\n' + label + ':')
        return label

    def gen_load(self, reg, offset):
        comment = 'load '
        string = 'lw ' + reg + ', ' + str(offset) + '($fp)'
        self.print_to_file(string, comment)

    def gen_load_im(self, reg, value):
        comment = 'load '
        string = 'li ' + reg + ', ' + str(value)
        self.print_to_file(string, comment)

    def gen_sw(self, value, offset):
        comment = 'store '
        string = 'sw ' + str(value) + ', ' + str(offset)  + '($fp)'
        self.print_to_file(string, comment)

    def gen_move(self, from_reg, to_reg):
        comment = 'move ' + from_reg + ' to ' + to_reg
        string = 'move ' + from_reg + ', ' + to_reg
        self.print_to_file(string, comment)

    def gen_jal(self, func_name):
        comment = 'return to ' + func_name
        string = 'jal ' + func_name
        self.print_to_file(string, comment)

    def gen_jr(self, reg):
        comment = 'return to ' + reg
        string = 'jr ' + reg
        self.print_to_file(string, comment)

    def gen_bne(self, lhs, rhs, label):
        comment = 'branch to ' + label + ' if ' + lhs + ' != ' + rhs
        string = 'bne ' + lhs + ', ' + rhs + ' ' + label
        self.print_to_file(string, comment)

    def gen_beq(self, lhs, rhs, label):
        comment = 'branch to ' + label + ' if ' + lhs + ' == ' + rhs
        string = 'beq ' + lhs + ', ' + rhs + ' ' + label
        self.print_to_file(string, comment)

    def gen_mflo(self, res):
        comment = 'move from'
        string = 'mflo ' + res
        self.print_to_file(string, comment)

    def gen_mfhi(self, res):
        comment = 'move from'
        string = 'mfhi ' + res
        self.print_to_file(string, comment)

    def gen_mult_or_div(self, res, lhs, rhs, op_str, op_com):
        comment = res + ' = ' + str(lhs) + op_com + str(rhs)
        string = op_str + str(lhs) + ', ' + str(rhs)
        self.print_to_file(string, comment)
        self.gen_mflo(res)

    def gen_mod(self, res, lhs, rhs):
        comment = res + ' = ' + str(lhs) + ' / ' + str(rhs)
        string = 'div ' + str(lhs) + ', ' + str(rhs)
        self.print_to_file(string, comment)
        self.gen_mfhi(res)

    def gen_binary_instruction(self, res, lhs, rhs, op_str, op_com):
        comment = res + ' = ' + str(lhs) + op_com + str(rhs)
        string = op_str + res + ', ' + str(lhs) + ', ' + str(rhs)
        self.print_to_file(string, comment)

    def gen_not(self, res, lhs, type_of):
        comment = res + ' = ' + str(lhs) + ' xor 1'
        string = res + ' = xor ' + type_of + ' ' + str(lhs) + ', 1'
        self.print_to_file(string, comment)

    def gen_math_instr(self, res, lhs, rhs, type_of, op: AST.MathOp):
        op_str, op_com = get_math_instruction(op, type_of == 'float')
        if op_str == 'mult ' or op_str == 'div ':
            self.gen_mult_or_div(res, lhs, rhs, op_str, op_com)
        elif op_str == 'mod ':
            self.gen_mod(res, lhs, rhs)
        else:
            self.gen_binary_instruction(res, lhs, rhs, op_str, op_com)

    def gen_comp_instr(self, res, lhs, rhs, op: AST.CompOp):
        # TODO less than or equal is broke
        label_false = self.get_lname()
        label_true = self.get_lname()
        label_continue = self.get_lname()
        
        if isinstance(op, AST.Less): 
            self.gen_binary_instruction(res, lhs, rhs, 'slt ', ' / ')
            return
        elif isinstance(op, AST.More):
            self.gen_binary_instruction(res, lhs, rhs, 'slt ', ' / ')
            self.gen_bne(res, '$zero', label_false)
            self.gen_branch_uncon(label_true)
        elif isinstance(op, AST.Equal):
            self.gen_beq(lhs, rhs, label_true)
            self.gen_branch_uncon(label_false)
        elif isinstance(op, AST.MoreE):
            self.gen_binary_instruction(res, lhs, rhs, 'slt ', ' / ')
            self.gen_beq(res, '$zero', label_true)
            self.gen_branch_uncon(label_false)
        elif isinstance(op, AST.LessE):
            self.gen_binary_instruction(res, lhs, rhs, 'slt ', ' / ')
            self.gen_beq(res, '$zero', label_false)
            self.gen_branch_uncon(label_true)

        self.print_label(label_false, 'not true')
        self.gen_load_im(res, 0)
        self.gen_branch_uncon(label_continue)

        self.print_label(label_true, 'true')
        self.gen_load_im(res, 1)
        self.gen_branch_uncon(label_continue)

        self.print_label(label_continue, 'exit comparison')

    def gen_logic_instr(self, res, lhs, rhs, type_of, op: AST.LogicOp):
        op_str, op_com = get_logic_instruction(op)
        self.gen_binary_instruction(res, lhs, rhs, type_of, op_str, op_com)

    def gen_syscall(self):
        comment = 'syscall'
        string = 'syscall'
        self.print_to_file(string, comment)

    def gen_getelementptr(self, reg, type_of, base_ptr):
        comment = 'get adress of ' + base_ptr
        string = reg + ' = getelementptr ' + type_of + ', ' + type_of + '* ' + base_ptr
        self.print_to_file(string, comment)

    def gen_getelemntptr_offset(self, reg, type_of, base_ptr, base = None, offset=None):
        comment = 'get value stored at ' + base_ptr + ' at base ' + str(base) + ' + offset' + str(offset)
        string = reg + ' = getelementptr ' + type_of + ', ' + type_of + '* ' + base_ptr + ', i32 ' + str(base) + ', i32 ' + str(offset)
        self.print_to_file(string, comment)

    def gen_branch_uncon(self, label): # unconditional branch
        comment = 'branch to ' + label
        string = 'beq $zero, $zero, ' + label
        self.print_to_file(string, comment)

    def gen_branch_con(self, label1, label2, reg): # conditional branch
        comment = 'branch to ' + label1 + ' if ' + reg + ' is true, else branch to ' + label2
        string = 'br i1 ' + reg + ', label %' + label1 + ', label %' + label2
        self.print_to_file(string, comment)

    def gen_function_def(self, name, args: {AST.Variable}, frame_size):
        self.reset_offset()
        self.print_label(name, "define function " + name)
        self.gen_sw('$ra', self.incr_sp())

        a_counter = 0
        for arg in args:
            offset = self.incr_sp()
            arg.set_offset(offset)
            self.gen_sw('$a' + str(a_counter), offset)
            a_counter += 1

    def gen_function_call(self, func_name):
        comment = 'call function ' + func_name
        string = 'jal ' + func_name
        self.print_to_file(string, comment)

    def gen_void_return(self):
        self.print_to_file("ret void", "return void")

    def gen_str_constant(self, meta: str, meta_size):
        name = self.get_strname()
        self.print_to_header(name + ' = private unnamed_addr constant [' + str(meta_size) + ' x i8] c' + meta)
        return name

    def gen_default_return(self, rtype):
        if (rtype[0:4] == 'void'):
            self.gen_void_return()
            return
        constant = get_constant(rtype)
        self.gen_return_statement(rtype, constant)
        pass

    def gen_global_var_assign(self, ast: AST.AssignOp):
        var: AST.Variable = ast.get_child(0).get_child(0)
        var.set_register('@' + var.get_name())
        string = '@' + var.get_name() + ' = global ' + to_mips_size(var) + ' ' + str(self.load_in_reg(ast.get_child(1)))
        self.print_to_header(string)

    def gen_global_var_decl(self, ast: AST.Decl):
        var: AST.Variable = ast.get_child(0)
        var.set_register('@' + var.get_name())
        string = '@' + var.get_name() + ' = global ' + to_mips_size(var) + ' ' + get_constant(to_mips_size(var))
        self.print_to_header(string)

    # VISITOR FUNCTIONS
    def visitComposite(self, ast: AST.Composite):
        self.visitChildren(ast)

    def visitLiteral(self, ast: AST.Literal):
        self.reset_treg()
        reg = self.get_treg(False)
        self.gen_load_im(reg, ast.get_value())
        offset = self.incr_sp()
        ast.set_offset(offset)
        self.gen_sw(reg,offset)

    def visitDecl(self, ast: AST.Decl):
        # TODO gvar
        var: AST.Variable = ast.get_child(0)
        var.set_offset(self.incr_sp())

    def visitAssignOp(self, ast: AST.AssignOp):
        # TODO gvar
        self.visitChildren(ast)
        if isinstance(ast.get_child(0), AST.Decl):
            var: AST.Variable = ast.get_child(0).get_child(0)
        else:
            var: AST.Variable = ast.get_child(0)

        self.gen_sw(self.load_in_reg(ast.get_child(1)), var.get_offset())

    def visitPrintf(self, ast: AST.Printf):  #
        self.visitChildren(ast)
        self.gen_load_im('$v0', 1)
        self.gen_load('$a0', ast.get_child(0).get_offset())
        self.gen_syscall()

    def visitNeg(self, ast: AST.Neg):
        self.visitChildren(ast)
        offset = self.incr_sp()
        ast.set_offset(offset)

        reg = self.get_treg()
        self.gen_binary_instruction(reg, '$zero', self.load_in_reg(ast.get_child(0)), 'subu ', ' - ')
        self.gen_sw(reg, offset)

        self.reset_treg()

    def visitNot(self, ast: AST.Not):
        pass

    def visitPos(self, ast: AST.Neg):
        self.visitChildren(ast)
        ast.set_offset(ast.get_child(0).get_offset())

    def visitCastOp(self, ast: AST.CastOp):
        self.visitChildren(ast)
        ast.set_offset(ast.get_child(0).get_offset())

    def visitBinaryOp(self, ast: AST.BinaryOp):
        self.visitChildren(ast)
        reg = self.get_treg()
        lhs, rhs = self.load_in_reg(ast.get_child(0)), self.load_in_reg(ast.get_child(1))

        if isinstance(ast, AST.LogicOp):
            self.gen_logic_instr(reg, lhs, rhs, to_mips_size(ast.get_child(0)), ast)
        elif isinstance(ast, AST.MathOp):
            self.gen_math_instr(reg, lhs, rhs, to_mips_size(ast), ast)
        elif isinstance(ast, AST.CompOp):
            self.gen_comp_instr(reg, lhs, rhs, to_mips_size(ast.get_child(0)), ast)

        offset = self.incr_sp()
        ast.set_offset(offset)
        self.gen_sw(reg, offset)
        self.reset_treg()

    def visitAdress(self, ast: AST.Adress):
        self.visitChildren(ast)
        reg = self.get_rname()
        ast.set_register(reg)
        self.gen_getelementptr(reg, to_mips_size(ast.get_child(0)), ast.get_child(0).get_register())

    def visitIndir(self, ast: AST.Indir):
        self.visitChildren(ast)
        reg = self.get_rname()
        self.gen_load(reg, self.get_register_of(ast.get_child(0)), to_mips_size(ast.get_child(0)))
        ast.set_register(reg)
        pass

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
        print(self.incr_sp())
        self.scope_counter -= 1

    def visitReturnStatement(self, ast:AST.ReturnStatement):
        self.visitChildren(ast)
        self.gen_load('$v0', ast.get_child(0).get_offset())
        self.gen_load('$ra', -8)
        self.gen_jr('$ra')

    def visitFunctionCall(self, ast:AST.FunctionCall):
        self.visitChildren(ast)
        offset = self.incr_sp()
        ast.set_offset(offset)
        a_counter = 0
        for a in range(ast.get_child_count()):
            self.gen_load('$a' + str(a_counter), ast.get_child(0).get_offset())
            a_counter += 1
        self.gen_function_call(ast.get_name())
        self.gen_sw('$v0', offset)

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

    def visitBreak(self, ast: AST.Break):
        self.gen_branch_uncon(self.exit_label_stack[-1])

    def visitContinue(self, ast: AST.Continue):
        self.gen_branch_uncon(self.begin_label_stack[-1])