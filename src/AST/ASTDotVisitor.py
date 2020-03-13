from src.SyntaxTrees import AST
from src.SyntaxTrees.ASTVisitor import ASTVisitor
import pydot


class ASTDotVisitor(ASTVisitor):
    graph = pydot.Dot(graph_type='graph')
    counter = 0
    def visitComposite(self, ast: AST.Composite):
        self.counter += 1
        name = self.counter
        self.graph.add_node(pydot.Node(name, label=type(ast).__name__))

        for index in range(0, ast.get_child_count()):
            child_name = self.visit(ast.get_child(index))
            self.graph.add_edge(pydot.Edge(name, child_name))

        return name

    def visitLiteral(self, ast: AST.Literal):
        self.counter += 1
        self.graph.add_node(pydot.Node(self.counter, label=ast.val))

        return self.counter

    def visitVariable(self, ast: AST.Variable):
        self.counter += 1
        self.graph.add_node(pydot.Node(self.counter, label=ast.get_name()))

        return self.counter




