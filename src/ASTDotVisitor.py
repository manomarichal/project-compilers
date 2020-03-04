from src import AST
import pydot

class ASTDotVisitor():
    graph = pydot.Dot(graph_type='graph')
    operatorCounter = 0
    literalCounter = 0
    docCounter = 0

    def visit(self, ast: AST.Component):
        return ast.accept(self)

    def visitComposite(self, ast:AST.Composite):
        self.graph.add_node(self, ast.getName())

        if ast.getParent() is not None:
            self.graph.add_edge(pydot.Edge(ast.getParent().getName(), ast.getName()))

        index = 0
        for index in range(ast.getChildCount()):
            self.visit(self, ast.getChild(index))




