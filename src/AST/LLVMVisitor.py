from src.AST import AST
from src.AST.Visitor import Visitor
from termcolor import colored, cprint


def to_llvm_type(var) -> str:
    var_type = var.get_type().__repr__()
    if var_type == 'int':
        return 'i32'
    elif var_type == 'float':
        return 'float'
    elif var_type == 'char':
        return 'i8'
    elif var_type == 'None':
        # TODO literals hebben soms none type
        return 'none'
    else:
        print('invalid type')
        exit(0)


class LLVMVisitor(Visitor):
    file = None
    _rcounter = 0

    def __init__(self, file):
        self.file = file
        # self.file.write('declare i32 @printf(i8*, ...)\n'
        #
        #               'define void @print(i32 %a){\n'
        #                '\t%p = call i32 (i8*, ...)\n'
        #                '\t\t@printf(i8* getelementptr inbounds (i32 0, i32 0),\n'
        #                '\t\t\ti32 %a)\n'
        #                '\tret void\n'
        #                '}\n\n')
        # self.file.write('\ndeclare void @printf(i32)')
        self.file.write('define i32 @main() {\n\tstart:')

    # HELPER FUNCTIONS
    def print_to_file(self, string, comment=None):
        if comment is not None:
            color = colored(comment, 'green')
            print("{: <30} {: <30} ".format(string, color))
        else:
            print("{: <30}".format(string))
        self.file.write('\n\t; ' + comment)
        self.file.write('\n\t\t' + string)

    def close(self):
        self.file.write('\n\t' + 'ret i32 0\n}\n')
        self.file.close()

    def load_var_in_reg(self, var: AST.Variable):
        reg = self.get_rname()
        comment = 'load ' + str(var.get_name()) + ' in ' + reg
        string = reg + ' = load ' + to_llvm_type(var) + ', ' + to_llvm_type(var) + '* ' + str(var.get_register())
        self.print_to_file(string, comment)
        return reg

    def get_rname(self) -> str:
        self._rcounter += 1
        return '%t' + str(self._rcounter)

    def math_opp(self, res, lhs: AST.Component, rhs: AST.Component, ast: AST.MathOp):

        if isinstance(ast, AST.Sum):
            op_str = ' add '
            op_com = ' + '
        elif isinstance(ast, AST.Sub):
            op_str = ' sub '
            op_com = ' - '
        elif isinstance(ast, AST.Prod):
            op_str = ' mul '
            op_com = ' * '
        elif isinstance(ast, AST.Div):
            op_str = ' mod '
            op_com = ' / '
        elif isinstance(ast, AST.Mod):
            op_str = ' mod '
            op_com = ' % '
        else:
            print("invalid math operator found while constant folding")

        if isinstance(lhs, AST.Variable):
            lhs_reg = self.load_var_in_reg(lhs)
        else:
            lhs_reg = lhs.get_register()

        if isinstance(rhs, AST.Variable):
            rhs_reg = self.load_var_in_reg(rhs)
        else:
            rhs_reg = rhs.get_register()

        comment = res + ' = ' + lhs_reg + op_com + rhs_reg
        string = res + ' =' + op_str + to_llvm_type(lhs) + ' ' + lhs_reg + ', ' + rhs_reg
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

        reg = '%' + var.get_name()

        comment = 'assign ' + ast.get_child(1).get_register() + ' to ' + reg
        string = 'store ' + to_llvm_type(var) + ' ' + str(
            ast.get_child(1).get_register() + ', ' + to_llvm_type(var) + '* ' + reg)
        self.print_to_file(string, comment)

    def visitMathOp(self, ast: AST.MathOp):
        self.visitChildren(ast)
        reg = self.get_rname()
        ast.set_register(reg)

        self.math_opp(reg, ast.get_child(0), ast.get_child(1), ast)

    def visitLiteral(self, ast: AST.Literal):
        reg = self.get_rname()
        ast.set_register(reg)

        comment = 'load ' + str(ast.get_value()) + ' in ' + reg
        string = reg + ' = add ' + to_llvm_type(ast) + ' ' + str(ast.get_value()) + ', ' + '0'
        self.print_to_file(string, comment)

    def visitPrintf(self, ast: AST.Printf):  # TODO

        if isinstance(ast.get_child(0), AST.Variable):
            reg = self.load_var_in_reg(ast.get_child(0))
        else:
            reg = ast.get_child(0).get_register()

        comment = 'print ' + reg
        string = 'call i32 @printf(i8* %p, i32 ' + reg + ')'

        # TODO printf afmaken
        # self.print_to_file(string, comment)
