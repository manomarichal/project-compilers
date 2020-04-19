from src.utility.SemanticExceptions import *
from src.AST.AST import *
from src.AST.Visitor import Visitor
from src.utility.TypeClass import TypeClass, TypeComponents
from src.utility import SymbolTable
from copy import deepcopy


class TypeVisitor (Visitor):
    def __init__(self):
        self.warnings = []
        self.errors = []

    def add_warning(self, warning):
        self.warnings.append(warning)

    def add_error(self, error):
        self.errors.append(error)
        raise error

    def implicit_conversion_warning(self, node, from_type: TypeClass, to_type: TypeClass):
        if from_type == TypeClass([TypeComponents.INT]) and to_type == TypeClass([TypeComponents.BOOL]):
            return
        self.add_warning(ImplicitConversionWarning(node, from_type, to_type))

    def no_conversion_error(self, node, a_type, b_type, bi_dir):
        self.add_error(NoConversionError(node, a_type, b_type, bi_dir))

    def insert_conversion(self, node: Composite, child_nr: int, to_type: TypeClass, warn: bool = False):
        old_child = node.get_child(child_nr)
        conversion = CastOp(to_type)
        node.replace_child(old_child, conversion)
        conversion.add_child(old_child)
        if warn:
            self.implicit_conversion_warning(node, old_child.get_type(), to_type)

    def assume_mono_conversion(self, node: Composite, child_nr: int, supposed_type: TypeClass):
        given_type: TypeClass = node.get_child(child_nr).get_type()
        if given_type == supposed_type:
            pass
        elif given_type.promotes_to(supposed_type):
            self.insert_conversion(node, child_nr, supposed_type)
        elif given_type.converts_to(supposed_type):
            self.insert_conversion(node, child_nr, supposed_type, True)
        else:
            self.no_conversion_error(node, given_type, supposed_type, False)
        return supposed_type

    # TODO: warn / error amibiguous conversions
    def assume_bi_conversion(self, node: Composite, child_nr_a: int, child_nr_b: int):
        a_type: TypeClass = node.get_child(child_nr_a).get_type()
        b_type: TypeClass = node.get_child(child_nr_b).get_type()
        if a_type == b_type:
            return a_type
        elif b_type.promotes_to(a_type):
            self.insert_conversion(node, child_nr_b, a_type)
            return a_type
        elif a_type.promotes_to(b_type):
            self.insert_conversion(node, child_nr_a, b_type)
            return b_type
        elif b_type.converts_to(a_type):
            self.insert_conversion(node, child_nr_b, a_type, True)
            return a_type
        elif a_type.converts_to(b_type):
            self.insert_conversion(node, child_nr_a, b_type, True)
            return b_type
        else:
            self.no_conversion_error(node, a_type, b_type, True)

    def visit_outside_statement(self, node):
        try:
            return self.visit(node)
        except StatementException:
            pass

    def visit_children_outside_statement(self, node):
        for child_nr in range(node.get_child_count()):
            self.visit_outside_statement(node.get_child(child_nr))

    def visit(self, node: Component) -> TypeClass:
        return Visitor.visit(self, node)

    def visitComposite(self, node: Composite):
        result = self.visitChildren(node)
        if result is None:
            return None
        if len(result) == 0:
            return None
        if len(result) == 1:
            node.set_type(result[0])
            return result[0]
        return result

    def visitScope(self, node):
        self.visit_children_outside_statement(node)

    def visitDoc(self, node: Doc):
        self.visit_children_outside_statement(node)

    def visitLeaf(self, node: Leaf):
        own_type = node.get_type()
        node.set_type(own_type)
        return own_type

    def visitMathOp(self, node: MathOp):
        self.visitChildren(node)
        own_type = self.assume_bi_conversion(node, 0, 1)
        node.set_type(own_type)
        return own_type

    def visitAssignOp(self, node):
        child_types = self.visitChildren(node)
        own_type = self.assume_mono_conversion(node, 1, child_types[0])
        node.set_type(own_type)
        return own_type

    def visitLogicOp(self, node: LogicOp):
        self.visitChildren(node)
        bool_type = TypeClass([TypeComponents.BOOL])
        for child_nr in range(node.get_child_count()):
            self.assume_mono_conversion(node, child_nr, bool_type)
        node.set_type(bool_type)
        return bool_type

    def visitCompOp(self, node: CompOp):
        self.visitChildren(node)
        bool_type = TypeClass([TypeComponents.BOOL])
        self.assume_bi_conversion(node, 0, 1)
        node.set_type(bool_type)
        return bool_type

    def visitAdress(self, node: Adress):
        child_type = self.visit(node.get_child(0))
        own_type = deepcopy(child_type)
        own_type.pushType(TypeComponents.PTR)
        node.set_type(own_type)
        return own_type

    def visitIndir(self, node: Indir):
        child_type = self.visit(node.get_child(0))
        own_type = None
        if child_type.is_ptr():
            own_type = deepcopy(child_type)
            own_type.popType()
        else:
            self.add_error(InvalidTypeError(node, child_type))
        node.set_type(own_type)
        return own_type

    def visitIndex(self, node: Index):
        child_types = self.visitChildren(node)
        own_type = None
        self.assume_mono_conversion(node, 1, TypeClass([TypeComponents.INT]))
        if child_types[0].is_array():
            own_type = deepcopy(child_types[0])
            own_type.popType()
        else:
            self.add_error(InvalidTypeError(node, child_types[0], "can only index arrays"))
        node.set_type(own_type)
        return own_type

    def visitIfStatement(self, node: IfStatement):
        self.visit_children_outside_statement(node)
        bool_type = TypeClass([TypeComponents.BOOL])
        self.assume_mono_conversion(node, 0, bool_type)
        return None

    def visitForStatement(self, node: ForStatement):
        self.visit_children_outside_statement(node)
        bool_type = TypeClass([TypeComponents.BOOL])
        self.assume_mono_conversion(node, 1, bool_type)
        return None

    def visitWhileStatement(self, node: WhileStatement):
        self.visit_children_outside_statement(node)
        bool_type = TypeClass([TypeComponents.BOOL])
        self.assume_mono_conversion(node, 0, bool_type)

    def visitSwitchStatement(self, node: SwitchStatement):
        self.visit_children_outside_statement(node)
        int_type = TypeClass([TypeComponents.INT])
        self.assume_mono_conversion(node, 0, int_type)

    def visitCaseBranch(self, node: CaseBranch):
        self.visit_children_outside_statement(node)
        int_type = TypeClass([TypeComponents.INT])
        self.assume_mono_conversion(node, 0, int_type)

    def visitFunctionDefinition(self, node: FunctionDefinition):
        self.visit_children_outside_statement(node)
        own_type = node.get_type()
        node.set_type(own_type)
        return own_type

    def visitFunctionCall(self, node: FunctionCall):
        self.visitChildren(node)
        own_entry: SymbolTable.FuncEntry = node.get_scope().symbol_find(node.get_name())
        own_type = own_entry.type_obj
        for argNr in range(node.get_child_count()):
            supposed_type: TypeClass = own_entry.arg_types[argNr]
            self.assume_mono_conversion(node, argNr, supposed_type)

        node.set_type(own_type)
        return own_type

    def visitReturnStatement(self, node: ReturnStatement):
        self.visitChildren(node)
        function_type = node.get_enclosing(FunctionDefinition).get_type()
        self.assume_mono_conversion(node, 0, function_type)
        node.set_type(function_type)
        return function_type
