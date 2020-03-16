from src.AST.Visitor import Visitor
from src.AST.AST import *
from src.utility.TypeClass import TypeClass, TypeComponents
from copy import deepcopy


class TypeListener:
    def update(self, node, node_type, child_types):
        try_type = type(node)
        while not hasattr(self, "update"+try_type.__name__):
            if try_type == Component:
                break
            try_type = type(super(try_type, node))
        else:
            return
        getattr(self, "update"+try_type.__name__)(node, node_type, child_types)


class TypeAssignVisitor (Visitor):
    def __init__(self):
        self.warnings = []
        self.observers = []

    def attach(self, listener: TypeListener):
        self.observers.append(listener)

    def detach(self, listener: TypeListener):
        self.observers.remove(listener)

    def notify(self, node, node_type, child_types):
        for observer in self.observers:
            observer.update(node, node_type, child_types)

    def implicit_conversion_warning(self, from_type: TypeClass, to_type: TypeClass):
        self.warnings.append("implicitly converting " + str(from_type) + " to " + str(to_type))

    def unary_propagate(self, node):
        child_type = self.visit(node.get_child(0))
        self.notify(node, child_type, [child_type])
        return child_type

    def visit(self, node) -> TypeClass:
        return Visitor.visit(self, node)

    def visitLeaf(self, node: Leaf):
        own_type = node.get_type()
        self.notify(node, [], own_type)
        return own_type

    def visitMathop(self, node: MathOp):
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
            self.implicit_conversion_warning(b_type, a_type)
            own_type = a_type
        elif a_type.converts_to(b_type) and not b_type.converts_to(a_type):
            self.implicit_conversion_warning(b_type, a_type)
            own_type = b_type
        self.notify(node, own_type, [a_type, b_type])
        return own_type

    def visitAssignOp(self, node):
        a_type = self.visit(node.get_child(0))
        b_type = self.visit(node.get_child(1))
        own_type = None
        if a_type == b_type:
            own_type = a_type
        elif b_type.promotes_to(a_type):
            own_type = a_type
        elif b_type.converts_to(a_type) and not a_type.converts_to(b_type):
            self.implicit_conversion_warning(b_type, a_type)
            own_type = a_type
        self.notify(node, own_type, [a_type, b_type])
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
        child_types = self.visitChildren(node)
        bool_type = TypeClass([TypeComponents.BOOL])
        all_promote = True
        all_convert = True
        warnings = []
        for child_type in child_types:
            if not child_type.promotes_to(bool_type):
                all_promote = False
            if not child_type.converts_to(bool_type):
                all_convert = False
            warnings.append(child_type)

        self.notify(node, bool_type, child_types)

        if all_promote:
            return bool_type
        if all_convert:
            for child_type in warnings:
                self.implicit_conversion_warning(child_type, bool_type)
            return bool_type

    def visitCompOp(self, node: CompOp):
        a_type = self.visit(node.get_child(0))
        b_type = self.visit(node.get_child(0))
        bool_type = TypeClass([TypeComponents.BOOL])

        self.notify(node, bool_type, [a_type, b_type])

        if a_type == b_type:
            return bool_type
        if b_type.promotes_to(a_type):
            return bool_type
        if a_type.promotes_to(b_type):
            return bool_type
        if b_type.converts_to(a_type) and not a_type.converts_to(b_type):
            self.implicit_conversion_warning(b_type, a_type)
            return bool_type
        if a_type.converts_to(b_type) and not b_type.converts_to(a_type):
            self.implicit_conversion_warning(b_type, a_type)
            return bool_type

    def visitAdress(self, node: Adress):
        child_type = self.visit(node.get_child(0))
        own_type = deepcopy(child_type).pushType(TypeComponents.PTR)
        self.notify(node, own_type, [child_type])
        return own_type

    def visitIndir(self, node: Indir):
        child_type = self.visit(node.get_child(0))
        own_type = None
        if child_type.is_ptr():
            own_type = deepcopy(child_type)
            own_type.popType()
        self.notify(node, own_type, [child_type])
        return own_type
