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

    if isinstance(op, AST.Sum):
        op_str += 'addu '
    elif isinstance(op, AST.Sub):
        op_str += 'subu '
    elif isinstance(op, AST.Prod):
        op_str += 'mult '
    elif isinstance(op, AST.Div):
        op_str += 'div '
    elif isinstance(op, AST.Mod):
        op_str += 'mod '

    return op_str

def get_comp_instruction(op:AST.CompOp, floating: bool):
    op_str = ''
    if isinstance(op, AST.More):
        if floating:
            op_str += 'ogt '
        else:
            op_str += 'sgt '
    elif isinstance(op, AST.MoreE):
        if floating:
            op_str += 'oge '
        else:
            op_str += 'sge '
    elif isinstance(op, AST.Less):
        if floating:
            op_str += 'olt '
        else:
            op_str += 'slt '
    elif isinstance(op, AST.LessE):
        if floating:
            op_str += 'ole '
        else:
            op_str += 'sle '
    elif isinstance(op, AST.Equal):
        if floating:
            op_str += 'oeq '
        else:
            op_str += 'eq '
    elif isinstance(op, AST.NotEqual):
        if floating:
            op_str += 'one '
        else:
            op_str += 'ne '
    return op_str

def get_logic_instruction(op:AST.LogicOp):
    op_str = ''

    if isinstance(op, AST.And):
        op_str += ' and '
    elif isinstance(op, AST.Or):
        op_str += ' or '

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
    def print_to_file(self, string, ws_str ='\n', modifier = 0):
        for a in range(self.scope_counter + modifier):
            ws_str += '\t'
        self.body_buf.write(ws_str + string)

    def print_to_header(self, string):
        self.header_buf.write('\n' + string)

    def close(self):
        self.file.write(self.header_buf.getvalue() + '\n')
        self.file.write(self.body_buf.getvalue() + '\n')
        self.file.close()
    
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
        self.print_to_file('lw ' + reg + ', ' + str(offset) + '($fp)')

    def gen_load_im(self, reg, value):
        self.print_to_file('li ' + reg + ', ' + str(value))

    def gen_sw(self, value, offset):
        self.print_to_file('sw ' + str(value) + ', ' + str(offset)  + '($fp)')

    def gen_move(self, from_reg, to_reg):
        self.print_to_file('move ' + from_reg + ', ' + to_reg)

    def gen_jal(self, func_name):
        self.print_to_file('jal ' + func_name)

    def gen_jr(self, reg):
        self.print_to_file('jr ' + reg)

    def gen_bne(self, lhs, rhs, label):
        self.print_to_file('bne ' + lhs + ', ' + rhs + ' ' + label)

    def gen_beq(self, lhs, rhs, label):
        self.print_to_file('beq ' + lhs + ', ' + rhs + ' ' + label)

    def gen_mflo(self, res):
        self.print_to_file('mflo ' + res)

    def gen_mfhi(self, res):
        self.print_to_file('mfhi ' + res)

    def gen_mult_or_div(self, res, lhs, rhs, op_str):
        self.print_to_file(op_str + str(lhs) + ', ' + str(rhs))
        self.gen_mflo(res)

    def gen_mod(self, res, lhs, rhs):
        self.print_to_file('div ' + str(lhs) + ', ' + str(rhs))
        self.gen_mfhi(res)

    def gen_binary_instruction(self, res, lhs, rhs, op_str):
        self.print_to_file(op_str + res + ', ' + str(lhs) + ', ' + str(rhs))

    def gen_not(self, res, lhs, type_of):
        self.print_to_file(res + ' = xor ' + type_of + ' ' + str(lhs) + ', 1')

    def gen_math_instr(self, res, lhs, rhs, op: AST.MathOp):
        op_str = get_math_instruction(op, False)
        if op_str == 'mult ' or op_str == 'div ':
            self.gen_mult_or_div(res, lhs, rhs, op_str)
        elif op_str == 'mod ':
            self.gen_mod(res, lhs, rhs)
        else:
            self.gen_binary_instruction(res, lhs, rhs, op_str)

    def gen_comp_instr(self, res, lhs, rhs, op: AST.CompOp):
        # TODO less than or equal is broke
        label_false = self.get_lname()
        label_true = self.get_lname()
        label_continue = self.get_lname()
        
        if isinstance(op, AST.Less): 
            self.gen_binary_instruction(res, lhs, rhs, 'slt ')
            return
        elif isinstance(op, AST.More):
            self.gen_binary_instruction(res, lhs, rhs, 'slt ')
            self.gen_bne(res, '$zero', label_false)
            self.gen_branch_uncon(label_true)
        elif isinstance(op, AST.Equal):
            self.gen_beq(lhs, rhs, label_true)
            self.gen_branch_uncon(label_false)
        elif isinstance(op, AST.MoreE):
            self.gen_binary_instruction(res, lhs, rhs, 'slt ')
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

    def gen_logic_instr(self, res, lhs, rhs, op: AST.LogicOp):
        pass
        # op_str, op_com = get_logic_instruction(op)
        # self.gen_binary_instruction(res, lhs, rhs, type_of, op_str, op_com)

    def gen_syscall(self):
        self.print_to_file('syscall')

    def gen_branch_uncon(self, label): # unconditional branch
        self.print_to_file('beq $zero, $zero, ' + label)

    def gen_branch_con(self, label1, label2, reg): # conditional branch
        self.gen_beq(reg, '$zero', label2)
        self.gen_branch_uncon(label1)

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
        self.print_to_file(string)

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
            self.gen_logic_instr(reg, lhs, rhs, ast)
        elif isinstance(ast, AST.MathOp):
            self.gen_math_instr(reg, lhs, rhs, ast)
        elif isinstance(ast, AST.CompOp):
            self.gen_comp_instr(reg, lhs, rhs, ast)

        offset = self.incr_sp()
        ast.set_offset(offset)
        self.gen_sw(reg, offset)
        self.reset_treg()

    def visitAdress(self, ast: AST.Adress):
        pass

    def visitIndir(self, ast: AST.Indir):
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

    def visitIfStatement(self, ast: AST.IfStatement):
        label_true = self.get_lname()
        label_false = self.get_lname()
        label_end = self.get_lname()

        self.visit(ast.get_child(0))
        if ast.get_child_count() == 3:
            self.gen_branch_con(label_true, label_false, self.load_in_reg(ast.get_child(0)))
        else:
            self.gen_branch_con(label_true, label_end, self.load_in_reg(ast.get_child(0)))

        self.print_label(label_true, 'if ' + ast.get_child(0).get_register() + ' is true')
        self.visit(ast.get_child(1))
        self.gen_branch_uncon(label_end)

        if ast.get_child_count() == 3:
            self.print_label(label_false, 'if ' + ast.get_child(0).get_register() + ' is false')
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