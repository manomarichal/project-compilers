# Implemented according to the composite design pattern
# some of these classes are mostly just interfaces / use for type-checking if needed

# WARNING: single inheritance ONLY or visitors might break

# TODO: add type to each node
# TODO: add type conversion nodes

from src.utility.SymbolTable import SymbolTable
from src.utility import TypeClass
from enum import Enum


# Component
class Component:
    _parent = None
    _register = None
    _ir_rep = None
    _type: TypeClass = None
    _source_loc = None

    def get_source_loc(self):
        return self._source_loc

    def set_source_loc(self, loc):
        self._source_loc = loc

    def is_lval(self):
        return False

    def get_ir_rep(self):
        return self._ir_rep

    def set_ir_rep(self, ir_rep):
        self._ir_rep = ir_rep

    def get_type(self) -> TypeClass:
        return self._type

    def set_type(self, new_type: TypeClass):
        self._type = new_type

    def get_register(self):
        return self._register

    def set_register(self, register):
        self._register = register

    def get_parent(self):
        return self._parent

    def get_scope(self):
        if self.get_parent() is None:
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

        self._register = ''

        if dummy is None:
            self._children = []
        else:
            assert isinstance(dummy, Composite)
            self.swap_children(dummy)

    def get_child(self, i: int)->Component:
        return self._children[i]

    def replace_child(self, old_child: Component, new_child: Component):
        index = self._children.index(old_child)
        self._children[index] = new_child
        self._children[index]._parent = self

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

    def set_positional_child(self, index: int, child: Component):
        while len(self._children) < index+1:
            self._children.append(None)
        self._children[index] = child
        child._parent = self

    def add_positional_child(self, index: int, child: Component):
        while len(self._children) < index:
            self._children.append(None)
        self._children.append(child)
        child._parent = self


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
            return self.get_symbol_table()[symbol]
        if self.get_parent() is None:
            return None
        return self.get_parent().get_scope().symbol_find(symbol)

    def symbol_remove(self, symbol):
        if symbol in self.get_symbol_table():
            self.get_symbol_table().pop(symbol)
        if self.get_parent() is None:
            return None
        return self.get_parent().get_scope().symbol_remove(symbol)


# if, for, while are scopes themselves for vars declared in their conditions
class IfStatement (Scope):  # child 0 is condition, 1 is then, (2 is else)
    def set_condition(self, condition):
        self.set_positional_child(0, condition)

    def set_then(self, effect):
        self.set_positional_child(1, effect)

    def set_else(self, effect):
        self.set_positional_child(2, effect)


# TODO: maybe simplify AST represtentation of switch/case/default (but then it's less uniform)
class SwitchStatement (Scope):  # 0=cond >1=branch(incl. default)
    def set_condition(self, condition):
        self.set_positional_child(0, condition)

    def add_branch(self, branch):
        self.add_positional_child(1, branch)


class CaseBranch (Composite):  # 0=cst >1=code
    def set_constant(self, constant):
        self.set_positional_child(0, constant)

    def add_effect(self, effect):
        self.add_positional_child(1, effect)


class DefaultBranch (Composite):  # >0=code # only here for consistency w/ specific case
    def add_effect(self, effect):
        self.add_positional_child(0, effect)


# for loops could also be translated to while loops in the ast if desired
class ForStatement (Scope):
    def set_init(self, init):
        self.set_positional_child(0, init)

    def set_check(self, check):
        self.set_positional_child(1, check)

    def set_advance(self, advance):
        self.set_positional_child(2, advance)

    def set_contents(self, content):
        self.set_positional_child(3, content)


class WhileStatement (Scope):
    def set_check(self, check):
        self.set_positional_child(0, check)

    def set_contents(self, content):
        self.set_positional_child(1, content)


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


class Decl(Composite):
    def is_lval(self):
        return True


class Printf(Composite):
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
    def is_lval(self):
        return True


class Adress(UnaryOp):
    pass


