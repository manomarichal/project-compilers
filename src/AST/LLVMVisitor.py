from src.AST import AST
from src.AST.Visitor import Visitor
from termcolor import colored, cprint
from src.utility.TypeClass import TypeClass

def get_math_instruction(op:AST.MathOp, floating: bool):

    if floating:
        op_str = ' f'
    else:
        op_str = ' '

    op_com = 'error in get_math_instruction'

    if isinstance(op, AST.Sum):
        op_str += 'add '
        op_com = ' + '
    elif isinstance(op, AST.Sub):
        op_str += 'sub '
        op_com = ' - '
    elif isinstance(op, AST.Prod):
        op_str += 'mul '
        op_com = ' * '
    elif isinstance(op, AST.Div):
        if op_str == ' f': op_str = ' fdiv '
        else: op_str += 'sdiv '
        op_com = ' / '
    elif isinstance(op, AST.Mod):
        if op_str == ' f': op_str = ' frem '
        else: op_str += 'srem '
        op_com = ' % '

    return op_str, op_com

def get_comp_instruction(op:AST.CompOp, floating: bool):

    if floating:
        op_str = ' fcmp '
    else:
        op_str = ' icmp '

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
        op_com = ' and '
    elif isinstance(op, AST.Or):
        op_str += ' or '
        op_com = ' or '

    return op_str, op_com

def to_pointer(node_type):
    if node_type[0:3] == 'int':
        base = 'i32'
        ptr_depth = len(node_type[3:])/2
    elif node_type[0:5] == 'float':
        base = 'float'
        ptr_depth = len(node_type[5:])/2
    elif node_type[0:4] == 'bool':
        base = 'i1'
        ptr_depth = len(node_type[4:])/2
    elif node_type[0:4] == 'char':
        base = 'i8'
        ptr_depth = len(node_type[4:]) / 2

    for i in range(int(ptr_depth)):
        base += '*'
    return base

def to_llvm_type(node) -> str:
    node_type = node.get_type().__repr__()
    if node_type == 'int':
        return 'i32'
    elif node_type == 'float':
        return 'float'
    elif node_type == 'char':
        return 'i8'
    elif node_type == 'bool':
        return 'i1'
    else:
        return to_pointer(node_type)


