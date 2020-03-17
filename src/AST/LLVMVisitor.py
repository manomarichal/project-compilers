from src.AST import AST
from src.AST.Visitor import Visitor
from enum import Enum
from termcolor import colored, cprint


def to_llvm_type(var) -> str:
    var_type = var.get_type().__repr__()
    if var_type == 'int':
        return 'i32'
    elif var_type == 'float':
        return 'float'
    elif var_type == 'char':
        return 'i32'
    elif var_type == 'None':
        # TODO literals hebben soms none type
        return 'none'
    else:
        print('invalid type')
        exit(0)


def math_opp(res, lhs: AST.Component ,rhs: AST.Component, ast: AST.MathOp):

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

    lhs_reg = lhs.get_register()
    rhs_reg = lhs.get_register()

    comment = colored(' // ' + res + ' = ' + lhs_reg + op_com + rhs_reg + '\t', 'green')
    print("{: <35} ".format(res + ' =' + op_str + to_llvm_type(lhs) + ', *' + lhs_reg))
    print("{: <35} {: <35} ".format(res + ' =' + op_str + to_llvm_type(rhs) + ', *' + rhs_reg, comment))

class LLVMVisitor(Visitor):

    _rcounter = 0

    # HELPER FUNCTIONS
    def _get_rname(self) -> str:
        self._rcounter += 1
        return '%t' + str(self._rcounter)

    def visitComposite(self, ast: AST.Composite):
        self.visitChildren(ast)


    def visitDecl(self, ast: AST.Decl):
        var: AST.Variable = ast.get_child(0)
        comment = colored('// init '+ var.get_register() + ' as ' + var.get_name() + '\t', 'green')
        
        print("{: <35} {: <35} ".format('%' + var.get_name() + ' = alloca ' + to_llvm_type(var), comment))

    def visitAssignOp(self, ast:AST.AssignOp):
        self.visitChildren(ast)

        # assignment could also be a definition
        if isinstance(ast.get_child(0), AST.Decl):
            var: AST.Variable = ast.get_child(0).get_child(0)
        else:
            var: AST.Variable = ast.get_child(0)

        reg = '%' + var.get_name()
        
        comment = colored(' // assign ' + ast.get_child(1).get_register() + ' to ' + reg + '\t', 'green')
        print("{: <35} {: <35} ".format(reg + ' = load ' + to_llvm_type(var) + ', *' + str(ast.get_child(1).get_register()), comment))

    def visitMathOp(self, ast: AST.MathOp):

        self.visitChildren(ast)

        if not (isinstance(ast.get_child(0), AST.Literal) and isinstance(ast.get_child(1), AST.Literal)): return


        self.visitChildren(ast)
        reg = self._get_rname()
        ast.set_register(reg)
        math_opp(reg, ast.get_child(0), ast.get_child(1), )

    def visitLiteral(self, ast: AST.Literal):
        reg = self._get_rname()
        ast.set_register(reg)

        comment = colored(' // load ' + str(ast.get_value()) + ' in ' + reg + '\t', 'green')
        print("{: <35} {: <35} ".format(reg + ' = load ' + to_llvm_type(ast) + ', ' + str(ast.get_value()), comment))

    








