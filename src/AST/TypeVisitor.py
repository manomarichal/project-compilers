from src.utility.SemanticExceptions import *
from src.AST.AST import *
from src.AST.Visitor import Visitor
from src.utility.TypeClass import TypeClass, TypeComponents
from copy import deepcopy


class TypeVisitor (Visitor):
    def __init__(self):
        self.warnings = []
        self.errors = []

    def warn(self, warning):
        self.warnings.append(warning)

    def error(self, error):
        self.errors.append(error)
        yield error

    def implicit_conversion_warning(self, node, from_type: TypeClass, to_type: TypeClass):
        self.warn(ImplicitConversionWarning(node, from_type, to_type))

    def no_conversion_error(self, node, a_type, b_type, bi_dir):
        self.warn(NoConversionError(node, a_type, b_type, bi_dir))

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
        elif a_type.promotes_to(b_type):
            own_type = b_type
        elif b_type.converts_to(a_type) and not a_type.converts_to(b_type):
            self.implicit_conversion_warning(node, b_type, a_type)
            own_type = a_type
        elif a_type.converts_to(b_type) and not b_type.converts_to(a_type):
            self.implicit_conversion_warning(node, b_type, a_type)
            own_type = b_type
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
        elif b_type.converts_to(a_type):
            self.implicit_conversion_warning(node, b_type, a_type)
            own_type = a_type
        else:
            self.no_conversion_error(node, a_type, b_type, True)
        node.set_type(own_type)
        return own_type

    def visitLogicOp(self, node: LogicOp):
        child_types = self.visitChildren(node)
        bool_type = TypeClass([TypeComponents.BOOL])

        all_promote = True
        all_convert = True
        warnings = []
        errors = []
        for child_type in child_types:
            if not child_type.promotes_to(bool_type):
                all_promote = False
            elif not child_type.converts_to(bool_type):
                all_convert = False
                warnings.append(child_type)
            else:
                errors.append(child_type)

        if all_promote:
            pass
        else:
            for child_type in warnings:
                self.implicit_conversion_warning(node, child_type, bool_type)
            if not all_convert:
                for child_type in errors:
                    self.no_conversion_error(node, child_type, bool_type, False)

        node.set_type(bool_type)
        return bool_type

    def visitCompOp(self, node: CompOp):
        a_type = self.visit(node.get_child(0))
        b_type = self.visit(node.get_child(0))
        bool_type = TypeClass([TypeComponents.BOOL])

        if a_type == b_type:
            pass
        elif b_type.promotes_to(a_type):
            pass
        elif a_type.promotes_to(b_type):
            pass
        elif b_type.converts_to(a_type) and not a_type.converts_to(b_type):
            self.implicit_conversion_warning(node, b_type, a_type)
        elif a_type.converts_to(b_type) and not b_type.converts_to(a_type):
            self.implicit_conversion_warning(node, b_type, a_type)
        else:
            self.no_conversion_error(node, a_type, b_type, True)

        node.set_type(bool_type)
        return bool_type

    def visitAdress(self, node: Adress):
        child_type = self.visit(node.get_child(0))
        own_type = deepcopy(child_type).pushType(TypeComponents.PTR)
        node.set_type(own_type)
        return own_type

    def visitIndir(self, node: Indir):
        child_type = self.visit(node.get_child(0))
        own_type = None
        if child_type.is_ptr():
            own_type = deepcopy(child_type)
            own_type.popType()
        else:
            self.error(InvalidTypeError(node, child_type))
        node.set_type(own_type)
        return own_type
