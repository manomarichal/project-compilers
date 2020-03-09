from src.antlr.GrammarVisitor import  GrammarVisitor
from src.ST import AST


# to check a token's "type" (hopefully):
# <token_obj>.getSymbol().getType() == <parser>.<token_name>

# usually just trying to get a certain child will suffice:
# <context>.<token_name>()
# <context>.getChild(<index>)


class CSTVisitor (GrammarVisitor):
    uuidCounter = 0

    def aggregateResult(self, aggregate, nextResult):
        if nextResult is None:
            return aggregate
        if aggregate is None:
            return AST.DummyNode(nextResult)
        aggregate.addChild(nextResult)
        return aggregate

    def visitDoc(self, ctx):
        name = self.uuidCounter
        self.uuidCounter += 1

        return AST.Doc(name, self.visitChildren(ctx))        
    
    def visitDecl(self, ctx):

        name = self.uuidCounter
        self.uuidCounter += 1
        my_ast = AST.AssignOp()

        my_ast.addChild(self.visit(ctx.getChild(0)))
        my_ast.addChild(self.visit(ctx.getChild(2)))

        my_ast.setName(name)
        return my_ast

    def visitExpr(self, ctx):
        # skip
        if ctx.LEFT_PAREN() and ctx.RIGHT_PAREN():
            return self.visit(ctx.getChild(1))

        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        name = self.uuidCounter
        self.uuidCounter += 1
        my_ast = None
        
        # unary operator
        if ctx.getChildCount() == 2:
            if ctx.NOT_OP():
                my_ast = AST.Not()
            elif ctx.PLUS():
                my_ast = AST.Pos()
            elif ctx.MINUS():
                my_ast = AST.Neg()

            my_ast.addChild(self.visit(ctx.getChild(1)))
        
        # binary operators
        if ctx.getChildCount() == 3:
            
            # BOOLEAN OPERATORS
            if ctx.AND_OP():
                my_ast = AST.And()
            elif ctx.OR_OP():
                my_ast = AST.Or()
            
            # COMPARISON OPERATORS
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
            
            # MATH OPERATORS    
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
            
            my_ast.addChild(self.visit(ctx.getChild(0)))
            my_ast.addChild(self.visit(ctx.getChild(2)))
        
        my_ast.setName(name)
        return my_ast
    
    def visitType(self, ctx):
        for tokenNr in range(ctx.getChildCount()):
            token = ctx.getChild(tokenNr)
            token_type = token.getSymbol().getType()
            if token.getSymbol().getType() == G
