from src.SyntaxTrees import AST
from src.SyntaxTrees.ASTVisitor import ASTVisitor
import pydot


class ASTDotVisitor(ASTVisitor):
    graph = pydot.Dot(graph_type='graph')
    def visitComposite(self, ast: AST.Composite):
        self.graph.add_node(pydot.Node(ast.get_name(), label=type(ast).__name__))

        if ast.get_parent() is not None:
            self.graph.add_edge(pydot.Edge(ast.get_parent().get_name(), ast.get_name()))

        for index in range(0, ast.get_child_count()):
            self.visit(ast.get_child(index))

    def visitLiteral(self, ast: AST.Literal):
        self.graph.add_node(pydot.Node(ast.get_name(), label=ast.val))

        if ast.get_parent() is not None:
            self.graph.add_edge(pydot.Edge(ast.get_parent().get_name(), ast.get_name()))

    def visitVariable(self, ast: AST.Variable):
        self.graph.add_node(pydot.Node(ast.get_name(), label='cool naam'))

        if ast.get_parent() is not None:
            self.graph.add_edge(pydot.Edge(ast.get_parent().get_name(), ast.get_name()))



