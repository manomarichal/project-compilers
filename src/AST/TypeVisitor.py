from src.utility.SemanticExceptions import *
from src.AST.AST import *
from src.AST.Visitor import Visitor
from src.utility.TypeClass import TypeClass, TypeComponents
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

    def visit(self, node) -> TypeClass:
        return Visitor.visit(self, node)

    def visitComposite(self, node: Composite):
        result = self.visitChildren(node)
        if len(result) == 0:
            return None
        if len(result) == 1:
            node.set_type(result[0])
            return result[0]
        return result

    def visit_outside_statement(self, node):
        try:
            return self.visit(node)
        except StatementException:
            pass

    def visitDoc(self, node: Doc):
        for child_nr in range(node.get_child_count()):
            self.visit_outside_statement(node.get_child(child_nr))

    def visitLeaf(self, node: Leaf):
        own_type = node.get_type()
        node.set_type(own_type)
        return own_type

    def visitMathOp(self, node: MathOp):
        a_type = self.visit(node.get_child(0))
        b_type = self.visit(node.get_child(1))
        own_type = None

        if a_type == b_type:
            own_type = a_type
        elif b_type.promotes_to(a_type):
            own_type = a_type
            self.insert_conversion(node, 1, own_type)
        elif a_type.promotes_to(b_type):
            own_type = b_type
            self.insert_conversion(node, 0, own_type)
        elif b_type.converts_to(a_type) and not a_type.converts_to(b_type):
            own_type = a_type
            self.insert_conversion(node, 1, own_type, True)
        elif a_type.converts_to(b_type) and not b_type.converts_to(a_type):
            own_type = b_type
            self.insert_conversion(node, 0, own_type, True)
        else:
            self.no_conversion_error(node, a_type, b_type, True)
        node.set_type(own_type)
        return own_type

    def visitAssignOp(self, node):
        a_type = self.visit(node.get_child(0))
        b_type = self.visit(node.get_child(1))
        own_type = None
        if a_type == b_type:
            own_type = a_type
        elif b_type.promotes_to(a_type):
            own_type = a_type
            self.insert_conversion(node, 1, own_type, False)
        elif b_type.converts_to(a_type):
            own_type = a_type
            self.insert_conversion(node, 1, own_type, True)
        else:
            self.no_conversion_error(node, a_type, b_type, True)
        node.set_type(own_type)
        return own_type

    def visitLogicOp(self, node: LogicOp):
        child_types = self.visitChildren(node)
        bool_type = TypeClass([TypeComponents.BOOL])

        index = -1
        for child_type in child_types:
            index += 1
            if child_type == bool_type:
                continue
            if child_type.promotes_to(bool_type):
                self.insert_conversion(node, index, bool_type)
                continue
            if child_type.converts_to(bool_type):
                self.insert_conversion(node, index, bool_type, True)
                continue
            self.no_conversion_error(node, child_type, bool_type, False)

        node.set_type(bool_type)
        return bool_type

    def visitCompOp(self, node: CompOp):
        a_type = self.visit(node.get_child(0))
        b_type = self.visit(node.get_child(1))
        bool_type = TypeClass([TypeComponents.BOOL])

        if a_type == b_type:
            pass
        elif b_type.promotes_to(a_type):
            self.insert_conversion(node, 1, a_type)
        elif a_type.promotes_to(b_type):
            self.insert_conversion(node, 0, b_type)
        elif b_type.converts_to(a_type) and not a_type.converts_to(b_type):
            self.insert_conversion(node, 1, a_type, True)
        elif a_type.converts_to(b_type) and not b_type.converts_to(a_type):
            self.insert_conversion(node, 0, a_type, True)
        else:
            self.no_conversion_error(node, a_type, b_type, True)

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
