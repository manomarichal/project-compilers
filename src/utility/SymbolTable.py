from src.utility.TypeClass import TypeClass


class SymbolTable(dict):
    parent_table = None

    def __init__(self, parent=None):
        self.parent_table = parent

    def jump_to_parent_table(self):
        if self.parent_table == None:
            return self
        else:
            return self.parent_table


class VarEntry:
    value = None
    type_obj = None

    def __init__(self, type_obj, value):
        self.value = value
        self.type_obj = type_obj

class FuncEntry:
    type_obj = None

    def __init__(self, type_obj):
        self.type_obj = type_obj