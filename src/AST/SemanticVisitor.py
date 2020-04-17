from src.AST import AST
from src.AST.Visitor import Visitor
from src.utility.SemanticExceptions import *
from src.utility import SymbolTable
from src.utility.TypeClass import *


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

    def visit_children_outside_statement(self, node):
        for child_nr in range(node.get_child_count()):
            self.visit_outside_statement(node.get_child(child_nr))

    def warn(self, warning):
        self.warnings.append(warning)

    def error(self, error):
        self.errors.append(error)
        raise error

    def visitComposite(self, node: AST.Composite):
        self.visitChildren(node)

    def visitScope(self, node: AST.Scope):
        self.visit_children_outside_statement(node)

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
                child: Component = node
                parent: Composite = child.get_parent()
                while isinstance(parent, AST.Index):
                    if not parent.get_child(0) is child:
                        self.warn(UninitialisedWarning(node))
                        return
                    child = parent
                    parent = parent.get_parent()

                if isinstance(parent, AST.AssignOp) and parent.get_child(0) is child:
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
        entry = node.get_scope().symbol_find(node.get_name())
        if entry in self.defined_st_entries:
            self.error(RedeclaredError(node))
        else:
            self.defined_st_entries.add(entry)

        for argNr in range(1, node.get_child_count()):
            self.visit_function_arg(node.get_child(argNr))
        self.visit_outside_statement(node.get_child(0))

    def visit_function_arg(self, node: AST.Decl):
        entry: SymbolTable.FuncEntry = node.get_scope().symbol_find(node.get_child(0).get_name())
        if entry in self.defined_st_entries:
            self.error(RedeclaredError(node.get_child(0)))
        else:
            self.defined_st_entries.add(entry)

    def visitFunctionCall(self, node: AST.FunctionCall):
        entry: SymbolTable.FuncEntry = node.get_scope().symbol_find(node.get_name())
        if entry is None or entry not in self.defined_st_entries:
            self.error(UndeclaredError(node))
        if entry.arg_count != node.get_child_count():
            self.error(ArgCountMismatchError(node, entry.arg_count, node.get_child_count()))

    def visitReturnStatement(self, node: AST.ReturnStatement):
        function = node.get_enclosing(AST.FunctionDefinition)
        if function is None:
            self.error(IllegalStatementError(node, "no enclosing function definition"))
        self.visitChildren(node)


# TODO: internal state and weird upkeep is getting a bit much -> helper functions? subclassing? separate passes?
class TypedSemanticsVisitor(Visitor):
    # warnings: list
    # errors: list
    # returns_awaiting: list[bool]  # stack to support nested function definitions
    # block_exited: list[bool]  # stack of currently active blocks: whether they are GUARANTEED to have exited already
    # last_scope_exited: bool  # whether the last popped scope (≠ block) was guaranteed to have exited
    # unused_code_warned: bool  # whether a warning has already been given about code after current block exit

    def __init__(self):
        self.warnings = list()
        self.errors = list()
        self.returns_awaiting = list()
        self.block_exited = list()
        self.last_scope_exited = False
        self.unused_code_warned = False

    # preferably don't use, visit_children version does a bunch of extra upkeep
    def visit_outside_statement(self, node):
        try:
            return self.visit(node)
        except StatementException:
            pass

    def visit_children_outside_statement(self, node):
        tmp = self.unused_code_warned
        self.unused_code_warned = False
        self.block_exited.append(False)
        for child_nr in range(node.get_child_count()):
            self.visit_outside_statement(node.get_child(child_nr))
        if type(node) == AST.Scope:
            self.last_scope_exited = self.block_exited[len(self.block_exited) - 1]
        self.block_exited.pop()
        self.unused_code_warned = tmp

    def warn(self, warning):
        self.warnings.append(warning)

    def error(self, error):
        self.errors.append(error)
        raise error

    def visit(self, node):
        if len(self.block_exited) > 0 and self.block_exited[len(self.block_exited)-1] and not self.unused_code_warned:
            self.unused_code_warned = True
            self.warn(UnusedCodeWarning(node))
        super().visit(node)

    def visitComposite(self, node: AST.Composite):
        self.visitChildren(node)

    def visitScope(self, node: AST.Scope):
        self.visit_children_outside_statement(node)

    def visitDoc(self, node: AST.Doc):
        self.visit_children_outside_statement(node)

    def visitAssignOp(self, node: AST.AssignOp):
        if node.get_type().is_const() and not isinstance(node.get_child(0), AST.Decl):
            self.error(ConstAssignmentError(node))
        self.visitChildren(node)

    def visitFunctionDefinition(self, node: AST.FunctionDefinition):
        if not node.get_type() == TypeClass([TypeComponents.VOID]):
            self.returns_awaiting.append(True)
            self.visit_children_outside_statement(node)
            missing_return = self.returns_awaiting[len(self.returns_awaiting)-1]
            self.returns_awaiting.pop()
            if missing_return:
                self.error(MissingReturnError(node))
            if not self.last_scope_exited:
                self.warn(NoReturnWarning(node))
        else:
            self.visitChildren(node)

    def visitReturnStatement(self, node: AST.ReturnStatement):
        self.visitChildren(node)
        if node.get_enclosing(AST.FunctionDefinition) is None:
            self.error(IllegalStatementError(node, "no enclosing function definition"))
        self.returns_awaiting[len(self.returns_awaiting)-1] = False
        self.block_exited[len(self.block_exited)-1] = True

    def visitContinue(self, node: AST.Continue):
        if node.get_enclosing(AST.ForStatement) is None and node.get_enclosing(AST.WhileStatement):
            self.error(IllegalStatementError(node, "no enclosing loop construct"))
        self.block_exited[len(self.block_exited)-1] = True

    def visitBreak(self, node: AST.Break):
        if node.get_enclosing(AST.ForStatement) is None \
                and node.get_enclosing(AST.WhileStatement) is None \
                and node.get_enclosing(AST.CaseBranch) is None \
                and node.get_enclosing(AST.DefaultBranch) is None:
            self.error(IllegalStatementError(node, "no enclosing switch branch or loop"))
        self.block_exited[len(self.block_exited)-1] = True
