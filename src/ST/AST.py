# Implemented according to the composite design pattern
# some of these classes are mostly just interfaces / use for type-checking if needed

# _genericAccept() not for external use!


# Component
class Component:
    _parent = None
    _name = None

    def __init__(self, name=None):
        self._name = name

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getParent(self):
        return self._parent

    def accept(self, visitor):
        return self._genericAccept(visitor, "Component", lambda x: None)

    def _genericAccept(self, visitor, name, nextAttempt):
        if hasattr(visitor, "visit" + name):
            return getattr(visitor, "visit" + name)(self)
        else:
            return nextAttempt(visitor)


# Composites
class Composite(Component):
    _children = []

    def __init__(self, name=None, dummy=None):
        Component.__init__(self, name)

        if dummy is None:
            self._children = []
        else:
            assert isinstance(dummy, Composite)
            self.swapChildren(dummy)

    def getChild(self, i: int):
        return self._children[i]

    def replaceChild(self, oldChild: Component, newChild: Component):
        self._children[self._children.index(oldChild)] = newChild

    def getChildCount(self):
        return len(self._children)

    def addChild(self, newChild: Component, i: int = None):
        if i is None:
            self._children.append(newChild)
        else:
            self._children.insert(i, newChild)

        newChild._parent = self

    def swapChildren(self, other):
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
        return self._genericAccept(visitor, "Composite", super().accept)


class DummyNode(Composite):
    def __init__(self, children):
        Composite.__init__(self)

        if isinstance(children, list):
            for child in children:
                self.addChild(child)

        else:
            assert isinstance(children, Component)
            self.addChild(children)

    def accept(self, visitor):
        return self._genericAccept(visitor, "DummyNode", super().accept)


class Doc(Composite):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Doc", super().accept)


class BinaryOp(Composite):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Operator", super().accept)


class UnaryOp(Composite):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Operator", super().accept)


class MathOp(BinaryOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Operator", super().accept)


class LogicOp(BinaryOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Operator", super().accept)


class CompOp(BinaryOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Operator", super().accept)


class Neg(UnaryOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Neg", super().accept)


class Pos(UnaryOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Pos", super().accept)


class Prod(MathOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Prod", super().accept)


class Div(MathOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Div", super().accept)


class Mod(MathOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Mod", super().accept)


class Sum(MathOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Sum", super().accept)


class Sub(MathOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Sub", super().accept)


class Not(LogicOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Not", super().accept)


class And(LogicOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "And", super().accept)


class Or(LogicOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Or", super().accept)


class Equal(CompOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Equal", super().accept)


class NotEqual(CompOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "NotEqual", super().accept)


class Less(CompOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Less", super().accept)


class LessE(CompOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "LessE", super().accept)


class More(CompOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "More", super().accept)


class MoreE(CompOp):
    def accept(self, visitor):
        return self._genericAccept(visitor, "MoreE", super().accept)


# Leaves
class Leaf(Component):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Leaf", super().accept)


class Literal(Leaf):
    val = None

    def getValue(self):
        return self.val

    def accept(self, visitor):
        return self._genericAccept(visitor, "Literal", super().accept)


class BoolLit(Literal):
    def __init__(self, val: int = 0):
        self.val = val

    def accept(self, visitor):
        return self._genericAccept(visitor, "IntLit", super().accept)


class IntLit(Literal):
    def __init__(self, val: int = 0):
        self.val = val

    def accept(self, visitor):
        return self._genericAccept(visitor, "IntLit", super().accept)
