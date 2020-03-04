from ST import AST

class ASTCFVisitor:
    def visit(self, tree):
        return tree.accept(self)

    def visitComponent(self, ast:AST.Component):

        if isinstance(ast, AST.Leaf):
            return

        for index in range(0, ast.getChildCount()):
            self.visit(ast.getChild(index))

        if isinstance(ast, AST.MathOp):
            if isinstance(ast.getChild(0), AST.IntLit) and isinstance(ast.getChild(1), AST.IntLit):
                value = 0

                if (isinstance(ast, AST.Sum)):
                    value = ast.getChild(0).getValue() + ast.getChild(1).getValue()
                elif (isinstance(ast, AST.Sub)):
                    value = ast.getChild(0).getValue() - ast.getChild(1).getValue()
                elif (isinstance(ast, AST.Prod)):
                    value = ast.getChild(0).getValue() * ast.getChild(1).getValue()
                elif (isinstance(ast, AST.Div)):
                    value = ast.getChild(0).getValue() / ast.getChild(1).getValue()
                elif (isinstance(ast, AST.Mod)):
                    value = ast.getChild(0).getValue() % ast.getChild(1).getValue()

                ast.getParent().replaceChild(ast, AST.IntLit(value))

        # TODO UNARY OPERATORS & LOGIC OPERATORS



