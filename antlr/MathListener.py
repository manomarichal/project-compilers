# Generated from Math.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MathParser import MathParser
else:
    from MathParser import MathParser

# This class defines a complete listener for a parse tree produced by MathParser.
class MathListener(ParseTreeListener):

    # Enter a parse tree produced by MathParser#doc.
    def enterDoc(self, ctx:MathParser.DocContext):
        pass

    # Exit a parse tree produced by MathParser#doc.
    def exitDoc(self, ctx:MathParser.DocContext):
        pass


    # Enter a parse tree produced by MathParser#bool_expr.
    def enterBool_expr(self, ctx:MathParser.Bool_exprContext):
        pass

    # Exit a parse tree produced by MathParser#bool_expr.
    def exitBool_expr(self, ctx:MathParser.Bool_exprContext):
        pass


    # Enter a parse tree produced by MathParser#comp_expr.
    def enterComp_expr(self, ctx:MathParser.Comp_exprContext):
        pass

    # Exit a parse tree produced by MathParser#comp_expr.
    def exitComp_expr(self, ctx:MathParser.Comp_exprContext):
        pass


    # Enter a parse tree produced by MathParser#math_expr.
    def enterMath_expr(self, ctx:MathParser.Math_exprContext):
        pass

    # Exit a parse tree produced by MathParser#math_expr.
    def exitMath_expr(self, ctx:MathParser.Math_exprContext):
        pass



del MathParser