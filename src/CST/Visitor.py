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

    def extract_decl(self, ctx: GrammarParser.PureDeclContext):
        name = ctx.identifier().getText()

        my_type = self.visitTypeObject(ctx.typeObj())
        if ctx.arrayIndex():
            my_type.pushType(TypeComponents.ARR)
            if ctx.arrayIndex().literal():
                my_type.set_array_len(int(self.visit(ctx.arrayIndex().literal()).get_value()))

        return name, my_type

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
        my_ast.IO = ctx.STDIO() is not None
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
                elif ctx.arrayIndex():
                    my_ast = AST.Index()
                    my_ast.set_index(self.visit(ctx.arrayIndex()))
                my_ast.set_positional_child(0, self.visit(ctx.getChild(0)))
                my_ast.set_source_loc(source_from_ctx(ctx))
                return my_ast
            elif ctx.INCR():
                my_ast = AST.IncrPre()
            elif ctx.DECR():
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

        if ctx.CHAR():  # TODO (maybe) multivalue chars
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
        if ctx.STRING():
            my_ast.val = list(ctx.getText()[1:len(ctx.getText())-1])
            # type should really be [char const]
            my_ast.set_type(TypeClass([TypeComponents.CHAR, TypeComponents.ARR], [None, len(my_ast.val)]))

        my_ast.set_source_loc(source_from_ctx(ctx))
        return my_ast

    def visitArrayLit(self, ctx: GrammarParser.ArrayLitContext):  # not very type-safe at all (nor safe in general)
        my_ast = AST.Literal(value=[])

        element = None
        for child in ctx.literal():
            element = self.visit(child)
            my_ast.get_value().append(element.get_value())
        my_type: TypeClass = deepcopy(element.get_type())
        my_type.pushType(TypeComponents.ARR)
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
        decl_info = self.extract_decl(ctx.pureDecl())
        var = AST.Variable(decl_info[0])
        var.set_source_loc(source_from_ctx(ctx))
        my_ast.add_child(var)

        self._current_sym_table[decl_info[0]] = VarEntry(decl_info[1], None)

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
        my_ast = AST.Printf(ctx.getChild(2).getText())
        my_ast.set_source_loc(source_from_ctx(ctx))
        for index in range(1, ctx.getChildCount()):
            if isinstance(ctx.getChild(index), GrammarParser.ExprContext):
                my_ast.add_child(self.visit(ctx.getChild(index)))
            pass
        return my_ast

    def visitScanf(self, ctx):
        my_ast = AST.Scanf(ctx.getChild(2).getText())
        my_ast.set_source_loc(source_from_ctx(ctx))
        for index in range(1, ctx.getChildCount()):
            if isinstance(ctx.getChild(index), GrammarParser.ExprContext):
                my_ast.add_child(self.visit(ctx.getChild(index)))
            pass
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

    def visitFunctionDef(self, ctx: GrammarParser.FunctionDefContext):
        decl = self.visitFunctionDecl(ctx.functionDecl())
        my_ast = AST.FunctionDefinition(decl.get_name())
        my_ast.set_source_loc(source_from_ctx(ctx))

        self.enter_scope(my_ast)

        # add definitions of arguments
        for child_nr in range(decl.get_child_count()):
            var: AST.Variable = decl.get_child(child_nr).get_child(0)
            self._current_sym_table[var.get_name()] = var.get_st_entry()
        my_ast.swap_children(decl)

        # make function body
        my_ast.add_child(self.visit(ctx.stateOrScope()), 0)

        self.exit_scope(my_ast)

        # add function to ST
        # self._current_sym_table[my_ast.get_name()] = decl.get_st_entry()
        # due to weird way st works w/ "current symbol table", the entry is already there

        return my_ast

    def visitFunctionDecl(self, ctx: GrammarParser.FunctionDeclContext):
        decl_info_list = [self.extract_decl(ctx.pureDecl(i)) for i in range(len(ctx.pureDecl()))]

        my_ast = AST.FunctionDeclaration(decl_info_list[0][0])
        my_ast.set_source_loc(source_from_ctx(ctx))

        # set type & arg_count of function
        my_st_entry = FuncEntry(decl_info_list[0][1])
        my_st_entry.arg_count = len(decl_info_list)-1

        self.enter_scope(my_ast)

        # add variable decls for each argument & add arguments info to function's st entries
        for arg_nr in range(1, len(decl_info_list)):
            arg_ctx = ctx.pureDecl(arg_nr)
            arg = AST.Variable(decl_info_list[arg_nr][0])
            arg.set_source_loc(source_from_ctx(arg_ctx))
            decl = AST.Decl()
            decl.set_source_loc(source_from_ctx(arg_ctx))
            decl.add_child(arg)
            my_ast.add_child(decl)
            self._current_sym_table[arg.get_name()] = VarEntry(decl_info_list[arg_nr][1])
            my_st_entry.arg_types.append(decl_info_list[arg_nr][1])

        self.exit_scope(my_ast)

        # save function's st entry
        self._current_sym_table[decl_info_list[0][0]] = my_st_entry
        return my_ast

    def visitReturnStatement(self, ctx: GrammarParser.ReturnStatementContext):
        my_ast = AST.ReturnStatement()
        my_ast.set_source_loc(source_from_ctx(ctx))
        if ctx.getChildCount() > 1:
            my_ast.add_child(self.visit(ctx.getChild(1)))
        else:
            void = AST.Literal(value=None)
            void.set_source_loc(source_from_ctx(ctx))
            void.set_type(TypeClass([TypeComponents.VOID]))
            my_ast.add_child(void)
        return my_ast
