import copy

PrimitiveComp = {"char", "int", "float"}
ModifierComp = {"const", "*"}
TypeComp = copy.deepcopy(PrimitiveComp)
TypeComp.union(ModifierComp)


class TypeClass:
    # [0] = primitive type
    # [1:] = type modifier
    _type_stack = []

    def __init__(self, type):
        self._type_stack = type

    def pushType(self, newType):
        self._type_stack.append(newType)

    def __eq__(self, other):
        return other.getType() == self.getType()

    def __ne__(self, other):
        return not self == other

    def getType(self):
        return self._type_stack

    def is_const(self) -> bool:
        tmp = self.get_top_type() == "const"
        return tmp

    def is_ptr(self) -> bool:
        return self.get_top_type("const") == "*"

    def promotes_to(self, other):
        self_type = self.get_top_type("const")
        other_type = other.get_top_type("const")
        if self_type == "char" and other_type in {"int", "float"}:
            return True
        if self_type == "int" and other_type == "float":
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
                return type

    def __repr__(self):
        result = ""
        for component in self.getType():
            result += component + " "
        return result[0:len(result)-1]
