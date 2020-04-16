from src.AST import AST
from src.AST.Visitor import Visitor
from src.utility.SemanticExceptions import *


class UntypedSemanticVisitor(Visitor):
    defined_st_entries: set
    uninitialised_st_entries: set
    warnings: list
    errors: list

    def __init__(self):
        self.defined_st_entries = set()
        self.uninitialised_st_entries = set()
        self.warnings = list()
        self.errors = list()

    def visit_outside_statement(self, node):
        try:
            return self.visit(node)
        except StatementException:
            pass

    def warn(self, warning):
        self.warnings.append(warning)

    def error(self, error):
        self.errors.append(error)
        raise error

    def visitComposite(self, node):
        self.visitChildren(node)

    def visitDoc(self, node: AST.Doc):
        for child_nr in range(node.get_child_count()):
            self.visit_outside_statement(node.get_child(child_nr))

    def visitDecl(self, node: AST.Decl):
        entry = node.get_scope().symbol_find(node.get_child(0).get_name())
        if entry in self.defined_st_entries:
            self.error(RedeclaredError(node.get_child(0)))
        else:
            self.defined_st_entries.add(entry)
            if not isinstance(node.get_parent(), AST.AssignOp):
                self.uninitialised_st_entries.add(entry)

    def visitVariable(self, node: AST.Variable):
        entry = node.get_st_entry()
        if entry is None or entry not in self.defined_st_entries:
            self.error(UndeclaredError(node))
        else:
            if entry in self.uninitialised_st_entries:
                if isinstance(node.get_parent(), AST.AssignOp) and node.get_parent().get_child(0) is node:
                    self.uninitialised_st_entries.remove(entry)
                else:
                    self.warn(UninitialisedWarning(node))

    def visitAdress(self, node: AST.Adress):
        if not node.get_child(0).is_lval():
            self.error(RValError(node))

        self.visit(node.get_child(0))

    def visitAssignOp(self, node: AST.AssignOp):
        if not node.get_child(0).is_lval():
            self.error(RValError(node, "in lhs"))

        # order matters! because of uninitialised warnings
        self.visit(node.get_child(1))
        self.visit(node.get_child(0))

    def visitFunctionDefinition(self, node: AST.FunctionDefinition):
        for argNr in range(1, node.get_child_count()):
            self.visitFunctionArg(node.get_child(argNr))
        self.visit(node.get_child(0))

    def visitFunctionArg(self, node: AST.Decl):
        entry = node.get_scope().symbol_find(node.get_child(0).get_name())
        if entry in self.defined_st_entries:
            self.error(RedeclaredError(node.get_child(0)))
        else:
            self.defined_st_entries.add(entry)


class TypedSemanticsVisitor(Visitor):
    warnings: list
    errors: list

    def __init__(self):
        self.warnings = list()
        self.errors = list()

    def visit_outside_statement(self, node):
        try:
            return self.visit(node)
        except StatementException:
            pass

    def warn(self, warning):
        self.warnings.append(warning)

    def error(self, error):
        self.errors.append(error)
        raise error

    def visitComposite(self, node):
        self.visitChildren(node)

    def visitDoc(self, node: AST.Doc):
        for child_nr in range(node.get_child_count()):
            self.visit_outside_statement(node.get_child(child_nr))

    def visitAssignOp(self, node: AST.AssignOp):
        if node.get_type().is_const() and not isinstance(node.get_child(0), AST.Decl):
            self.error(ConstAssignmentError(node))

        self.visit(node.get_child(0))
        self.visit(node.get_child(1))
