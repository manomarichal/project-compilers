from src.AST import AST
from src.AST.Visitor import Visitor
from src.utility.SemanticExceptions import StatementException, UndeclaredError, RedeclaredError, RValError, ConstAssignmentError


class UntypedSemanticVisitor(Visitor):
    defined_st_entries: set
    warnings: list
    errors: list

    def __init__(self):
        self.defined_st_entries = set()
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

    def visitVariable(self, node: AST.Variable):
        entry = node.get_st_entry()
        if entry is None or entry not in self.defined_st_entries:
            if entry not in self.defined_st_entries:
                self.error(UndeclaredError(node))

    def visitAdress(self, node: AST.Adress):
        if not node.get_child(0).is_lval():
            self.error(RValError(node))


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
