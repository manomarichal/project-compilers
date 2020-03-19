from src.AST import AST
from src.AST.Visitor import Visitor
from src.utility.TypeClass import TypeClass

class CFVisitor(Visitor):
    def visit(self, tree):
        return tree.accept(self)

    def visitComposite(self, ast):
        self.visitChildren(ast)



