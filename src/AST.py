# Implemented according to the composite design pattern
# some of these classes are mostly just interfaces / use for type-checking if needed


# Component
class Component:
    __parent: None
    __name: None

    def __init__(self, name=None):
        self.__name = name

    def accept(self, visitor):
        visitName = "visit" + type(self).__name__
        if hasattr(visitor, visitName):
            return getattr(visitor, visitName)(self)
        else:
            return visitor.visitChildren(self)

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getParent(self):
        return self.__parent


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


class DummyNode(Composite):
    def __init__(self, children):
        Composite.__init__(self)

        if isinstance(children, list):
            for child in children:
                self.addChild(child)

        else:
            assert isinstance(children, Component)
            self.addChild(children)


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
