from src.AST.AST import *
from src.utility.TypeClass import TypeClass


class SemanticException (Exception):
    node: Component
    message: str

    def __init__(self, node, message):
        self.node = node
        self.message = message

    def __repr__(self):  # TODO: add source text to AST nodes
        return type(self).__name__ + ": " + self.message + "\nat " + "<node_location>"


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


class NoConversionError (SemanticError, StatementException):
    def __init__(self, node: Component, a_type: TypeClass, b_type: TypeClass, bidirectional: bool):
        self.node = node
        self.message = "can't convert " + str(a_type) + " to " + str(b_type)
        if bidirectional:
            self.message += " or vice versa"

        self.a_type = a_type
        self.b_type = b_type


class InvalidTypeError (SemanticError, StatementException):
    def __init__(self, node: Component, node_type: TypeClass):
        self.node = node
        self.message = "invalid type " + str(node_type) + " for " + type(node).__name__

        self.node_type = node_type
