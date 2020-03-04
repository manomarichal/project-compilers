# Implemented according to the composite design pattern
# some of these classes are mostly just interfaces / use for type-checking if needed

# genericAccept() not for external use!


# Component
class Component:
    __parent = None
    __name = None

    def __init__(self, name=None):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getParent(self):
        return self.__parent

    def accept(self, visitor):
        return self.genericAccept(visitor, "Component", lambda x: None)

    def genericAccept(self, visitor, name, nextAttempt):
        if hasattr(visitor, "visit" + name):
            return getattr(visitor, "visit" + name)(self)
        else:
            return nextAttempt(visitor)


# Composites
class Composite(Component):
    __children = []

    def __init__(self, name=None, dummy=None):
        Component.__init__(self, name)

        if dummy is None:
            self.__children = []
        else:
            assert isinstance(dummy, Composite)
            self.swapChildren(dummy)

    def getChild(self, i: int):
        return self.__children[i]

    def getChildCount(self):
        return len(self.__children)

    def addChild(self, newChild: Component, i: int = None):
        if i is None:
            self.__children.append(newChild)
        else:
            self.__children.insert(i, newChild)

        newChild.__parent = self

    def swapChildren(self, other):
        assert isinstance(other, Composite)

        tmp = self.__children
        self.__children = other.__children
        other.__children = tmp

        other.__children = tmp

        for child in self.__children:
            child.__parent = self

            for child in other.__children:
                child.__parent = other

    def accept(self, visitor):
        return self.genericAccept(visitor, "Composite", super().accept)


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
        return self.genericAccept(visitor, "DummyNode", super().accept)


class Doc(Composite):
    def accept(self, visitor):
        return self.genericAccept(visitor, "Doc", super().accept)


class Operator(Composite):
    def accept(self, visitor):
        return self.genericAccept(visitor, "Operator", super().accept)


class Neg(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "Neg", super().accept)


class Pos(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "Pos", super().accept)


class Prod(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "Prod", super().accept)


class Div(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "Div", super().accept)


class Mod(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "Mod", super().accept)


class Sum(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "Sum", super().accept)


class Sub(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "Sub", super().accept)


class Not(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "Not", super().accept)


class And(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "And", super().accept)


class Or(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "Or", super().accept)


class Equal(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "Equal", super().accept)


class NotEqual(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "NotEqual", super().accept)


class Less(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "Less", super().accept)


class LessE(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "LessE", super().accept)


class More(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "More", super().accept)


class MoreE(Operator):
    def accept(self, visitor):
        return self.genericAccept(visitor, "MoreE", super().accept)


# Leaves
class Leaf(Component):
    def accept(self, visitor):
        return self.genericAccept(visitor, "Leaf", super().accept)


class Literal(Leaf):
    val = None

    def accept(self, visitor):
        return self.genericAccept(visitor, "Literal", super().accept)


class IntLit(Literal):
    def __init__(self, val: int = 0):
        self.val = val

    def accept(self, visitor):
        return self.genericAccept(visitor, "IntLit", super().accept)
