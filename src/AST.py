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


class Operator(Composite):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Operator", super().accept)


class Neg(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Neg", super().accept)


class Pos(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Pos", super().accept)


class Prod(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Prod", super().accept)


class Div(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Div", super().accept)


class Mod(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Mod", super().accept)


class Sum(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Sum", super().accept)


class Sub(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Sub", super().accept)


class Not(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Not", super().accept)


class And(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "And", super().accept)


class Or(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Or", super().accept)


class Equal(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Equal", super().accept)


class NotEqual(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "NotEqual", super().accept)


class Less(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Less", super().accept)


class LessE(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "LessE", super().accept)


class More(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "More", super().accept)


class MoreE(Operator):
    def accept(self, visitor):
        return self._genericAccept(visitor, "MoreE", super().accept)


# Leaves
class Leaf(Component):
    def accept(self, visitor):
        return self._genericAccept(visitor, "Leaf", super().accept)


class Literal(Leaf):
    val = None

    def accept(self, visitor):
        return self._genericAccept(visitor, "Literal", super().accept)


class IntLit(Literal):
    def __init__(self, val: int = 0):
        self.val = val

    def accept(self, visitor):
        return self._genericAccept(visitor, "IntLit", super().accept)
