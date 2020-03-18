from src.AST import AST
from src.AST.Visitor import Visitor
import pydot


def label_big(ast: AST.Component, name=None):
    label = type(ast).__name__
    if name is not None:
        label += ": " + str(name)
    return label + "\n(" + str(ast.get_type()) + ")"


def label_small(ast: AST.Component, name=None):
    if name is not None:
        return str(name)
    return type(ast).__name__


class DotVisitor(Visitor):
    graph = pydot.Dot(graph_type='graph')
    counter = 0

    def __init__(self, label_strategy=label_small):
        self.label_strategy = label_strategy

    def visitComposite(self, ast: AST.Composite):
        self.counter += 1
        name = self.counter
        self.graph.add_node(pydot.Node(name, label=self.label_strategy(ast)))

        for index in range(0, ast.get_child_count()):
            child_name = self.visit(ast.get_child(index))
            self.graph.add_edge(pydot.Edge(name, child_name))

        return name

    def visitLiteral(self, ast: AST.Literal):
        self.counter += 1
        self.graph.add_node(pydot.Node(self.counter, label=self.label_strategy(ast, ast.get_value())))

        return self.counter

    def visitVariable(self, ast: AST.Variable):
        self.counter += 1
        self.graph.add_node(pydot.Node(self.counter, label=self.label_strategy(ast, ast.get_name())))

        return self.counter




