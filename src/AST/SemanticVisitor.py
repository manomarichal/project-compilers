from src.AST.TypeAssignVisitor import TypeAssignVisitor, TypeListener
from src.AST import AST
from src.utility.TypeClass import TypeClass
from sys import stderr


class SemanticVisitor(TypeListener):
    visitor: TypeAssignVisitor
    defined_st_entries: set

    def __init__(self, type_assign_visitor=None):
        TypeListener.__init__(self)
        self.defined_st_entries = set()
        if type_assign_visitor is None:
            self.visitor = TypeAssignVisitor()
            self.visitor.attach(self)
        else:
            self.visitor = type_assign_visitor
            self.visitor.attach(self)

    def visit(self, node):
        self.visitor.visit(node)

    def enterDecl(self, node: AST.Decl):
        entry = node.get_scope().symbol_find(node.get_child(0).get_name())
        if entry in self.defined_st_entries:
            print("redeclaration of variable "+node.get_child(0).get_name(), file=stderr)
        else:
            self.defined_st_entries.add(entry)

    def enterVariable(self, node: AST.Variable):
        entry = node.get_scope().symbol_find(node.get_name())
        if entry not in self.defined_st_entries:
            print("usage of undeclared variable " + node.get_name(), file=stderr)

    def exitAssignOp(self, node: AST.AssignOp, node_type: TypeClass, child_types: list):
        if child_types[0].is_const():
            print("assigning to const type " + child_types[0])
        if not node.get_child(0).isRval():
            print("assigning to lval of type " + child_types[0])

