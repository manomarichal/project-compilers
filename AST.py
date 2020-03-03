# Implemented according to the composite design pattern
# some of these classes are mostly just interfaces / use for type-checking if needed


# Component
class Component:
    children = None


# Composites
class Composite(Component):
    def __init__(self, children: list = None):
        if children is None:
            self.children = []
        else:
            self.children = children


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
