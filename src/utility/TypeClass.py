import copy


class TypeComponents:
    VOID = 0
    BOOL = 1
    CHAR = 2
    INT = 3
    FLOAT = 4
    CONST = 5
    PTR = 6
    ARR = 7

    primitive = {BOOL, CHAR, INT, FLOAT}
    modifier = {CONST, PTR}

    translations = {VOID: "void",
                    BOOL: "bool",
                    CHAR: "char",
                    INT: "int",
                    FLOAT: "float",
                    CONST: "const",
                    PTR: "*",
                    ARR: "[]"}


class TypeClass:
    # [0] = primitive type
    # [1:] = type modifier
    _type_stack: list

    def __init__(self, type_stack, info_list=None):
        self._type_stack = []
        self._array_lengths = []
        for type_nr in range(len(type_stack)):
            new_type = type_stack[type_nr]
            if info_list is not None:
                self.pushType(new_type, info_list[type_nr])
            else:
                self.pushType(new_type)

    def pushType(self, new_type, info=None):
        self._type_stack.append(new_type)
        if new_type == TypeComponents.ARR:
            self._array_lengths.append(info)

    def popType(self, ignore_const: bool = False):
        if ignore_const and self.get_top_type() == TypeComponents.CONST:
            self._type_stack.pop()
        self._type_stack.pop()

    def get_array_len(self, index=None):
        if index is None:
            return self._array_lengths[len(self._array_lengths)-1]
        return self._array_lengths[index]

    def set_array_len(self, length, index=None):
        if index is None:
            self._array_lengths[len(self._array_lengths) - 1] = length
            return
        self._array_lengths[index] = length
        return

    def __eq__(self, other):
        return other.getType() == self.getType()

    def __ne__(self, other):
        return not self.__eq__(other)

    def getType(self):
        return self._type_stack

    def is_const(self) -> bool:
        return self.get_top_type() == TypeComponents.CONST

    def is_ptr(self) -> bool:
        return self.get_top_type(TypeComponents.CONST) == TypeComponents.PTR

    def is_array(self) -> bool:
        return self.get_top_type() == TypeComponents.ARR

    def promotes_to(self, other):
        self_type = self.get_top_type(TypeComponents.CONST)
        other_type = other.get_top_type(TypeComponents.CONST)
        result = False

        if self_type == TypeComponents.BOOL and other_type in {TypeComponents.CHAR, TypeComponents.INT, TypeComponents.FLOAT}:
            return True
        if self_type == TypeComponents.CHAR and other_type in {TypeComponents.INT, TypeComponents.FLOAT}:
            return True
        if self_type == TypeComponents.INT and other_type in {TypeComponents.FLOAT}:
            return True

        if self_type == TypeComponents.ARR and other_type == TypeComponents.PTR:  # does not take const into account
            self.popType()
            other.popType()
            if self == other:
                result = True
            self.pushType(TypeComponents.ARR)
            other.pushType(TypeComponents.PTR)

        if self_type == TypeComponents.PTR and other_type == TypeComponents.ARR:
            self.popType()
            other.popType()
            if self == other:
                result = True
            self.pushType(TypeComponents.PTR)
            other.pushType(TypeComponents.ARR)

        self.pushType(TypeComponents.CONST)
        if self == other:
            self.popType()
            result = True
        self.popType()

        return result

    def converts_to(self, other):
        if self.promotes_to(other):
            return True
        void_type = TypeClass([TypeComponents.VOID])
        if self == void_type and not other == void_type:
            return False
        if self.is_array() or other.is_array():  # not really true: arrays are ptrs & ptrs can be converted to int etc
            return False
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
        array_nr = 0
        for component in self.getType():
            if component == TypeComponents.ARR:
                result = "[" + result[0:len(result)-1]
                if self._array_lengths[array_nr] is not None:
                    result += " x" + str(self._array_lengths[array_nr])
                result += "] "
                array_nr += 1
                continue
            result += TypeComponents.translations[component] + " "
        return result[0:len(result)-1]

    def __str__(self):
        return repr(self)


bool_type = TypeClass([TypeComponents.BOOL])
char_type = TypeClass([TypeComponents.CHAR])
int_type = TypeClass([TypeComponents.INT])
float_type = TypeClass([TypeComponents.FLOAT])
