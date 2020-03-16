# Implemented according to the composite design pattern
# some of these classes are mostly just interfaces / use for type-checking if needed

# WARNING: single inheritance ONLY or visitors might break

from src.utility.SymbolTable import SymbolTable
from src.utility import TypeClass


# Component
class Component:
    _parent = None

    def get_parent(self):
        return self._parent

    def get_scope(self):
        if self.get_parent() is None:
            print("Ohnoes! No scope...")
            return None
        return self.get_parent().get_scope()

    def accept(self, visitor, *args):
        return self.generic_accept(visitor, "visit", *args)

    def generic_accept(self, visitor, prefix: str, *args):
        try_type = type(self)
        while not hasattr(visitor, prefix + try_type.__name__):
            if try_type == Component:
                break
            try_type = try_type.__bases__[0]
        else:
            return getattr(visitor, prefix + try_type.__name__)(self, *args)


# Composites
class Composite(Component):
    _children = []

    def __init__(self, dummy=None):
        Component.__init__(self)

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


class Scope(Composite):
    _symbol_table = None

    def get_scope(self):
        return self

    def get_symbol_table(self) -> SymbolTable:
        return self._symbol_table

    def set_symbol_table(self, table: SymbolTable):
        self._symbol_table = table

    def symbol_find(self, symbol):
        if symbol in self.get_symbol_table():
            return symbol
        if self.get_parent() is None:
            print("No scope containing \"" + symbol + "\" found when finding the symbol")
            return None
        return self.get_parent().get_scope().symbol_find(symbol)

    def symbol_remove(self, symbol):
        if symbol in self.get_symbol_table():
            self.get_symbol_table().pop(symbol)
        if self.get_parent() is None:
            print("No scope containing \"" + symbol + "\" found when removing the symbol")
            return None
        return self.get_parent().get_scope().symbol_remove(symbol)


class DummyNode(Composite):
    def __init__(self, children):
        Composite.__init__(self)

        if isinstance(children, list):
            for child in children:
                self.add_child(child)

        else:
            assert isinstance(children, Component)
            self.add_child(children)


class Doc(Scope):
    pass


class Expression(Composite):
    pass


# OPERATORS
class BinaryOp(Composite):
    pass


class UnaryOp(Composite):
    pass


class MathOp(BinaryOp):
    pass


class Neg(UnaryOp):
    pass


class IncrPost(UnaryOp):
    pass


class IncrPre(UnaryOp):
    pass


class DecrPost(UnaryOp):
    pass


class DecrPre(UnaryOp):
    pass


class Pos(UnaryOp):
    pass


class Indir(UnaryOp):
    pass


class Adress(UnaryOp):
    pass


class LogicOp(BinaryOp):
    pass


class CompOp(BinaryOp):
    pass


class Prod(MathOp):
    pass


class Div(MathOp):
    pass


class Mod(MathOp):
    pass


class Sum(MathOp):
    pass


class Sub(MathOp):
    pass


class Not(LogicOp):
    pass


class And(LogicOp):
    pass


class Or(LogicOp):
    pass


class Equal(CompOp):
    pass


class NotEqual(CompOp):
    pass


class Less(CompOp):
    pass


class LessE(CompOp):
    pass


class More(CompOp):
    pass


class MoreE(CompOp):
    pass


class AssignOp(BinaryOp):
    pass


# Leaves
class Leaf(Component):
    def get_type(self):
        pass


class Literal(Leaf):
    val = None
    type_obj = None

    def __init__(self, value=None):
        Leaf.__init__(self)
        self.val = value

    def get_type(self):
        return self.type_obj

    def set_type(self, type_obj):
        self.type_obj = type_obj

    def get_value(self):
        return self.val


class Variable(Leaf):
    _name: str

    def __init__(self, name):
        self._name = name

    def get_type(self):
        assert(self.get_name() is not None)
        return self.get_scope().get_symbol_table()[self.get_name()]

    def get_name(self):
        return self._name


class Decl(Variable):
    pass



