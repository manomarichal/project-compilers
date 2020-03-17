from src.utility.TypeClass import TypeClass


SymbolTable = dict


class VarEntry:
    value = None
    type_obj = None

    def __init__(self, type_obj, value):
        self.value = value
        self.type_obj = type_obj

