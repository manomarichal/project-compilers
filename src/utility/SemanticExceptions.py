from src.AST.AST import *
from src.utility.TypeClass import TypeClass


class SemanticException (Exception):
    node: Component
    message: str

    def __init__(self, node, message):
        self.node = node
        self.message = message

    def __repr__(self):  # TODO: add source text to AST nodes
        return type(self).__name__ + ": " + self.message + "\n\tat " + "<node_location>"

    @staticmethod
    def repr_node(node):
        result = type(node).__name__
        if hasattr(node, "get_name"):
            result += " \"" + str(node.get_name()) + "\""
        return result


class SemanticError (SemanticException):
    pass


class SemanticWarning (SemanticException):
    pass


class DocumentException (SemanticException):
    pass


class StatementException (SemanticException):
    pass


class ImplicitConversionWarning (SemanticWarning, StatementException):
    def __init__(self, node: Component, from_type: TypeClass, to_type: TypeClass):
        self.node = node
        self.message = "implicitly converting " + str(from_type) + " to " + str(to_type)

        self.from_type = from_type
        self.to_type = to_type


class UninitialisedWarning (SemanticWarning, StatementException):
    def __init__(self, node: Variable):
        self.node = node
        self.message = "usage of value of uninitialised variable \"" + node.get_name() + "\""


class NoConversionError (SemanticError, StatementException):
    def __init__(self, node: Component, a_type: TypeClass, b_type: TypeClass, bidirectional: bool):
        self.node = node
        self.message = "can't convert " + str(a_type) + " to " + str(b_type)
        if bidirectional:
            self.message += " or vice versa"

        self.a_type = a_type
        self.b_type = b_type


class InvalidTypeError (SemanticError, StatementException):
    def __init__(self, node: Component, my_type: TypeClass):
        self.node = node
        self.message = "invalid type " + str(my_type) + " for " + self.repr_node(node)


class UndeclaredError (SemanticError, StatementException):
    def __init__(self, node: Component):
        self.node = node
        self.message = "usage of undeclared " + self.repr_node(node)


class RedeclaredError (SemanticError, StatementException):
    def __init__(self, node: Component):
        self.node = node
        self.message = "redeclaration of " + self.repr_node(node)


class RValError (SemanticError, StatementException):
    def __init__(self, node: Component, detail=None):
        self.node = node
        self.message = self.repr_node(node) + " expected l-val, got r-val"
        if detail is not None:
            self. message += " (" + detail + ")"


class ConstAssignmentError (SemanticError, StatementException):
    def __init__(self, node: AssignOp):
        self.node = node
        self.message = "assigning to constant of type \"" + node.get_child(0).get_type().__repr__() + "\""
