from src.AST import AST
from src.AST.Visitor import Visitor


class LLVMVisitor(Visitor):

    def get_type(ast: AST.Variable):
        return ast.get_type().__repr__()

    def visitComposite(self, ast:AST.Composite):
        self.visitChildren(ast)

    def visitVariable(self):
        pass





