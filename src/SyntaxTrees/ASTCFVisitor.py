from src.SyntaxTrees import AST


class ASTCFVisitor:
    def visit(self, tree):
        return tree.accept(self)

    def visitComponent(self, ast):

        if isinstance(ast, AST.Leaf):
            return

        for index in range(0, ast.get_child_count()):
            self.visit(ast.get_child(index))

        if isinstance(ast, AST.MathOp):
            if isinstance(ast.get_child(0), AST.Literal) and isinstance(ast.get_child(1), AST.Literal):
                value = 0

                if isinstance(ast, AST.Sum):
                    value = ast.get_child(0).get_value() + ast.get_child(1).get_value()
                elif isinstance(ast, AST.Sub):
                    value = ast.get_child(0).get_value() - ast.get_child(1).get_value()
                elif isinstance(ast, AST.Prod):
                    value = ast.get_child(0).get_value() * ast.get_child(1).get_value()
                elif isinstance(ast, AST.Div):
                    value = ast.get_child(0).get_value() / ast.get_child(1).get_value()
                elif isinstance(ast, AST.Mod):
                    value = ast.get_child(0).get_value() % ast.get_child(1).get_value()
                else:
                    print("invalid math operator found while constant folding")

                ast.get_parent().replace_child(ast, AST.Literal(value))

        elif isinstance(ast, AST.CompOp):
            if isinstance(ast.get_child(0), AST.Literal) and isinstance(ast.get_child(1), AST.Literal):

                value = False
                if isinstance(ast, AST.Equal):
                    value = ast.get_child(0).get_value() == ast.get_child(1).get_value()
                elif isinstance(ast, AST.NotEqual):
                    value = ast.get_child(0).get_value() != ast.get_child(1).get_value()
                elif isinstance(ast, AST.More):
                    value = ast.get_child(0).get_value() > ast.get_child(1).get_value()
                elif isinstance(ast, AST.Less):
                    value = ast.get_child(0).get_value() < ast.get_child(1).get_value()
                elif isinstance(ast, AST.MoreE):
                    value = ast.get_child(0).get_value() >= ast.get_child(1).get_value()
                elif isinstance(ast, AST.LessE):
                    value = ast.get_child(0).get_value() <= ast.get_child(1).get_value()
                else:
                    print("invalid comparison operator found while constant folding")

                ast.get_parent().replace_child(ast, AST.Literal(value))

        elif isinstance(ast, AST.LogicOp):
            if isinstance(ast.get_child(0), AST.Literal):
                if isinstance(ast, AST.Not):
                    value = not (ast.get_child(0).get_value() != 0)

                elif isinstance(ast.get_child(1), AST.Literal):
                    if isinstance(ast, AST.Or):
                        value = (ast.get_child(0).get_value() != 0) or (ast.get_child(1).get_value() != 0)
                    elif isinstance(ast, AST.And):
                        value = (ast.get_child(0).get_value() != 0) and (ast.get_child(1).get_value() != 0)
                    else:
                        print("invalid logic operator found while constant folding")
                        exit(1)
                else:
                    print("something went wrong when constant folding with a logic operator")
                    exit(1)

                ast.get_parent().replace_child(ast, AST.Literal(value))

        elif isinstance(ast, AST.UnaryOp):
            if isinstance(ast.get_child(0), AST.Literal):
                if isinstance(ast, AST.Pos):
                    ast.get_parent().replace_child(ast, AST.Literal(ast.get_child(0).get_value()))
                elif isinstance(ast, AST.Neg):
                    ast.get_parent().replace_child(ast, AST.Literal(-ast.get_child(0).get_value()))
                else:
                    print("something went wrong when constant folding with an unary operator")
                    exit(1)
