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
        if self.get_top_type() == "const":
            return self._type_stack[len(self._type_stack)] == "*"
        return self.get_top_type == "*"

    def get_top_type(self):
        return self._type_stack[len(self._type_stack)-1]

    def __repr__(self):
        result = ""
        for component in self.getType():
            result += component + " "
        return result[0:len(result)-1]
