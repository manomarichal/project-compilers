# Implemented according to the composite design pattern
# some of these classes are mostly just interfaces / use for type-checking if needed

from src.TypeClass import TypeClass


# Component
class Component:
    _parent = None
    _name = None
    type_obj = None

    def __init__(self, name=None):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_parent(self):
        return self._parent

    def accept(self, visitor):
        return self._generic_accept(visitor, "Component", lambda x: None)

    def _generic_accept(self, visitor, name, next_attempt):
        if hasattr(visitor, "visit" + name):
            return getattr(visitor, "visit" + name)(self)
        else:
            return next_attempt(visitor)


# Composites
class Composite(Component):
    _children = []

    def __init__(self, name=None, dummy=None):
        Component.__init__(self, name)

        if dummy is None:
            self._children = []
        else:
            assert isinstance(dummy, Composite)
            self.swap_children(dummy)

    def get_child(self, i: int):
        return self._children[i]

    def replace_child(self, old_child: Component, new_child: Component):
        self._children[self._children.index(old_child)] = new_child

    def get_child_count(self):
        return len(self._children)

    def add_child(self, new_child: Component, i: int = None):
        if i is None:
            self._children.append(new_child)
        else:
            self._children.insert(i, new_child)

        new_child._parent = self

    def swap_children(self, other):
        assert isinstance(other, Composite)

        tmp = self._children
        self._children = other._children
        other._children = tmp

        other._children = tmp

        for child in self._children:
            child._parent = self

            for child in other._children:
                child._parent = other

    def accept(self, visitor):
        return self._generic_accept(visitor, "Composite", super().accept)


class DummyNode(Composite):
    def __init__(self, children):
        Composite.__init__(self)

        if isinstance(children, list):
            for child in children:
                self.add_child(child)

        else:
            assert isinstance(children, Component)
            self.add_child(children)

    def accept(self, visitor):
        return self._generic_accept(visitor, "DummyNode", super().accept)


class Doc(Composite):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Doc", super().accept)


class Expression(Composite):
    def get_type(self):
        return self.type_obj

    def accept(self, visitor):
        return self._generic_accept(visitor, "Literal", super().accept)


# OPERATORS
class BinaryOp(Composite):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Operator", super().accept)


class UnaryOp(Composite):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Operator", super().accept)


class MathOp(BinaryOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Operator", super().accept)


class Neg(UnaryOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Neg", super().accept)


class IncrPost(UnaryOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Neg", super().accept)


class IncrPre(UnaryOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Neg", super().accept)


class DecrPost(UnaryOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Neg", super().accept)


class DecrPre(UnaryOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Neg", super().accept)


class Pos(UnaryOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Pos", super().accept)


class LogicOp(BinaryOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Operator", super().accept)


class CompOp(BinaryOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Operator", super().accept)


class Prod(MathOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Prod", super().accept)


class Div(MathOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Div", super().accept)


class Mod(MathOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Mod", super().accept)


class Sum(MathOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Sum", super().accept)


class Sub(MathOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Sub", super().accept)


class Not(LogicOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Not", super().accept)


class And(LogicOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "And", super().accept)


class Or(LogicOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Or", super().accept)


class Equal(CompOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Equal", super().accept)


class NotEqual(CompOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "NotEqual", super().accept)


class Less(CompOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Less", super().accept)


class LessE(CompOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "LessE", super().accept)


class More(CompOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "More", super().accept)


class MoreE(CompOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "MoreE", super().accept)


class AssignOp(BinaryOp):
    def accept(self, visitor):
        return self._generic_accept(visitor, "AssignOp", super().accept)


# Leaves
class Leaf(Component):
    def accept(self, visitor):
        return self._generic_accept(visitor, "Leaf", super().accept)


class Literal(Leaf):
    val = None

    def get_value(self):
        return self.val

    def accept(self, visitor):
        return self._generic_accept(visitor, "Literal", super().accept)


class Variable(Leaf):
    def get_type(self):
        return self.type_obj

    def accept(self, visitor):
        return self._generic_accept(visitor, "Variable", super().accept)


class IntLit(Literal):
    def __init__(self, val: int = 0):
        self.val = val

    def accept(self, visitor):
        return self._generic_accept(visitor, "IntLit", super().accept)
