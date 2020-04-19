from src.AST import AST
from src.AST.Visitor import Visitor
from src.utility.SemanticExceptions import *
from src.utility import SymbolTable
from src.utility.TypeClass import *


class UntypedSemanticVisitor(Visitor):
    # defined_var_entries: set{VarEntry}
    # uninitialised_var_entries: set{VarEntry}
    # declared_function_entries: set{FunctionEntry}
    # defined_function_entries: set{FunctionEntry}
    # warnings: list[SemanticException]
    # errors: list[SemanticException]
    # has_main: bool
    # has_IO: bool  # TODO: actual includes maybe?

    def __init__(self):
        self.defined_var_entries = set()
        self.uninitialised_var_entries = set()
        self.declared_function_entries = set()
        self.defined_function_entries = set()
        self.warnings = list()
        self.errors = list()
        self.has_main = False
        self.has_IO = False

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

    def assume_single_rval(self, node: AST.Composite):
        if not node.get_child(0).is_lval():
            self.error(RValError(node))

    def visitComposite(self, node: AST.Composite):
        self.visitChildren(node)

    def visitScope(self, node: AST.Scope):
        self.visit_children_outside_statement(node)

    def visitDoc(self, node: AST.Doc):
        self.has_IO = node.IO
        for child_nr in range(node.get_child_count()):
            self.visit_outside_statement(node.get_child(child_nr))
        if not self.has_main:
            self.error(NoMainError(node))

    def visitDecl(self, node: AST.Decl):
        entry = node.get_scope().symbol_find(node.get_child(0).get_name())
        if entry in self.defined_var_entries:
            self.error(RedeclaredError(node.get_child(0)))
        else:
            self.defined_var_entries.add(entry)
            if not isinstance(node.get_parent(), AST.AssignOp):
                self.uninitialised_var_entries.add(entry)

    def visitVariable(self, node: AST.Variable):
        entry = node.get_st_entry()
        if entry is None or entry not in self.defined_var_entries:
            self.error(UndeclaredError(node))
        else:
            if entry in self.uninitialised_var_entries:
                child: Component = node
                parent: Composite = child.get_parent()
                while isinstance(parent, AST.Index) or isinstance(parent, AST.Adress):
                    if not parent.get_child(0) is child:
                        self.warn(UninitialisedWarning(node))
                        return
                    child = parent
                    parent = parent.get_parent()

                # TODO: maybe ScanF inherits FunctionCall? otherwise, clean this up
                if (isinstance(parent, AST.AssignOp) and parent.get_child(0) is child)\
                        or (isinstance(parent, AST.FunctionCall) or isinstance(parent, AST.Scanf)):
                    self.uninitialised_var_entries.remove(entry)
                else:
                    self.warn(UninitialisedWarning(node))

    def visitAdress(self, node: AST.Adress):
        self.assume_single_rval(node)
        self.visit(node.get_child(0))

    def visitIncrPre(self, node: AST.IncrPre):
        self.assume_single_rval(node)
        self.visit(node.get_child(0))

    def visitIncrPost(self, node):
        self.assume_single_rval(node)
        self.visit(node.get_child(0))

    def visitDecrPre(self, node):
        self.assume_single_rval(node)
        self.visit(node.get_child(0))

    def visitDecrPost(self, node):
        self.assume_single_rval(node)
        self.visit(node.get_child(0))

    def visitAssignOp(self, node: AST.AssignOp):
        if not node.get_child(0).is_lval():
            self.error(RValError(node, "in lhs"))

        # order matters! because of uninitialised warnings
        self.visit(node.get_child(1))
        self.visit(node.get_child(0))

    def visitFunctionDefinition(self, node: AST.FunctionDefinition):
        if node.get_name() == "main":
            self.has_main = True

        entry = node.get_st_entry()

        self.verify_func_def_signature(node, entry)

        nest = node.get_enclosing(AST.FunctionDefinition)
        if nest is not None:
            self.error(NestedFunctionError(node, nest))

        if entry not in self.declared_function_entries:
            self.declared_function_entries.add(entry)

        if entry in self.defined_function_entries:
            self.error(RedeclaredError(node))
        else:
            self.defined_function_entries.add(entry)

        for argNr in range(1, node.get_child_count()):
            self.visit_function_arg(node.get_child(argNr))
        self.visit_outside_statement(node.get_child(0))

    def visitFunctionDeclaration(self, node: AST.FunctionDeclaration):
        entry = node.get_st_entry()

        self.verify_func_decl_signature(node, entry)

        nest = node.get_enclosing(AST.FunctionDefinition)
        if nest is not None:
            self.error(NestedFunctionError(node, nest))

        if entry not in self.declared_function_entries:
            self.declared_function_entries.add(entry)

    def verify_func_decl_signature(self, node: AST.FunctionDeclaration, entry: SymbolTable.FuncEntry):
        node_args = [node.get_child(i).get_child(0).get_type() for i in range(node.get_child_count())]
        if node_args != entry.arg_types:
            self.error(SignatureMismatchError(node, (node_args, node.get_type()), (entry.arg_types, entry.type_obj)))

    def verify_func_def_signature(self, node: AST.FunctionDefinition, entry: SymbolTable.FuncEntry):
        node_args = [node.get_child(i).get_child(0).get_type() for i in range(1, node.get_child_count())]
        if node_args != entry.arg_types:
            self.error(SignatureMismatchError(node, (node_args, node.get_type()), (entry.arg_types, entry.type_obj)))

    def visit_function_arg(self, node: AST.Decl):
        entry: SymbolTable.VarEntry = node.get_child(0).get_st_entry()
        if entry in self.defined_var_entries:
            self.error(RedeclaredError(node.get_child(0)))
        else:
            self.defined_var_entries.add(entry)

    def visitFunctionCall(self, node: AST.FunctionCall):
        entry: SymbolTable.FuncEntry = node.get_scope().symbol_find(node.get_name())
        if entry is None:
            self.error(UndeclaredError(node))
        if entry not in self.declared_function_entries:
            self.warn(ImplicitDeclarationWarning(node))
        if entry.arg_count != node.get_child_count():
            self.error(ArgCountMismatchError(node, entry.arg_count, node.get_child_count()))

    def visitReturnStatement(self, node: AST.ReturnStatement):
        function = node.get_enclosing(AST.FunctionDefinition)
        if function is None:
            self.error(IllegalStatementError(node, "no enclosing function definition"))
        self.visitChildren(node)

    # TODO - correct scoping (decl in body not usable in check)
    def visitWhileStatement(self, node: AST.WhileStatement):
        self.visit_outside_statement(node.get_child(1))
        self.visit_outside_statement(node.get_child(0))

    # TODO - correct scoping (decl in body not usable in check or advance)
    def visitForStatement(self, node: AST.ForStatement):
        self.visit_outside_statement(node.get_child(0))
        self.visit_outside_statement(node.get_child(3))
        self.visit_outside_statement(node.get_child(1))
        self.visit_outside_statement(node.get_child(2))

    def visitPrintf(self, node: AST.Printf):
        if not self.has_IO:
            self.error(UndefinedError(node, "forgot to include stdio?"))
        self.visitChildren(node)

    def visitScanf(self, node: AST.Scanf):
        if not self.has_IO:
            self.error(UndefinedError(node, "forgot to include stdio?"))
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
        void_type = TypeClass([TypeComponents.VOID])
        self.returns_awaiting.append(True)
        self.visit_children_outside_statement(node)
        missing_return = self.returns_awaiting[len(self.returns_awaiting) - 1]
        self.returns_awaiting.pop()
        node.guarantied_return = self.last_scope_exited
        if missing_return:
            if not node.get_type() == void_type:
                self.warn(NoReturnWarning(node))
        else:
            if not node.get_type() == void_type and not self.last_scope_exited:
                self.warn(MayNotReturnWarning(node))

    def visitReturnStatement(self, node: AST.ReturnStatement):
        self.visitChildren(node)
        if node.get_enclosing(AST.FunctionDefinition) is None:
            self.error(IllegalStatementError(node, "no enclosing function definition"))
        self.returns_awaiting[len(self.returns_awaiting)-1] = False
        self.block_exited[len(self.block_exited)-1] = True

    def visitContinue(self, node: AST.Continue):
        if node.get_enclosing(AST.ForStatement) is None and node.get_enclosing(AST.WhileStatement) is None:
            self.error(IllegalStatementError(node, "no enclosing loop construct"))
        self.block_exited[len(self.block_exited)-1] = True

    def visitBreak(self, node: AST.Break):
        if node.get_enclosing(AST.ForStatement) is None \
                and node.get_enclosing(AST.WhileStatement) is None \
                and node.get_enclosing(AST.CaseBranch) is None \
                and node.get_enclosing(AST.DefaultBranch) is None:
            self.error(IllegalStatementError(node, "no enclosing switch branch or loop"))
        self.block_exited[len(self.block_exited)-1] = True
