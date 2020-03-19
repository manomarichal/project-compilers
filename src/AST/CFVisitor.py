from src.AST import AST
from src.AST.Visitor import Visitor
from src.utility.TypeClass import TypeClass

def create_literal(value, lhs: AST.Literal, rhs:AST.Literal):
    lit = AST.Literal()



class CFVisitor(Visitor):
    def visit(self, tree):
        return tree.accept(self)

    def visitComposite(self, ast):
        self.visitChildren(ast)

    def visitMathOp(self, ast):
        self.visitChildren(ast)

        if not (isinstance (ast.get_child(0), AST.Literal) and isinstance(ast.get_child(1), AST.Literal)): return

        value = 0
        if isinstance(ast, AST.Sum):
            value = ast.get_child(0).get_value() + ast.get_child(1).get_value()
        elif isinstance(ast, AST.Sub):
            value = ast.get_child(0).get_value() - ast.get_child(1).get_value()
        elif isinstance(ast, AST.Prod):
            value = ast.get_child(0).get_value() * ast.get_child(1).get_value()
        elif isinstance(ast, AST.Div):
            value = ast.get_child(0).get_value() / ast.get_child(1).get_value()
        elif isinstance(ast, AST.Mod):
            value = ast.get_child(0).get_value() % ast.get_child(1).get_value()
        else:
            print("invalid math operator found while constant folding")

        ast.get_parent().replace_child(ast, create_literal(value))

    def visitCompOp(self, ast):
        self.visitChildren(ast)

        if not (isinstance(ast.get_child(0), AST.Literal) and isinstance(ast.get_child(1), AST.Literal)): return

        value = False
        if isinstance(ast, AST.Equal):
            value = ast.get_child(0).get_value() == ast.get_child(1).get_value()
        elif isinstance(ast, AST.NotEqual):
            value = ast.get_child(0).get_value() != ast.get_child(1).get_value()
        elif isinstance(ast, AST.More):
            value = ast.get_child(0).get_value() > ast.get_child(1).get_value()
        elif isinstance(ast, AST.Less):
            value = ast.get_child(0).get_value() < ast.get_child(1).get_value()
        elif isinstance(ast, AST.MoreE):
            value = ast.get_child(0).get_value() >= ast.get_child(1).get_value()
        elif isinstance(ast, AST.LessE):
            value = ast.get_child(0).get_value() <= ast.get_child(1).get_value()
        else:
            print("invalid comparison operator found while constant folding")

        ast.get_parent().replace_child(ast, create_literal(value))

    def visitLogicOp(self, ast):
        self.visitChildren(ast)

        if not isinstance(ast.get_child(0), AST.Literal): return

        if isinstance(ast, AST.Not):
            value = not (ast.get_child(0).get_value() != 0)
        elif isinstance(ast.get_child(1), AST.Literal):
            if isinstance(ast, AST.Or):
                value = (ast.get_child(0).get_value() != 0) or (ast.get_child(1).get_value() != 0)
            elif isinstance(ast, AST.And):
                value = (ast.get_child(0).get_value() != 0) and (ast.get_child(1).get_value() != 0)
            else:
                print("invalid logic operator found while constant folding")
                exit(1)
        else:
            print("something went wrong when constant folding with a logic operator")
            exit(1)

        ast.get_parent().replace_child(ast, create_literal(value))

    def visitUnaryOp(self, ast):
        self.visitChildren(ast)

        if not isinstance(ast.get_child(0), AST.Literal): return

        if isinstance(ast, AST.Pos):
            ast.get_parent().replace_child(ast, AST.Literal(ast.get_child(0).get_value()))
        elif isinstance(ast, AST.Neg):
            ast.get_parent().replace_child(ast, AST.Literal(-ast.get_child(0).get_value()))
        elif isinstance(ast, AST.Adress): return
        elif isinstance(ast, AST.Indir): return
        else:
            print("something went wrong when constant folding with an unary operator")
            exit(1)

    def visitAssignOp(self, ast: AST.AssignOp):
        self.visitChildren(ast)

        if ast.get_child(0).get_child(0).get_type().is_const():
            ast.get_parent().replace_child(ast, create_literal(ast.get_child(1).get_value()))


