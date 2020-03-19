from src.antlr.GrammarVisitor import GrammarVisitor
from src.antlr.GrammarParser import GrammarParser
from src.AST import AST
from src.utility.TypeClass import TypeClass, TypeComponents
from src.utility.SymbolTable import SymbolTable, VarEntry


# to check a token's "type" (hopefully):
# <token_obj>.getSymbol().getType() == <parser>.<token_name>

# usually just trying to get a certain child will suffice:
# <context>.<token_name>()
# <context>.getChild(<index>)


class Visitor (GrammarVisitor):

    _current_scope = None

    def aggregateResult(self, aggregate, nextResult):
        if nextResult is None:
            return aggregate
        if aggregate is None:
            return AST.DummyNode(nextResult)
        aggregate.add_child(nextResult)
        return aggregate

    def visitDoc(self, ctx):
        my_ast = AST.Doc()
        my_ast.set_symbol_table(SymbolTable())
        self._current_scope = my_ast.get_symbol_table()
        my_ast.swap_children(self.visitChildren(ctx))
        return my_ast

    def visitExpr(self, ctx):
        # skip
        if ctx.LEFT_PAREN() and ctx.RIGHT_PAREN():
            return self.visit(ctx.getChild(1))

        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        my_ast = None

        # unary operator
        if ctx.getChildCount() == 2:
            if ctx.NOT_OP():
                my_ast = AST.Not()
            elif ctx.PLUS():
                my_ast = AST.Pos()
            elif ctx.MINUS():
                my_ast = AST.Neg()
            elif ctx.AMP():
                my_ast = AST.Adress()
            elif ctx.STAR():
                my_ast = AST.Indir()
            elif isinstance(ctx.getChild(0), GrammarParser.ExprContext):
                if ctx.getChild(1).getSymbol().type == GrammarParser.DECR:
                    my_ast = AST.DecrPost()
                elif ctx.getChild(1).getSymbol().type == GrammarParser.INCR:
                    my_ast = AST.IncrPost()
                my_ast.add_child(self.visit(ctx.getChild(0)))
                return my_ast
            elif ctx.getChild(0).getSymbol().type == GrammarParser.INCR:
                my_ast = AST.IncrPre()
            elif ctx.getChild(0).getSymbol().type == GrammarParser.DECR:
                my_ast = AST.DecrPre()

            my_ast.add_child(self.visit(ctx.getChild(1)))

        # binary operators
        if ctx.getChildCount() == 3:
            # ASSIGNMENT
            if ctx.ASSIGN_OP():
                my_ast = AST.AssignOp()

            # BOOLEAN OPERATORS
            elif ctx.AND_OP():
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

            my_ast.add_child(self.visit(ctx.getChild(0)))
            my_ast.add_child(self.visit(ctx.getChild(2)))

        return my_ast

    def visitLiteral(self, ctx):
        my_ast = AST.Literal()

        if ctx.CHAR():  #TODO (maybe) multivalue chars
            my_ast.val = ord(ctx.getText()[1])
            my_ast.set_type(TypeClass([TypeComponents.CHAR]))
        if ctx.INT():
            my_ast.val = int(ctx.getText())
            my_ast.set_type(TypeClass([TypeComponents.INT]))
        if ctx.FLOAT():
            my_ast.val = float(ctx.getText())
            my_ast.set_type(TypeClass([TypeComponents.FLOAT]))

        return my_ast

    def visitTypeObject(self, ctx):
        type_stack = []

        const_reminder = False

        # TODO syntax errors, semantic shit and warnings
        # TODO (maybe) no more strings =(
        for tokenNr in range(ctx.getChildCount()):
            token = ctx.getChild(tokenNr)
            token_type = token.getSymbol().type

            if token_type in {GrammarParser.CHAR_TYPE, GrammarParser.INT_TYPE, GrammarParser.FLOAT_TYPE}:
                assert len(type_stack) == 0
                if token_type == GrammarParser.CHAR_TYPE:
                    type_stack.append(TypeComponents.CHAR)
                if token_type == GrammarParser.INT_TYPE:
                    type_stack.append(TypeComponents.INT)
                if token_type == GrammarParser.FLOAT_TYPE:
                    type_stack.append(TypeComponents.FLOAT)
                if const_reminder:
                    type_stack.append(TypeComponents.CONST)

            if token_type == GrammarParser.STAR:
                assert len(type_stack) > 0
                type_stack.append(TypeComponents.PTR)
            if token_type == GrammarParser.CONST:
                if len(type_stack) == 0:
                    const_reminder = True
                else:
                    assert type_stack[len(type_stack)-1] != TypeComponents.CONST
                    type_stack.append(TypeComponents.CONST)

        return TypeClass(type_stack)

    def visitDecl(self, ctx):
        my_ast = AST.Decl()
        var = AST.Variable(ctx.getChild(1).getText())
        my_ast.add_child(var)

        self._current_scope[ctx.getChild(1).getText()] = VarEntry(self.visitTypeObject(ctx.getChild(0)), None)

        if ctx.getChildCount() == 4:
            assign = AST.AssignOp()
            assign.add_child(my_ast)
            assign.add_child(self.visit(ctx.getChild(3)))
            return assign

        else:
            return my_ast

    def visitIdentifier(self, ctx):
        my_ast = AST.Variable(name=ctx.getText())
        return my_ast

    def visitPrintf(self, ctx):
        my_ast = AST.Printf()
        my_ast.add_child(self.visit(ctx.getChild(2)))
        return my_ast

