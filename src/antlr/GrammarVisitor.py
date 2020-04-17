# Generated from src/antlr/Grammar.g4 by ANTLR 4.8
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


    # Visit a parse tree produced by GrammarParser#block.
    def visitBlock(self, ctx:GrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#typeObj.
    def visitTypeObj(self, ctx:GrammarParser.TypeObjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#arrayIndex.
    def visitArrayIndex(self, ctx:GrammarParser.ArrayIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#arrayLit.
    def visitArrayLit(self, ctx:GrammarParser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#identifier.
    def visitIdentifier(self, ctx:GrammarParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#statement.
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#control.
    def visitControl(self, ctx:GrammarParser.ControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#functionDecl.
    def visitFunctionDecl(self, ctx:GrammarParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#functionCall.
    def visitFunctionCall(self, ctx:GrammarParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#functionArgument.
    def visitFunctionArgument(self, ctx:GrammarParser.FunctionArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#parenCond.
    def visitParenCond(self, ctx:GrammarParser.ParenCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#stateOrScope.
    def visitStateOrScope(self, ctx:GrammarParser.StateOrScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#construct.
    def visitConstruct(self, ctx:GrammarParser.ConstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#scopeConstr.
    def visitScopeConstr(self, ctx:GrammarParser.ScopeConstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ifConstr.
    def visitIfConstr(self, ctx:GrammarParser.IfConstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#switchConstr.
    def visitSwitchConstr(self, ctx:GrammarParser.SwitchConstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#caseBranch.
    def visitCaseBranch(self, ctx:GrammarParser.CaseBranchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#defaultBranch.
    def visitDefaultBranch(self, ctx:GrammarParser.DefaultBranchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#forConstr.
    def visitForConstr(self, ctx:GrammarParser.ForConstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#whileConstr.
    def visitWhileConstr(self, ctx:GrammarParser.WhileConstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#general_expr.
    def visitGeneral_expr(self, ctx:GrammarParser.General_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#decl.
    def visitDecl(self, ctx:GrammarParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#pureDecl.
    def visitPureDecl(self, ctx:GrammarParser.PureDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#returnStatement.
    def visitReturnStatement(self, ctx:GrammarParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#literal.
    def visitLiteral(self, ctx:GrammarParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expr.
    def visitExpr(self, ctx:GrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#printf.
    def visitPrintf(self, ctx:GrammarParser.PrintfContext):
        return self.visitChildren(ctx)



del GrammarParser