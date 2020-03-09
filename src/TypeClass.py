# from enum import Enum, auto
# class TypeComponents (Enum):
#     CHAR = auto()
#     INT = auto()
#     FLOAT = auto()
#     PTR = auto()
#     CONST = auto()


TypeComponents = {"char", "int", "float", "*", "const"}


class TypeClass:
    _type_stack = []

    def __init__(self, type):
        assert TypeComponents.issuperset(type)
        self._type_stack = type

    def __eq__(self, other):
        return other.getType() == self.getType()

    def __ne__(self, other):
        return not self == other

    def getType(self):
        return self._type_stack

    def __repr__(self):
        result = ""
        for component in self.getType():
            result += component + " "
        return result[0:len(result)-2]
