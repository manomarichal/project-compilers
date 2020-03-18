import copy


class TypeComponents:
    BOOL = 1
    CHAR = 2
    INT = 3
    FLOAT = 4
    CONST = 5
    PTR = 6

    primitive = {BOOL, CHAR, INT, FLOAT}
    modifier = {CONST, PTR}

    translations = {BOOL: "bool",
                    CHAR: "char",
                    INT: "int",
                    FLOAT: "float",
                    CONST: "const",
                    PTR: "*"}


class TypeClass:
    # [0] = primitive type
    # [1:] = type modifier
    _type_stack = []

    def __init__(self, type_stack):
        self._type_stack = type_stack

    def pushType(self, new_type):
        self._type_stack.append(new_type)

    def popType(self):
        if self.get_top_type() == TypeComponents.CONST:
            self._type_stack.pop()
        self._type_stack.pop()

    def __eq__(self, other):
        return other.getType() == self.getType()

    def __ne__(self, other):
        return not self == other

    def getType(self):
        return self._type_stack

    def is_const(self) -> bool:
        return self.get_top_type() == TypeComponents.CONST

    def is_ptr(self) -> bool:
        return self.get_top_type(TypeComponents.CONST) == TypeComponents.PTR

    def promotes_to(self, other):
        self_type = self.get_top_type(TypeComponents.CONST)
        other_type = other.get_top_type(TypeComponents.CONST)
        if self_type == TypeComponents.CHAR and other_type in {TypeComponents.INT, TypeComponents.FLOAT}:
            return True
        if self_type == TypeComponents.INT and other_type == TypeComponents.FLOAT:
            return True
        return False

    def converts_to(self, other):
        return True

    def get_top_type(self, exclude=None):
        if exclude is None:
            return self._type_stack[len(self._type_stack)-1]
        if not isinstance(exclude, list):
            exclude = [exclude]
        for type_comp in reversed(self._type_stack):
            if type_comp not in exclude:
                return type_comp

    def __repr__(self):
        result = ""
        for component in self.getType():
            result += TypeComponents.translations[component] + " "
        return result[0:len(result)-1]