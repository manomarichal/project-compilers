import copy

PrimitiveComp = {"bool", "char", "int", "float"}
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
        my_top = self.get_top_type("const")
        other_top = other.get_top_type("const")

        if my_top == "char":
            return other_top in {"int", "float"}
        elif my_top == "int":
            return other_top == "float"

        return False

    def converts_to(self, other):
        return True

    def get_top_type(self, ignore=None):
        if ignore is None:
            return self._type_stack[len(self._type_stack)-1]
        elif not isinstance(ignore, list):
            ignore = [ignore]
        else:
            for result in reversed(self._type_stack):
                if result not in ignore:
                    return result

    def __repr__(self):
        result = ""
        for component in self.getType():
            result += component + " "
        return result[0:len(result)-1]
