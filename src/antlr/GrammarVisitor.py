# Generated from src/Grammar.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#doc.
    def visitDoc(self, ctx:GrammarParser.DocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#bool_expr.
    def visitBool_expr(self, ctx:GrammarParser.Bool_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#comp_expr.
    def visitComp_expr(self, ctx:GrammarParser.Comp_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#math_expr.
    def visitMath_expr(self, ctx:GrammarParser.Math_exprContext):
        return self.visitChildren(ctx)



del GrammarParser