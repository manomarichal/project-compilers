from antlr.MathVisitor import MathVisitor
import AST


# to check a token's "type" (hopefully):
# <token_obj>.getSymbol().getType() == <parser>.<token_name>

# usually just trying to get a certain child will suffice:
# <context>.<token_name>()
# <context>.getChild(<index>)


class CustomVisitor (MathVisitor):
    def aggregateResult(self, aggregate, nextResult):
        if aggregate is None:
            return [nextResult]
        return aggregate.append(nextResult)

    def visitDoc(self, ctx):
        return AST.Doc(self.visitChildren(ctx))

    def visitBool_expr(self, ctx):
        if ctx.LEFT_PAREN() and ctx.RIGHT_PAREN():
            return self.visit(ctx.getChild(1))

        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        my_ast = AST.Operator()

        if ctx.getChildCount() == 2:
            if ctx.NOT_OP():
                my_ast = AST.Not()

            my_ast.children.append(self.visit(ctx.getChild(1)))

        elif ctx.getChildCount() == 3:
            if ctx.AND_OP():
                my_ast = AST.And()
            elif ctx.OR_OP():
                my_ast = AST.Or()

            my_ast.children.append(self.visit(ctx.getChild(0)))
            my_ast.children.append(self.visit(ctx.getChild(2)))

        return my_ast

    def visitComp_expr(self, ctx):
        my_ast = AST.Operator()

        if ctx.SMALLER_OP():
            my_ast = AST.Less()
        elif ctx.GREATER_OP():
            my_ast = AST.More()
        elif ctx.EQUAL_OP():
            my_ast = AST.Equal()
        elif ctx.SMALLER_E_OP():
            my_ast = AST.LessE()
        elif ctx.GREATER_E_OP():
            my_ast = AST.MoreE()
        elif ctx.NOT_EQUAL_OP():
            my_ast = AST.NotEqual()

        my_ast.children.append(self.visit(ctx.getChild(0)))
        my_ast.children.append(self.visit(ctx.getChild(2)))

    def visitMath_expr(self, ctx):
        if ctx.LEFT_PAREN() and ctx.RIGHT_PAREN():
            return self.visit(ctx.getChild(1))

        my_ast = AST.Operator()

        if ctx.getChildCount() == 1:
            if ctx.INT():
                my_ast = AST.IntLit(int(ctx.getText()))

        elif ctx.getChildCount() == 2:
            if ctx.PLUS():
                my_ast = AST.Pos()
            elif ctx.MINUS():
                my_ast = AST.Neg()

            my_ast.children.append(self.visit(ctx.getChild(1)))

        elif ctx.getChildCount() == 3:
            if ctx.STAR():
                my_ast = AST.Prod()
            elif ctx.SLASH():
                my_ast = AST.Div()
            elif ctx.PERCENT():
                my_ast = AST.Mod()
            elif ctx.PLUS():
                my_ast = AST.Sum()
            elif ctx.MINUS():
                my_ast = AST.Sub()

            my_ast.children.append(self.visit(ctx.getChild(0)))
            my_ast.children.append(self.visit(ctx.getChild(2)))

        return my_ast
