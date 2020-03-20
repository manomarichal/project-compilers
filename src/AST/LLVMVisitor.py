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
        op_str += 'mod '
        op_com = ' % '

    return op_str, op_com

def get_comp_instruction(op:AST.CompOp, floating: bool):

    if floating:
        op_str = ' fcmp '
    else:
        op_str = ' icmp '

    op_com = 'error in get_comp_instruction'

    if isinstance(op, AST.More):
        op_str += 'sgt '
        op_com = ' > '
    elif isinstance(op, AST.MoreE):
        op_str += 'sge '
        op_com = ' >= '
    elif isinstance(op, AST.Less):
        op_str += 'slt '
        op_com = ' < '
    elif isinstance(op, AST.LessE):
        op_str += 'sle '
        op_com = ' <= '
    elif isinstance(op, AST.Equal):
        op_str += 'eq '
        op_com = ' == '
    elif isinstance(op, AST.NotEqual):
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
        print('invalid type')
        exit(0)


class LLVMVisitor(Visitor):
    file = None
    _rcounter = 0

    def __init__(self, file):
        self.file = file
        self.file.write("declare i32 @printf(i8*, ...)")
        self.file.write("\n@istr = private constant [4 x i8] c\"%d\\0A\\00\"")
        self.file.write("\n@fstr = private constant [4 x i8] c\"%f\\0A\\00\"")
        self.file.write('\ndefine i32 @main() {\n\tstart:')

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
    
    def get_reg(self, ast: AST.Component):
        # variables have to be loaded in before being used
        if isinstance(ast, AST.Variable):
            return self.generate_load(ast)
        else:
            return ast.get_register()

    # GENERATOR FUNCTIONS
    def generate_load(self, var: AST.Variable):
        reg = self.get_rname()
        comment = 'load ' + str(var.get_name()) + ' in ' + reg
        string = reg + ' = load ' + to_llvm_type(var) + ', ' + to_llvm_type(var) + '* ' + str(var.get_register())
        self.print_to_file(string, comment)
        return reg

    def generate_store(self, var: AST.Variable, org: str):
        comment = 'assign ' + org + ' to ' + var.get_register()
        string = 'store ' + to_llvm_type(var) + ' ' + org + ', ' + to_llvm_type(var) + '* ' + var.get_register()
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

    # %X = fpext float 3.125 to double (%X = 3.125000e+00)
    def generate_fpext(self, reg, from_type, to_type, value):
        comment = 'fp zero extent ' + from_type + ' ' + value + ' to ' + to_type
        string = reg + ' = fpext ' + from_type + ' ' + value + ' to ' + to_type
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

        self.generate_store(var, ast.get_child(1).get_register())

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
        self.generate_store(ast.get_child(0), reg)                          # store variable

    def visitIncrPost(self, ast: AST.IncrPost):
        self.visitChildren(ast)
        reg = self.generate_load(ast.get_child(0))
        ast.set_register(reg)
        var_reg = self.get_rname()
        self.generate_math_instr(var_reg, reg, 1, to_llvm_type(ast.get_child(0)), AST.Sum())
        self.generate_store(ast.get_child(0), var_reg)

    def visitDecrPre(self, ast: AST.DecrPre):
        self.visitChildren(ast)
        reg = self.get_rname()
        ast.set_register(reg)
        var_reg = self.generate_load(ast.get_child(0))
        self.generate_math_instr(reg, var_reg, 1, to_llvm_type(ast.get_child(0)), AST.Sub())
        self.generate_store(ast.get_child(0), reg)

    def visitDecrPost(self, ast: AST.DecrPost):
        self.visitChildren(ast)
        reg = self.generate_load(ast.get_child(0))
        ast.set_register(reg)
        var_reg = self.get_rname()
        self.generate_math_instr(var_reg, reg, 1, to_llvm_type(ast.get_child(0)), AST.Sub())
        self.generate_store(ast.get_child(0), var_reg)

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
        elif ast.get_conversion_type() == AST.conv_type.BOOL_TO_INT:
            self.generate_zext(reg, 'i1', 'i32', var_reg)
        #TODO conversions from and to floats

    def visitBinaryOp(self, ast: AST.BinaryOp):
        self.visitChildren(ast)
        reg = self.get_rname()
        ast.set_register(reg)
        lhs, rhs = self.get_reg(ast.get_child(0)), self.get_reg(ast.get_child(1))

        if isinstance(ast, AST.LogicOp):
            self.generate_logic_instr(reg, lhs, rhs, to_llvm_type(ast), ast)
        elif isinstance(ast, AST.MathOp):
            self.generate_math_instr(reg, lhs, rhs, to_llvm_type(ast), ast)
        elif isinstance(ast, AST.CompOp):
            self.generate_comp_instr(reg, lhs, rhs, 'i32', ast)



