from src.AST.Visitor import Visitor
from src.AST.AST import *
from src.utility.TypeClass import TypeClass, TypeComponents
from copy import deepcopy


class TypeAssignVisitor (Visitor):
    def __init__(self):
        self.warnings = []

    def implicit_conversion_warning(self, from_type: TypeClass, to_type: TypeClass):
        self.warnings.append("implicitly converting " + str(from_type) + " to " + str(to_type))

    def unary_propagate(self, node):
        return self.visit(node.get_child(0))

    def visit(self, node) -> TypeClass:
        return Visitor.visit(self, node)

    def visitLeaf(self, node: Leaf):
        return node.get_type()

    def visitMathop(self, node: MathOp):
        a_type = self.visit(node.get_child(0))
        b_type = self.visit(node.get_child(1))
        if a_type == b_type:
            return a_type
        if b_type.promotes_to(a_type):
            return a_type
        if a_type.promotes_to(b_type):
            return b_type
        if b_type.converts_to(a_type) and not a_type.converts_to(b_type):
            self.implicit_conversion_warning(b_type, a_type)
            return a_type
        if a_type.converts_to(b_type) and not b_type.converts_to(a_type):
            self.implicit_conversion_warning(b_type, a_type)
            return b_type

    def visitAssignOp(self, node):
        a_type = self.visit(node.get_child(0))
        b_type = self.visit(node.get_child(1))
        if a_type == b_type:
            return a_type
        if b_type.promotes_to(a_type):
            return a_type
        if b_type.converts_to(a_type) and not a_type.converts_to(b_type):
            self.implicit_conversion_warning(b_type, a_type)
            return a_type

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
        return deepcopy(self.visit(node.get_child(0))).pushType(TypeComponents.PTR)

    def visitIndir(self, node: Indir):
        child_type = deepcopy(self.visit(node.get_child(0)))
        if child_type.is_ptr():
            child_type.popType()
            return child_type