# cast from get_child(0).get_type() to get_type()
class conv_type(Enum):
    #TODO automatiseren
    BOOL_TO_INT = 1
    BOOL_TO_FLOAT = 2
    INT_TO_BOOL = 3
    INT_TO_FLOAT = 4
    FLOAT_TO_INT = 5
    FLOAT_TO_BOOL = 6
    FLOAT_TO_CHAR = 7
    INT_TO_CHAR = 8
    BOOL_TO_CHAR = 9
    CHAR_TO_BOOL = 10
    CHAR_TO_FLOAT = 11
    CHAR_TO_INT = 12

class CastOp(UnaryOp):
    def __init__(self, to_type, dummy=None):
        super().__init__(dummy)
        self.set_type(to_type)

    def get_conversion_type(self) -> conv_type:
        if self.get_child(0).get_type().__repr__() == 'bool' and self.get_type().__repr__() == 'int':
            return conv_type.BOOL_TO_INT
        if self.get_child(0).get_type().__repr__() == 'bool' and self.get_type().__repr__() == 'float':
            return conv_type.BOOL_TO_FLOAT
        elif self.get_child(0).get_type().__repr__() == 'int' and self.get_type().__repr__() == 'bool':
            return conv_type.INT_TO_BOOL
        elif self.get_child(0).get_type().__repr__() == 'int' and self.get_type().__repr__() == 'float':
            return conv_type.INT_TO_FLOAT
        elif self.get_child(0).get_type().__repr__() == 'float' and self.get_type().__repr__() == 'int':
            return conv_type.FLOAT_TO_INT
        elif self.get_child(0).get_type().__repr__() == 'float' and self.get_type().__repr__() == 'bool':
            return conv_type.FLOAT_TO_BOOL
        elif self.get_child(0).get_type().__repr__() == 'float' and self.get_type().__repr__() == 'char':
            return conv_type.FLOAT_TO_CHAR
        elif self.get_child(0).get_type().__repr__() == 'int' and self.get_type().__repr__() == 'char':
            return conv_type.INT_TO_CHAR
        elif self.get_child(0).get_type().__repr__() == 'bool' and self.get_type().__repr__() == 'char':
            return conv_type.BOOL_TO_CHAR
        elif self.get_child(0).get_type().__repr__() == 'char' and self.get_type().__repr__() == 'bool':
            return conv_type.CHAR_TO_BOOL
        elif self.get_child(0).get_type().__repr__() == 'char' and self.get_type().__repr__() == 'int':
            return conv_type.CHAR_TO_INT
        elif self.get_child(0).get_type().__repr__() == 'char' and self.get_type().__repr__() == 'float':
            return conv_type.CHAR_TO_FLOAT


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
    pass


class Literal(Leaf):
    val = None

    def __init__(self, value=None):
        Leaf.__init__(self)
        self.val = value

    def get_value(self):
        return self.val


class Variable(Leaf):
    _name: str

    def __init__(self, name):
        self._name = name

    def is_lval(self):
        return True

    def get_st_entry(self):
        scope = self.get_scope()
        if scope is None:
            return None
        return scope.symbol_find(self.get_name())

    def get_type(self):
        entry = self.get_st_entry()
        if entry is None:
            return None
        return entry.type_obj

    def get_val(self):
        entry = self.get_st_entry()
        if entry is None:
            return None
        return entry.value

    def get_name(self):
        return self._name

    def get_register(self):
        return '%' + self.get_name()


class ControlWord (Leaf):
    pass


class Break (Leaf):
    pass


class Continue (Leaf):
    pass

class WhileConstr(Composite):
    pass

# Functions:
class FunctionCall(Composite):
    _name: str

    def __init__(self, name):
        super().__init__()
        self._name = name

    def get_name(self):
        return self._name

class FunctionDefinition(Scope):
    _name: str

    def __init__(self, name):
        super().__init__()
        self._name = name

    def get_name(self):
        return self._name

    def get_st_entry(self):
        scope = self.get_scope()
        if scope is None:
            return None
        return scope.symbol_find(self.get_name())

    def get_type(self):
        entry = self.get_st_entry()
        if entry is None:
            return None
        return entry.type_obj

class FunctionArgument(Composite):
    pass

