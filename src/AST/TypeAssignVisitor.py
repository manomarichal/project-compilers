from src.AST.Visitor import Visitor
from src.AST.AST import *
from src.utility.TypeClass import TypeClass, TypeComponents
from src.utility.SemanticExceptions import *
from copy import deepcopy


class TypeListener:
    def generic_enter(self, node: Component):
        return node.generic_accept(self, "enter")

    def generic_exit(self, node: Component, node_type: TypeClass, child_types: list):
        return node.generic_accept(self, "exit", node_type, child_types)

    def warn(self, warning):
        pass

    def error(self, warning):
        pass


class TypeAssignVisitor (Visitor):
    def __init__(self):
        self.observers = []

    def attach(self, listener: TypeListener):
        self.observers.append(listener)

    def detach(self, listener: TypeListener):
        self.observers.remove(listener)

    def notify_enter(self, node):
        for observer in self.observers:
            observer.generic_enter(node)

    def notify_exit(self, node, node_type, child_types):
        for observer in self.observers:
            observer.generic_exit(node, node_type, child_types)

    def warn(self, warning):
        for observer in self.observers:
            observer.warn(warning)

    def error(self, error):
        for observer in self.observers:
            observer.error(error)
        yield error

    def implicit_conversion_warning(self, node, from_type: TypeClass, to_type: TypeClass):
        self.warn(ImplicitConversionWarning(node, from_type, to_type))

    def no_conversion_error(self, node, a_type, b_type, bi_dir):
        self.warn(NoConversionError(node, a_type, b_type, bi_dir))

    def unary_propagate(self, node):
        self.notify_enter(node)
        child_type = self.visit(node.get_child(0))
        self.notify_exit(node, child_type, [child_type])
        return child_type

    def visit(self, node) -> TypeClass:
        return Visitor.visit(self, node)

    def visitDoc(self, node: Doc):
        for child_nr in range(node.get_child_count()):
            child = node.get_child(child_nr)
            try:
                self.visit(child)
            except StatementException:
                continue

    def visitLeaf(self, node: Leaf):
        self.notify_enter(node)
        own_type = node.get_type()
        self.notify_exit(node, [], own_type)
        return own_type

    def visitMathop(self, node: MathOp):
        self.notify_enter(node)
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
        self.notify_exit(node, own_type, [a_type, b_type])
        return own_type

    def visitAssignOp(self, node):
        self.notify_enter(node)
        a_type = self.visit(node.get_child(0))
        b_type = self.visit(node.get_child(1))
        own_type = None
        if a_type == b_type:
            own_type = a_type
        elif b_type.promotes_to(a_type):
            own_type = a_type
        elif b_type.converts_to(a_type) and not a_type.converts_to(b_type):
            self.implicit_conversion_warning(node, b_type, a_type)
            own_type = a_type
        else:
            self.no_conversion_error(node, a_type, b_type, True)
        self.notify_exit(node, own_type, [a_type, b_type])
        return own_type

    def visitPos(self, node):
        return self.unary_propagate(node)

    def visitNeg(self, node):
        return self.unary_propagate(node)

    def visitIncrPre(self, node):
        return self.unary_propagate(node)

    def visitIncrPost(self, node):
        return self.unary_propagate(node)

    def visitDecrPre(self, node):
        return self.unary_propagate(node)

    def visitDecrPost(self, node):
        return self.unary_propagate(node)

    def visitLogicOp(self, node: LogicOp):
        self.notify_enter(node)
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

        self.notify_exit(node, bool_type, child_types)
        return bool_type

    def visitCompOp(self, node: CompOp):
        self.notify_enter(node)
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

        self.notify_exit(node, bool_type, [a_type, b_type])
        return bool_type

    def visitAdress(self, node: Adress):
        self.notify_enter(node)
        child_type = self.visit(node.get_child(0))
        own_type = deepcopy(child_type).pushType(TypeComponents.PTR)
        self.notify_exit(node, own_type, [child_type])
        return own_type

    def visitIndir(self, node: Indir):
        self.notify_enter(node)
        child_type = self.visit(node.get_child(0))
        own_type = None
        if child_type.is_ptr():
            own_type = deepcopy(child_type)
            own_type.popType()
        else:
            self.error(InvalidTypeError(node, child_type))
        self.notify_exit(node, own_type, [child_type])
        return own_type
