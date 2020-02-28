# Generated from Math.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MathParser import MathParser
else:
    from MathParser import MathParser

# This class defines a complete generic visitor for a parse tree produced by MathParser.

class MathVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MathParser#doc.
    def visitDoc(self, ctx:MathParser.DocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#bool_expr.
    def visitBool_expr(self, ctx:MathParser.Bool_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#comp_expr.
    def visitComp_expr(self, ctx:MathParser.Comp_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#math_expr.
    def visitMath_expr(self, ctx:MathParser.Math_exprContext):
        return self.visitChildren(ctx)



del MathParser