class LLVMVisitor(Visitor):
    file = None
    _rcounter = 0 # counter to keep track of registers used
    _lcounter = 0 # counter to keep track of labels used

    def __init__(self, file):
        self.file = file
        self.file.write("declare i32 @printf(i8*, ...)")
        self.file.write("\n@istr = private constant [4 x i8] c\"%d\\0A\\00\"")
        self.file.write("\n@fstr = private constant [4 x i8] c\"%f\\0A\\00\"")
        self.file.write('\ndefine i32 @main() {\n\nstart:')

    # HELPER FUNCTIONS
    def print_to_file(self, string, comment=None):
        self.file.write('\n\t; ' + comment)
        self.file.write('\n\t\t' + string)

    def close(self):
        self.file.write('\n\t' + 'ret i32 0\n}\n')
        self.file.close()

    def get_rname(self) -> str:
        self._rcounter += 1
        return '%t' + str(self._rcounter)

    def get_lname(self) -> str:
        self._lcounter += 1
        return 'l' + str(self._lcounter)

    def get_reg(self, ast: AST.Component):
        # variables have to be loaded in before being used
        if isinstance(ast, AST.Variable) or isinstance(ast, AST.Indir):
            return self.generate_load(ast)
        else:
            return ast.get_register()

    # GENERATOR FUNCTIONS
    def print_label(self, label, label_comment):
        self.file.write('\n\n; ' + label_comment)
        self.file.write('\n' + label + ':')
        return label

    def generate_load(self, var: AST.Variable):
        reg = self.get_rname()
        comment = 'load ' + str(var.get_register()) + ' in ' + reg
        string = reg + ' = load ' + to_llvm_type(var) + ', ' + to_llvm_type(var) + '* ' + str(var.get_register())
        self.print_to_file(string, comment)
        return reg

    def generate_store(self, value, destination, type_of):
        comment = 'assign ' + value + ' to ' + destination
        string = 'store ' + type_of + ' ' + value + ', ' + type_of + '* ' + destination
        self.print_to_file(string, comment)

    def generate_binary_instruction(self, res, lhs, rhs, type_of, op_str, op_com):
        comment = res + ' = ' + str(lhs) + op_com + str(rhs)
        string = res + ' =' + op_str + type_of + ' ' + str(lhs) + ', ' + str(rhs)
        self.print_to_file(string, comment)

    def generate_math_instr(self, res, lhs, rhs, type_of, op: AST.MathOp):
        op_str, op_com = get_math_instruction(op, type_of == 'float')
        self.generate_binary_instruction(res, lhs, rhs, type_of, op_str, op_com)

    def generate_comp_instr(self, res, lhs, rhs, type_of, op: AST.CompOp):
        op_str, op_com = get_comp_instruction(op, type_of == 'float')
        self.generate_binary_instruction(res, lhs, rhs, type_of, op_str, op_com)

    def generate_logic_instr(self, res, lhs, rhs, type_of, op: AST.LogicOp):
        op_str, op_com = get_logic_instruction(op)
        self.generate_binary_instruction(res, lhs, rhs, type_of, op_str, op_com)

    def generate_int_printf(self, reg, type_of):
        comment = 'print ' + reg
        string = self.get_rname() + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @istr,i32 0, i32 0)," + type_of + " " + reg + ")"
        self.print_to_file(string, comment)

    def generate_float_printf(self, reg):
        comment = 'print ' + reg
        string = self.get_rname() + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @fstr,i32 0, i32 0), double " + reg + ")"
        self.print_to_file(string, comment)

    # %X = trunc i32 235 to i1 (%X = 1)
    def generate_trunc(self, reg, from_type, to_type, value):
        comment = 'convert ' + from_type + ' ' + value + ' to ' + to_type
        string = reg + ' = trunc ' + from_type + ' ' + value + ' to ' + to_type
        self.print_to_file(string, comment)

    # %X = zext i1 1 to i32 (%X = 00000..1)
    def generate_zext(self, reg, from_type, to_type, value):
        comment = 'zero extent ' + from_type + ' ' + value + ' to ' + to_type
        string = reg + ' = zext ' + from_type + ' ' + value + ' to ' + to_type
        self.print_to_file(string, comment)

    # %X = fpext float 3.125 to double     ; yields double: 3.125000e+00)
    def generate_fpext(self, reg, from_type, to_type, value):
        comment = 'fp zero extent ' + from_type + ' ' + value + ' to ' + to_type
        string = reg + ' = fpext ' + from_type + ' ' + value + ' to ' + to_type
        self.print_to_file(string, comment)

    # %X = sitofp i32 257 to float         ; yields float:257.0
    def generate_sitofp(self, reg, from_type, to_type, value):
        comment = 'signed int ' + from_type + ' ' + value + ' to ' + to_type
        string = reg + ' = sitofp ' + from_type + ' ' + value + ' to ' + to_type
        self.print_to_file(string, comment)
    # %X = uitofp i32 257 to float         ; yields float:257.0
    def generate_uitofp(self, reg, from_type, to_type, value):
        comment = 'unsigned int ' + from_type + ' ' + value + ' to ' + to_type
        string = reg + ' = uitofp ' + from_type + ' ' + value + ' to ' + to_type
        self.print_to_file(string, comment)

    # %X = fptosi double -123.0 to i32      ; yields i32:-123
    def generate_fptosi(self, reg, from_type, to_type, value):
        comment = 'float ' + from_type + ' ' + value + ' to signed ' + to_type
        string = reg + ' = fptosi ' + from_type + ' ' + value + ' to ' + to_type
        self.print_to_file(string, comment)

    # %X = fptoui double 123.0 to i32      ; yields i32:123
    def generate_fptoui(self, reg, from_type, to_type, value):
        comment = 'float ' + from_type + ' ' + value + ' to unsigned ' + to_type
        string = reg + ' = fptoui ' + from_type + ' ' + value + ' to ' + to_type
        self.print_to_file(string, comment)

    # <result> = getelementptr <ty>, <ty>* <ptrval>{, [inrange] <ty> <idx>}*
    def generate_getelementptr(self, reg, type_of, base_ptr):
        comment = 'get adress of ' + base_ptr
        string = reg + ' = getelementptr ' + type_of + ', ' + type_of + '* ' + base_ptr
        self.print_to_file(string, comment)

    def generate_branch_uncon(self, label1): # unconditional branch
        comment = 'branch to ' + label1
        string = 'br label %' + label1
        self.print_to_file(string, comment)

    def generate_branch_con(self, label1, label2, reg): # conditional branch
        comment = 'branch to ' + label1 + ' if ' + reg + ' is true, else branch to ' + label2
        string = 'br i1 ' + reg + ', label %' + label1 + ', label %' + label2
        self.print_to_file(string, comment)



    # VISITOR FUNCTIONS
    def visitComposite(self, ast: AST.Composite):
        self.visitChildren(ast)

    def visitDecl(self, ast: AST.Decl):
        var: AST.Variable = ast.get_child(0)
        comment = 'init ' + var.get_register() + ' as ' + var.get_name()
        string = '%' + var.get_name() + ' = alloca ' + to_llvm_type(var)
        self.print_to_file(string, comment)

    def visitAssignOp(self, ast: AST.AssignOp):
        self.visitChildren(ast)

        # assignment could also be a definition
        if isinstance(ast.get_child(0), AST.Decl):
            var: AST.Variable = ast.get_child(0).get_child(0)
        else:
            var: AST.Variable = ast.get_child(0)

        self.generate_store(self.get_reg(ast.get_child(1)), var.get_register(), to_llvm_type(var))

    def visitLiteral(self, ast: AST.Literal):
        reg = self.get_rname()
        ast.set_register(reg)
        if to_llvm_type(ast) == 'float':
            c = '0.0'
        else:
            c = '0'
        self.generate_math_instr(reg, ast.get_value(), c, to_llvm_type(ast), AST.Sum())

    def visitPrintf(self, ast: AST.Printf):  #
        self.visitChildren(ast)
        reg = self.get_reg(ast.get_child(0))

        if to_llvm_type(ast.get_child(0)) != 'float':
            self.generate_int_printf(reg, to_llvm_type(ast.get_child(0)))
        else:
            # we first need to convert the float for a double (because reasons)
            c_reg = self.get_rname()
            self.generate_fpext(c_reg, 'float', 'double', reg)
            self.generate_float_printf(c_reg)

    def visitIncrPre(self, ast: AST.IncrPre):
        self.visitChildren(ast)
        reg = self.get_rname()                                              # reserve register
        ast.set_register(reg)
        var_reg = self.generate_load(ast.get_child(0))                      # load child variable in var_reg
        self.generate_math_instr(reg, var_reg, 1, to_llvm_type(ast.get_child(0)), AST.Sum())  # increase by 1
        self.generate_store(reg, ast.get_child(0).get_register(), to_llvm_type(ast.get_child(0)))                          # store variable

    def visitIncrPost(self, ast: AST.IncrPost):
        self.visitChildren(ast)
        reg = self.generate_load(ast.get_child(0))
        ast.set_register(reg)
        var_reg = self.get_rname()
        self.generate_math_instr(var_reg, reg, 1, to_llvm_type(ast.get_child(0)), AST.Sum())
        self.generate_store(var_reg, ast.get_child(0).get_register(), to_llvm_type(ast.get_child(0)))                          # store variable

    def visitDecrPre(self, ast: AST.DecrPre):
        self.visitChildren(ast)
        reg = self.get_rname()
        ast.set_register(reg)
        var_reg = self.generate_load(ast.get_child(0))
        self.generate_math_instr(reg, var_reg, 1, to_llvm_type(ast.get_child(0)), AST.Sub())
        self.generate_store(reg, ast.get_child(0).get_register(), to_llvm_type(ast.get_child(0)))                          # store variable

    def visitDecrPost(self, ast: AST.DecrPost):
        self.visitChildren(ast)
        reg = self.generate_load(ast.get_child(0))
        ast.set_register(reg)
        var_reg = self.get_rname()
        self.generate_math_instr(var_reg, reg, 1, to_llvm_type(ast.get_child(0)), AST.Sub())
        self.generate_store(var_reg, ast.get_child(0).get_register(), to_llvm_type(ast.get_child(0)))                          # store variable

    def visitNeg(self, ast: AST.Neg):
        self.visitChildren(ast)
        var_reg = self.get_reg(ast.get_child(0))
        reg = self.get_rname()
        ast.set_register(reg)
        self.generate_math_instr(reg, var_reg, -1, to_llvm_type(ast.get_child(0)), AST.Prod())

    def visitPos(self, ast: AST.Neg):
        self.visitChildren(ast)
        reg = self.get_reg(ast.get_child(0))
        ast.set_register(reg)

    def visitCastOp(self, ast: AST.CastOp):
        self.visitChildren(ast)
        reg = self.get_rname()
        ast.set_register(reg)
        var_reg = self.get_reg(ast.get_child(0))

        if ast.get_conversion_type() == AST.conv_type.INT_TO_BOOL:
            self.generate_trunc(reg, 'i32', 'i1', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.INT_TO_FLOAT:
            self.generate_sitofp(reg, 'i32', 'float', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.BOOL_TO_INT:
            self.generate_zext(reg, 'i1', 'i32', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.BOOL_TO_FLOAT:
            self.generate_uitofp(reg, 'i1', 'float', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.FLOAT_TO_BOOL:
            self.generate_fptoui(reg, 'float', 'i1', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.FLOAT_TO_INT:
            self.generate_fptosi(reg, 'float', 'i32', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.FLOAT_TO_CHAR:
            self.generate_fptosi(reg, 'float', 'i8', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.INT_TO_CHAR:
            self.generate_trunc(reg, 'i32', 'i8', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.BOOL_TO_CHAR:
            self.generate_zext(reg, 'i1', 'i8', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.CHAR_TO_FLOAT:
            self.generate_sitofp(reg, 'i8', 'float', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.CHAR_TO_BOOL:
            self.generate_trunc(reg, 'i8', 'i1', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.CHAR_TO_INT:
            self.generate_zext(reg, 'i8', 'i32', var_reg)


    def visitBinaryOp(self, ast: AST.BinaryOp):
        self.visitChildren(ast)
        reg = self.get_rname()
        ast.set_register(reg)
        lhs, rhs = self.get_reg(ast.get_child(0)), self.get_reg(ast.get_child(1))

        if isinstance(ast, AST.LogicOp):
            self.generate_logic_instr(reg, lhs, rhs, to_llvm_type(ast.get_child(0)), ast)
        elif isinstance(ast, AST.MathOp):
            self.generate_math_instr(reg, lhs, rhs, to_llvm_type(ast), ast)
        elif isinstance(ast, AST.CompOp):
            self.generate_comp_instr(reg, lhs, rhs, to_llvm_type(ast.get_child(0)), ast)

    def visitAdress(self, ast: AST.Adress):
        self.visitChildren(ast)
        reg = self.get_rname()
        ast.set_register(reg)
        self.generate_getelementptr(reg, to_llvm_type(ast.get_child(0)), ast.get_child(0).get_register())

    def visitIndir(self, ast: AST.Indir):
        self.visitChildren(ast)
        adress_of_pointee = self.generate_load(ast.get_child(0))
        ast.set_register(adress_of_pointee)

    def visitIfStatement(self, ast: AST.IfStatement):
        label_true = self.get_lname()
        label_false = self.get_lname()
        label_end = self.get_lname()

        self.visit(ast.get_child(0))
        self.generate_branch_con(label_true, label_false, self.get_reg(ast.get_child(0)))

        self.print_label(label_true, 'if ' + ast.get_child(0).get_register() + ' is true')
        self.visit(ast.get_child(1))
        self.generate_branch_uncon(label_end)

        self.print_label(label_false, 'if ' + ast.get_child(0).get_register() + ' is false')
        self.visit(ast.get_child(2))
        self.generate_branch_uncon(label_end)

        self.print_label(label_end, 'exit')

    def visitScope(self, ast: AST.Scope):
        self.visitChildren(ast)

    def visitWhileConstr(self, ast: AST.WhileConstr):
        # counter = self.get_rname()
        # op_str, op_com = get_logic_instruction(AST.And())
        # # set counter to zero
        # self.generate_binary_instruction(counter, 0, 0, 'i1', op_str, op_com)

        loop_check = self.get_lname()
        loop_body = self.get_lname()
        loop_end = self.get_lname()

        self.generate_branch_uncon(loop_check)

        self.print_label(loop_check, 'while header')
        self.visit(ast.get_child(0))
        self.generate_branch_con(loop_body, loop_end, self.get_reg(ast.get_child(0)))

        self.print_label(loop_body, 'while body')
        self.visit(ast.get_child(1))
        self.generate_branch_uncon(loop_check)

        self.print_label(loop_end, 'exit')
