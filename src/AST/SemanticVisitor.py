from src.AST.Visitor import Visitor
from src.AST import AST
from sys import stderr


class SemanticVisitor(Visitor):
    def __init__(self):
        self.defined_st_entries = set()

    def visitDecl(self, node: AST.Decl):
        entry = node.get_scope().symbol_find(node.get_name())
        if entry in self.defined_st_entries:
            print("redeclaration of variable "+node.get_name(), file=stderr)
        else:
            self.defined_st_entries.add(entry)

    def visitVariable(self, node:AST.Variable):
        entry = node.get_scope().symbol_find(node.get_name())
        if entry not in self.defined_st_entries:
            print("usage of undeclared variable " + node.get_name(), file=stderr)

    def visitMathOp(self, node:AST.MathOp):
        pass

