from src.antlr.GrammarVisitor import GrammarVisitor
from src.antlr.GrammarParser import GrammarParser
from src.AST import AST
from src.utility.TypeClass import TypeClass, TypeComponents
from src.utility.SymbolTable import SymbolTable, VarEntry, FuncEntry, SymEntry

from copy import deepcopy


# to check a token's "type" (hopefully):
# <token_obj>.getSymbol().getType() == <parser>.<token_name>

# usually just trying to get a certain child will suffice:
# <context>.<token_name>()
# <context>.getChild(<index>)


def source_from_ctx(ctx):
    start = ctx.start
    return "\"" + start.source[1].fileName + "\", line " + str(start.line)


class Visitor (GrammarVisitor):
    _current_sym_table: SymbolTable = SymbolTable()

    def enter_scope(self, ast: AST.Scope):
        ast.set_symbol_table(SymbolTable(self._current_sym_table))
        self._current_sym_table = ast.get_symbol_table()

    def enter_existing_scope(self, ast: AST.Scope):
        self._current_sym_table = ast.get_symbol_table()

    def exit_scope(self, ast: AST.Scope):
        self._current_sym_table = self._current_sym_table.jump_to_parent_table()

    def aggregateResult(self, aggregate: AST.DummyNode, nextResult):
        if nextResult is None:
            return aggregate
        elif aggregate is None:
            return nextResult
        elif not isinstance(aggregate, AST.DummyNode):
            aggregate = AST.DummyNode([aggregate, nextResult])
        else:
            aggregate.add_child(nextResult)
        return aggregate

    def visitBlock(self, ctx: GrammarParser.BlockContext):
        statements = []
        for a in range(ctx.getChildCount()):
            statements.append(self.visit(ctx.getChild(a)))
        return statements

    def visitDoc(self, ctx):
        my_ast = AST.Doc()
        self.enter_scope(my_ast)
        my_ast.add_childs(self.visitBlock(ctx.block()))
        my_ast.set_source_loc(source_from_ctx(ctx))
        self.exit_scope(my_ast)
        return my_ast

    def visitScopeConstr(self, ctx: GrammarParser.ScopeConstrContext):
        my_ast = AST.Scope()
        my_ast.set_symbol_table(self._current_sym_table)
        my_ast.add_childs(self.visitBlock(ctx.block()))
        return my_ast

    def visitIfConstr(self, ctx: GrammarParser.IfConstrContext):
        my_ast = AST.IfStatement()
        self.enter_scope(my_ast)
        my_ast.set_condition(self.visit(ctx.parenCond()))
        my_ast.set_then(self.visit(ctx.stateOrScope(0)))
        if len(ctx.stateOrScope()) == 2:
            my_ast.set_else(self.visit(ctx.stateOrScope(1)))
        my_ast.set_source_loc(source_from_ctx(ctx))
        self.exit_scope(my_ast)
        return my_ast

    def visitSwitchConstr(self, ctx: GrammarParser.SwitchConstrContext):
        my_ast = AST.SwitchStatement()
        self.enter_scope(my_ast)
        my_ast.set_condition(self.visit(ctx.parenCond()))
        for branch_ctx in ctx.caseBranch():
            my_ast.add_branch(self.visit(branch_ctx))
        if ctx.defaultBranch():
            my_ast.add_branch(self.visit(ctx.defaultBranch()))
        my_ast.set_source_loc(source_from_ctx(ctx))
        self.exit_scope(my_ast)
        return my_ast

    def visitCaseBranch(self, ctx: GrammarParser.CaseBranchContext):
        my_ast = AST.CaseBranch()
        my_ast.set_constant(self.visit(ctx.literal()))
        self.add_child_block(my_ast, ctx.block())
        my_ast.set_source_loc(source_from_ctx(ctx))
        return my_ast

    def visitDefaultBranch(self, ctx: GrammarParser.DefaultBranchContext):
        my_ast = AST.CaseBranch()
        self.add_child_block(my_ast, ctx.block())
        my_ast.set_source_loc(source_from_ctx(ctx))
        return my_ast

    def visitForConstr(self, ctx: GrammarParser.ForConstrContext):
        my_ast = AST.ForStatement()
        self.enter_scope(my_ast)
        params = [self.visit(ctx.general_expr(i)) for i in range(3)]
        my_ast.set_init(params[0])
        my_ast.set_check(params[1])
        my_ast.set_advance(params[2])
        my_ast.set_contents(self.visit(ctx.stateOrScope()))
        my_ast.set_source_loc(source_from_ctx(ctx))
        self.exit_scope(my_ast)
        return my_ast

    def visitWhileConstr(self, ctx: GrammarParser.WhileConstrContext):
        my_ast = AST.WhileStatement()
        self.enter_scope(my_ast)
        my_ast.set_check(self.visit(ctx.parenCond()))
        my_ast.set_contents(self.visit(ctx.stateOrScope()))
        my_ast.set_source_loc(source_from_ctx(ctx))
        self.exit_scope(my_ast)
        return my_ast

    def visitExpr(self, ctx):
        # skip
        if ctx.functionCall():
            a = self.visit(ctx.getChild(0))
            return a

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
            elif isinstance(ctx.getChild(0), GrammarParser.ExprContext):  # postfix operators go here
                if ctx.DECR():
                    my_ast = AST.DecrPost()
                elif ctx.INCR():
                    my_ast = AST.IncrPost()
                my_ast.set_positional_child(0, self.visit(ctx.getChild(0)))
                my_ast.set_source_loc(source_from_ctx(ctx))
                return my_ast
            elif ctx.arrayIndex():
                my_ast = AST.Index()
                index = self.visit(ctx.arrayIndex())
                my_ast.add_child(self.visit(ctx.getChild(0)))
                my_ast.set_index(index)
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

        my_ast.set_source_loc(source_from_ctx(ctx))
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
        if ctx.arrayLit():
            my_ast = self.visit(ctx.arrayLit())

        my_ast.set_source_loc(source_from_ctx(ctx))
        return my_ast

    def visitArrayLit(self, ctx: GrammarParser.ArrayLitContext):  # not very type-safe at all
        my_ast = AST.Literal(value=[])

        element = None
        for child in ctx.literal():
            element = self.visit(child)
            my_ast.get_value().append(element.get_value())
        my_type: TypeClass = deepcopy(element.get_type())
        my_type.pushType(TypeComponents.ARR, len(ctx.literal()))
        my_ast.set_type(my_type)

        my_ast.set_source_loc(source_from_ctx(ctx))
        return my_ast

    def visitTypeObject(self, ctx):
        type_stack = []

        const_reminder = False

        # TODO syntax errors, semantic shit and warnings
        # TODO (maybe) no more strings =(
        for tokenNr in range(ctx.getChildCount()):
            token = ctx.getChild(tokenNr)
            token_type = token.getSymbol().type

            if token_type in {GrammarParser.CHAR_TYPE, GrammarParser.INT_TYPE, GrammarParser.FLOAT_TYPE, GrammarParser.VOID_TYPE}:
                assert len(type_stack) == 0
                if token_type == GrammarParser.VOID_TYPE:
                    type_stack.append(TypeComponents.VOID)
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
        var.set_source_loc(source_from_ctx(ctx))
        my_ast.add_child(var)

        var_type = self.visitTypeObject(ctx.getChild(0))
        if ctx.arrayIndex():
            var_type.pushType(TypeComponents.ARR, self.visit(ctx.arrayIndex()).get_value())
        self._current_sym_table[ctx.getChild(1).getText()] = VarEntry(var_type, None)

        my_ast.set_source_loc(source_from_ctx(ctx))
        if ctx.ASSIGN_OP() is not None:
            assign = AST.AssignOp()
            assign.add_child(my_ast)
            assign.add_child(self.visit(ctx.expr()))
            assign.set_source_loc(source_from_ctx(ctx))
            return assign
        else:
            return my_ast

    def visitIdentifier(self, ctx):
        my_ast = AST.Variable(name=ctx.getText())
        my_ast.set_source_loc(source_from_ctx(ctx))
        return my_ast

    def visitPrintf(self, ctx):
        my_ast = AST.Printf()
        my_ast.add_child(self.visit(ctx.getChild(2)))
        my_ast.set_source_loc(source_from_ctx(ctx))
        return my_ast

    def visitControl(self, ctx: GrammarParser.ControlContext):
        my_ast = None
        token_type = ctx.getChild(0).getSymbol().type
        if token_type == GrammarParser.BREAK_KW:
            my_ast = AST.Break()
        if token_type == GrammarParser.CONT_KW:
            my_ast = AST.Continue()
        my_ast.set_source_loc(source_from_ctx(ctx))
        return my_ast

    def visitFunctionCall(self, ctx: GrammarParser.FunctionCallContext):
        my_ast = AST.FunctionCall(ctx.getChild(0).getText())
        for a in range(1, len(ctx.children)):
            if isinstance(ctx.getChild(a), GrammarParser.FunctionArgumentContext):
                my_ast.add_child(self.visit(ctx.getChild(a)))
        my_ast.set_source_loc(source_from_ctx(ctx))
        return my_ast

    def visitFunctionDecl(self, ctx: GrammarParser.FunctionDeclContext):
        my_ast = AST.FunctionDefinition(ctx.getChild(1).getText())
        my_ast.set_source_loc(source_from_ctx(ctx))

        # set type & arg_count of function
        my_st_entry = FuncEntry(self.visitTypeObject(ctx.getChild(0)))
        my_st_entry.arg_count = len(ctx.typeObj())-1

        self.enter_scope(my_ast)

        # make function body
        my_ast.add_child(self.visit(ctx.getChild(len(ctx.children) - 1)))

        # add variables within the scope for each argument & add argument info to function's st entry
        for a in range(1, len(ctx.children)-1):
            if isinstance(ctx.getChild(a), GrammarParser.TypeObjContext):
                arg = AST.Variable(ctx.getChild(a+1).getText())
                arg.set_source_loc(ctx.getChild(a+1))
                decl = AST.Decl()
                decl.set_source_loc(ctx.getChild(a + 1))
                decl.add_child(arg)
                my_ast.add_child(decl)
                arg_type = self.visitTypeObject(ctx.getChild(a))
                self._current_sym_table[arg.get_name()] = VarEntry(arg_type)
                my_st_entry.arg_types.append(arg_type)

        self.exit_scope(my_ast)

        # save function's st entry
        self._current_sym_table[ctx.getChild(1).getText()] = my_st_entry
        return my_ast

    def visitReturnStatement(self, ctx:GrammarParser.ReturnStatementContext):
        my_ast = AST.ReturnStatement()
        my_ast.set_source_loc(source_from_ctx(ctx))
        my_ast.add_child(self.visit(ctx.getChild(1)))
        return my_ast

    def visitArrayIndex(self, ctx: GrammarParser.ArrayIndexContext):
        index = self.visit(ctx.getChild(1))
        index.set_type(TypeClass([TypeComponents.INT]))
        return index

