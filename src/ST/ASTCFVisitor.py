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

                if isinstance(ast, AST.Sum):
                    value = ast.getChild(0).getValue() + ast.getChild(1).getValue()
                elif isinstance(ast, AST.Sub):
                    value = ast.getChild(0).getValue() - ast.getChild(1).getValue()
                elif isinstance(ast, AST.Prod):
                    value = ast.getChild(0).getValue() * ast.getChild(1).getValue()
                elif isinstance(ast, AST.Div):
                    value = ast.getChild(0).getValue() / ast.getChild(1).getValue()
                elif isinstance(ast, AST.Mod):
                    value = ast.getChild(0).getValue() % ast.getChild(1).getValue()
                else:
                    print("invalid math operator found while constant folding")

                ast.getParent().replaceChild(ast, AST.IntLit(value))

        elif isinstance(ast, AST.CompOp):
            if isinstance(ast.getChild(0), AST.Literal) and isinstance(ast.getChild(1), AST.Literal):

                value = False
                if isinstance(ast, AST.Equal):
                    value = ast.getChild(0).getValue() == ast.getChild(1).getValue()
                elif isinstance(ast, AST.NotEqual):
                    value = ast.getChild(0).getValue() != ast.getChild(1).getValue()
                elif isinstance(ast, AST.More):
                    value = ast.getChild(0).getValue() > ast.getChild(1).getValue()
                elif isinstance(ast, AST.Less):
                    value = ast.getChild(0).getValue() < ast.getChild(1).getValue()
                elif isinstance(ast, AST.MoreE):
                    value = ast.getChild(0).getValue() >= ast.getChild(1).getValue()
                elif isinstance(ast, AST.LessE):
                    value = ast.getChild(0).getValue() <= ast.getChild(1).getValue()
                else:
                    print("invalid comparison operator found while constant folding")

                ast.getParent().replaceChild(ast, AST.Literal(value))

        #TODO NOT Operator
        elif isinstance(ast, AST.LogicOp):
            if isinstance(ast.getChild(0), AST.Literal):
                value = False

                if isinstance(ast.getChild(1), AST.Literal):
                    if isinstance(ast, AST.Or):
                        value = ast.getChild(0).getValue() or ast.getChild(1).getValue()
                    elif isinstance(ast, AST.And):
                        value = not ast.getChild(0).getValue()
                    else:
                        print("invalid logic operator found while constant folding")

                ast.getParent().replaceChild(ast, AST.IntLiteralLit(value))

        # TODO Unary Operators



