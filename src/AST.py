# Implemented according to the composite design pattern
# some of these classes are mostly just interfaces / use for type-checking if needed


# Component
class Component:
    __parent: None
    __name: None

    def accept(self, visitor):
        visitName = "visit" + type(self).__name__
        if hasattr(visitor, visitName):
            return getattr(visitor, visitName)(self)
        else:
            return visitor.visitChildren(self)

    def getName(self):
        return self.__name

    def getParent(self):
        return self.__parent


# Composites
class Composite(Component):
    __children: list

    def __init__(self, children: list = None):
        if children is None:
            self.children = []
        else:
            self.children = children

    def getChild(self, i: int):
        return self.children[i]

    def getChildCount(self):
        return len(self.children)

    def addChild(self, newChild: Component, i: int = None):
        if i is None:
            self.__children.append(newChild)
        else:
            self.__children.insert(i, newChild)

        newChild.__parent = self

    def swapChildren(self, other):
        assert isinstance(other, Composite)

tmp = self.__children
        self.children = other.__childrenn = tmp

        other.children = tmp

for child in self.__children:
            child.__parent = self

        for child in other.__children:
            child.__parent = other

class DummyNode(Composite):
    pass


class Doc(Composite):
    pass


class Operator(Composite):
    pass


class Neg(Operator):
    pass


class Pos(Operator):
    pass


class Prod(Operator):
    pass


class Div(Operator):
    pass


class Mod(Operator):
    pass


class Sum(Operator):
    pass


class Sub(Operator):
    pass


class Not(Operator):
    pass


class And(Operator):
    pass


class Or(Operator):
    pass


class Equal(Operator):
    pass


class NotEqual(Operator):
    pass


class Less (Operator):
    pass


class LessE (Operator):
    pass


class More (Operator):
    pass


class MoreE (Operator):
    pass

# Leaves
class Leaf(Component):
    pass


class Literal(Leaf):
    val = None


class IntLit(Literal):
    def __init__(self, val: int = 0):
        self.val = val
