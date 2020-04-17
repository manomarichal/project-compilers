from src.AST import AST
from src.AST.Visitor import Visitor
from termcolor import colored, cprint
from src.utility.TypeClass import TypeClass
from io import StringIO

def get_math_instruction(op:AST.MathOp, floating: bool):

    if floating:
        op_str = ' f'
    else:
        op_str = ' '

    op_com = 'error in get_math_instruction'

    if isinstance(op, AST.Sum):
        op_str += 'add '
        op_com = ' + '
    elif isinstance(op, AST.Sub):
        op_str += 'sub '
        op_com = ' - '
    elif isinstance(op, AST.Prod):
        op_str += 'mul '
        op_com = ' * '
    elif isinstance(op, AST.Div):
        if op_str == ' f': op_str = ' fdiv '
        else: op_str += 'sdiv '
        op_com = ' / '
    elif isinstance(op, AST.Mod):
        if op_str == ' f': op_str = ' frem '
        else: op_str += 'srem '
        op_com = ' % '

    return op_str, op_com

def get_comp_instruction(op:AST.CompOp, floating: bool):

    if floating:
        op_str = ' fcmp '
    else:
        op_str = ' icmp '

    op_com = 'error in get_comp_instruction'

    if isinstance(op, AST.More):
        if floating:
            op_str += 'ogt '
        else:
            op_str += 'sgt '
        op_com = ' > '
    elif isinstance(op, AST.MoreE):
        if floating:
            op_str += 'oge '
        else:
            op_str += 'sge '
        op_com = ' >= '
    elif isinstance(op, AST.Less):
        if floating:
            op_str += 'olt '
        else:
            op_str += 'slt '
        op_com = ' < '
    elif isinstance(op, AST.LessE):
        if floating:
            op_str += 'ole '
        else:
            op_str += 'sle '
        op_com = ' <= '
    elif isinstance(op, AST.Equal):
        if floating:
            op_str += 'oeq '
        else:
            op_str += 'eq '
        op_com = ' == '
    elif isinstance(op, AST.NotEqual):
        if floating:
            op_str += 'one '
        else:
            op_str += 'ne '
        op_com = ' != '

    return op_str, op_com

def get_logic_instruction(op:AST.LogicOp):

    op_com = 'error in get_logic_instruction'
    op_str = ''

    if isinstance(op, AST.And):
        op_str += ' and '
        op_com = ' and '
    elif isinstance(op, AST.Or):
        op_str += ' or '
        op_com = ' or '

    return op_str, op_com

def check_for_pointers(node_type, base):
    ptr_depth = 0
    for a in range(len(node_type)-1, -1, -1):
        if node_type[a] == '*':
            ptr_depth += 1

    for i in range(int(ptr_depth)):
        base += '*'
    return base

def to_array_type(node_type):
    base = '[' + node_type[len(node_type)-1] + ' x '
    base += to_base_type(node_type[1:]) + ']'
    return base

def to_base_type(node_type):
    if node_type[0:3] == 'int':
        return 'i32'
    elif node_type[0:5] == 'float':
        return 'float'
    elif node_type[0:4] == 'char':
        return 'i8'
    elif node_type[0:4] == 'bool':
        return 'i1'

def to_llvm_type(node) -> str:
    node_type = node.get_type().__repr__()

    base = ''
    if node_type == 'void':
        base = 'void'
    elif node_type[0] == '[':
        base += to_array_type(node_type)
    else:
        base += to_base_type(node_type)

    llvm_type = check_for_pointers(node_type, base)
    return llvm_type

class LLVMVisitor(Visitor):
    file = None
    _rcounter = 0 # counter to keep track of registers used
    _lcounter = 0 # counter to keep track of labels used
    exit_label_stack = []
    begin_label_stack = []

    def __init__(self, file):
        self.header_buf = StringIO()
        self.file = file
        self.header_buf.write("declare i32 @printf(i8*, ...)")
        self.header_buf.write("\n@istr = private constant [4 x i8] c\"%d\\0A\\00\"")
        self.header_buf.write("\n@fstr = private constant [4 x i8] c\"%f\\0A\\00\"")
        self.file.write(self.header_buf.getvalue() + '\n')

    # HELPER FUNCTIONS
    def print_to_file(self, string, comment=None, ws_str ='\n\t\t', ws_comment='\n\t'):
        self.file.write(ws_comment + '; ' + comment)
        self.file.write(ws_str + string)

    def close(self):
        self.file.close()

    def get_rname(self) -> str:
        self._rcounter += 1
        return '%t' + str(self._rcounter)

    def get_lname(self) -> str:
        self._lcounter += 1
        return 'l' + str(self._lcounter)

    def get_register_of(self, ast: AST.Component):
        if isinstance(ast, AST.Index):
            reg = self.get_rname()
            self._getelemntptr_array(reg, to_llvm_type(ast.get_child(0)), ast.get_child(0).get_register(), 0, ast.get_child(1).get_value())
            return reg
        return ast.get_register()

    def get_value_of(self, ast: AST.Component):
        # variables have to be loaded in before being used
        if isinstance(ast, AST.Variable) or isinstance(ast, AST.Indir):
            reg = self.get_rname()
            self.gen_load(reg, ast.get_register(), to_llvm_type(ast))
            return reg
        elif isinstance(ast, AST.Index):
            reg1 = self.get_rname()
            reg2 = self.get_rname()
            self.gen_getelemntptr_array(reg1, to_llvm_type(ast.get_child(0)), ast.get_child(0).get_register(), 0, self.get_value_of(ast.get_child(1)))
            self.gen_load(reg2, reg1, to_llvm_type(ast))
            return reg2
        else:
            return ast.get_register()

    # GENERATOR FUNCTIONS
    def print_label(self, label, label_comment):
        self.file.write('\n\n; ' + label_comment)
        self.file.write('\n' + label + ':')
        return label

    def gen_alloca(self, reg, type):
        comment = 'allocate ' + reg
        string = reg + ' = alloca ' + type
        self.print_to_file(string, comment)

    def gen_load(self, reg, ptr, type_of):
        comment = 'load ' + ptr + ' in ' + reg
        string = reg + ' = load ' + type_of + ', ' + type_of + '* ' + ptr
        self.print_to_file(string, comment)

    def gen_store(self, value, destination, type_of):
        comment = 'store ' + str(value) + ' in ' + destination
        string = 'store ' + type_of + ' ' + str(value) + ', ' + type_of + '* ' + destination
        self.print_to_file(string, comment)

    def gen_binary_instruction(self, res, lhs, rhs, type_of, op_str, op_com):
        comment = res + ' = ' + str(lhs) + op_com + str(rhs)
        string = res + ' =' + op_str + type_of + ' ' + str(lhs) + ', ' + str(rhs)
        self.print_to_file(string, comment)

    def gen_math_instr(self, res, lhs, rhs, type_of, op: AST.MathOp):
        op_str, op_com = get_math_instruction(op, type_of == 'float')
        self.gen_binary_instruction(res, lhs, rhs, type_of, op_str, op_com)

    def gen_comp_instr(self, res, lhs, rhs, type_of, op: AST.CompOp):
        op_str, op_com = get_comp_instruction(op, type_of == 'float')
        self.gen_binary_instruction(res, lhs, rhs, type_of, op_str, op_com)

    def gen_logic_instr(self, res, lhs, rhs, type_of, op: AST.LogicOp):
        op_str, op_com = get_logic_instruction(op)
        self.gen_binary_instruction(res, lhs, rhs, type_of, op_str, op_com)

    def gen_int_printf(self, reg, type_of):
        comment = 'print ' + str(reg)
        string = self.get_rname() + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @istr,i32 0, i32 0)," + type_of + " " + str(reg) + ")"
        self.print_to_file(string, comment)

    def gen_float_printf(self, reg):
        comment = 'print ' + reg
        string = self.get_rname() + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @fstr,i32 0, i32 0), double " + str(reg) + ")"
        self.print_to_file(string, comment)

    # %X = trunc i32 235 to i1 (%X = 1)
    def gen_trunc(self, reg, from_type, to_type, value):
        comment = 'convert ' + from_type + ' ' + str(value) + ' to ' + to_type
        string = str(reg) + ' = trunc ' + from_type + ' ' + str(value) + ' to ' + to_type
        self.print_to_file(string, comment)

    # %X = zext i1 1 to i32 (%X = 00000..1)
    def gen_zext(self, reg, from_type, to_type, value):
        comment = 'zero extent ' + from_type + ' ' + str(value) + ' to ' + to_type
        string = str(reg) + ' = zext ' + from_type + ' ' + str(value) + ' to ' + to_type
        self.print_to_file(string, comment)

    # %X = fpext float 3.125 to double     ; yields double: 3.125000e+00)
    def gen_fpext(self, reg, from_type, to_type, value):
        comment = 'fp zero extent ' + from_type + ' ' + str(value) + ' to ' + to_type
        string = str(reg) + ' = fpext ' + from_type + ' ' + str(value) + ' to ' + to_type
        self.print_to_file(string, comment)

    # %X = sitofp i32 257 to float         ; yields float:257.0
    def gen_sitofp(self, reg, from_type, to_type, value):
        comment = 'signed int ' + from_type + ' ' + str(value) + ' to ' + to_type
        string = str(reg) + ' = sitofp ' + from_type + ' ' + str(value) + ' to ' + to_type
        self.print_to_file(string, comment)

    # %X = uitofp i32 257 to float         ; yields float:257.0
    def gen_uitofp(self, reg, from_type, to_type, value):
        comment = 'unsigned int ' + from_type + ' ' + str(value) + ' to ' + to_type
        string = str(reg) + ' = uitofp ' + from_type + ' ' + str(value) + ' to ' + to_type
        self.print_to_file(string, comment)

    # %X = fptosi double -123.0 to i32      ; yields i32:-123
    def gen_fptosi(self, reg, from_type, to_type, value):
        comment = 'float ' + from_type + ' ' + str(value) + ' to signed ' + to_type
        string = str(reg) + ' = fptosi ' + from_type + ' ' + str(value) + ' to ' + to_type
        self.print_to_file(string, comment)

    # %X = fptoui double 123.0 to i32      ; yields i32:123
    def gen_fptoui(self, reg, from_type, to_type, value):
        comment = 'float ' + from_type + ' ' + str(value) + ' to unsigned ' + to_type
        string = str(reg) + ' = fptoui ' + from_type + ' ' + str(value) + ' to ' + to_type
        self.print_to_file(string, comment)

    # <result> = getelementptr <ty>, <ty>* <ptrval>{, [inrange] <ty> <idx>}*
    def gen_getelementptr(self, reg, type_of, base_ptr):
        comment = 'get adress of ' + base_ptr
        string = reg + ' = getelementptr ' + type_of + ', ' + type_of + '* ' + base_ptr
        self.print_to_file(string, comment)

    def gen_getelemntptr_array(self, reg, type_of, base_ptr, base = None, offset=None):
        comment = 'get value stored at ' + base_ptr + ' at base ' + str(base) + ' + offset' + str(offset)
        string = reg + ' = getelementptr ' + type_of + ', ' + type_of + '* ' + base_ptr + ', i64 ' + str(base) + ', i64 ' + str(offset)
        self.print_to_file(string, comment)

    def gen_branch_uncon(self, label1): # unconditional branch
        comment = 'branch to ' + label1
        string = 'br label %' + label1
        self.print_to_file(string, comment)

    def gen_branch_con(self, label1, label2, reg): # conditional branch
        comment = 'branch to ' + label1 + ' if ' + reg + ' is true, else branch to ' + label2
        string = 'br i1 ' + reg + ', label %' + label1 + ', label %' + label2
        self.print_to_file(string, comment)

    def gen_function_def(self, rtype, name, args):
        comment = 'define function ' + name
        string = "define " + rtype + ' @' + name + '('

        for a in range(len(args)):
            if a != 0:
                string += ', '
            string += to_llvm_type(args[a])
        string += ') {'
        self.print_to_file(string, comment,'\n', '\n\n')

        for a in range(len(args)):
            # allocate a register for the function argument
            arg_reg = '%a' + str(a)
            self.gen_alloca(arg_reg, to_llvm_type(args[a]))

            # update the symbol table entry for that function argument
            args[a].set_register(arg_reg)

            # store the function argument in the reserved register
            self.gen_store('%' + str(a), arg_reg, to_llvm_type(args[a]))

    def gen_function_call(self, reg, rtype, name, args):
        if rtype[0:4] == 'void':
            comment = 'call function ' + name
            string = 'call void' + ' @' + name + '('
        else:
            comment = 'call function ' + name + ' in ' + reg
            string = reg + ' = call '+ rtype + ' @' + name + '('

        for a in range(len(args)):
            if a != 0:
                string += ', '
            string += to_llvm_type(args[a]) + ' ' + str(self.get_value_of(args[a]))
        string += ')'
        self.print_to_file(string, comment)

    def gen_return_statement(self, rtype, reg):
        comment = 'return register ' + str(reg)
        string = "ret " + rtype + ' ' + str(reg)
        self.print_to_file(string, comment)

    def gen_void_return(self):
        self.print_to_file("ret void", "return void")

    # VISITOR FUNCTIONS
    def visitComposite(self, ast: AST.Composite):
        self.visitChildren(ast)

    def visitDecl(self, ast: AST.Decl):
        var: AST.Variable = ast.get_child(0)
        var.set_register(self.get_rname())
        self.gen_alloca(var.get_register(), to_llvm_type(var))

    def visitAssignOp(self, ast: AST.AssignOp):
        self.visitChildren(ast)

        # assignment could also be a definition
        if isinstance(ast.get_child(0), AST.Decl):
            var: AST.Variable = ast.get_child(0).get_child(0)
        else:
            var: AST.Variable = ast.get_child(0)

        self.gen_store(self.get_value_of(ast.get_child(1)), self.get_register_of(var), to_llvm_type(var))

    def visitPrintf(self, ast: AST.Printf):  #
        self.visitChildren(ast)
        reg = self.get_value_of(ast.get_child(0))

        if to_llvm_type(ast.get_child(0)) != 'float':
            self.gen_int_printf(reg, to_llvm_type(ast.get_child(0)))
        else:
            # we first need to convert the float for a double (because reasons)
            c_reg = self.get_rname()
            self.gen_fpext(c_reg, 'float', 'double', reg)
            self.gen_float_printf(c_reg)

    def visitIncrPre(self, ast: AST.IncrPre):
        self.visitChildren(ast)
        reg = self.get_rname()
        ast.set_register(reg)
        self.gen_math_instr(reg, self.get_value_of(ast.get_child(0)), 1, to_llvm_type(ast), AST.Sum())
        self.gen_store(reg,self.get_register_of(ast.get_child(0)), to_llvm_type(ast.get_child(0)))

    def visitIncrPost(self, ast: AST.IncrPost):
        self.visitChildren(ast)
        reg = self.get_value_of(ast.get_child(0))
        reg2 = self.get_rname()
        ast.set_register(reg)
        self.gen_math_instr(reg2, reg , 1, to_llvm_type(ast), AST.Sum())
        self.gen_store(reg2, self.get_register_of(ast.get_child(0)), to_llvm_type(ast.get_child(0)))                        # store variable

    def visitDecrPre(self, ast: AST.DecrPre):
        self.visitChildren(ast)
        reg = self.get_rname()
        ast.set_register(reg)
        self.gen_math_instr(reg, self.get_value_of(ast.get_child(0)), 1, to_llvm_type(ast), AST.Sub())
        self.gen_store(reg, self.get_register_of(ast.get_child(0)), to_llvm_type(ast.get_child(0)))                        # store variable

    def visitDecrPost(self, ast: AST.DecrPost):
        self.visitChildren(ast)
        reg = self.get_value_of(ast.get_child(0))
        reg2 = self.get_rname()
        ast.set_register(reg)
        self.gen_math_instr(reg2, reg, 1, to_llvm_type(ast), AST.Sub())
        self.gen_store(reg2, self.get_register_of(ast.get_child(0)), to_llvm_type(ast.get_child(0)))                         # store variable

    def visitNeg(self, ast: AST.Neg):
        self.visitChildren(ast)
        var_reg = self.get_value_of(ast.get_child(0))
        reg = self.get_rname()
        ast.set_register(reg)
        self.gen_math_instr(reg, var_reg, -1, to_llvm_type(ast.get_child(0)), AST.Prod())

    def visitPos(self, ast: AST.Neg):
        self.visitChildren(ast)
        reg = self.get_value_of(ast.get_child(0))
        ast.set_register(reg)

    def visitCastOp(self, ast: AST.CastOp):
        self.visitChildren(ast)
        reg = self.get_rname()
        ast.set_register(reg)
        var_reg = self.get_value_of(ast.get_child(0))

        if ast.get_conversion_type() == AST.conv_type.INT_TO_BOOL:
            self.gen_trunc(reg, 'i32', 'i1', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.INT_TO_FLOAT:
            self.gen_sitofp(reg, 'i32', 'float', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.BOOL_TO_INT:
            self.gen_zext(reg, 'i1', 'i32', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.BOOL_TO_FLOAT:
            self.gen_uitofp(reg, 'i1', 'float', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.FLOAT_TO_BOOL:
            self.gen_fptoui(reg, 'float', 'i1', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.FLOAT_TO_INT:
            self.gen_fptosi(reg, 'float', 'i32', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.FLOAT_TO_CHAR:
            self.gen_fptosi(reg, 'float', 'i8', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.INT_TO_CHAR:
            self.gen_trunc(reg, 'i32', 'i8', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.BOOL_TO_CHAR:
            self.gen_zext(reg, 'i1', 'i8', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.CHAR_TO_FLOAT:
            self.gen_sitofp(reg, 'i8', 'float', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.CHAR_TO_BOOL:
            self.gen_trunc(reg, 'i8', 'i1', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.CHAR_TO_INT:
            self.gen_zext(reg, 'i8', 'i32', var_reg)


    def visitBinaryOp(self, ast: AST.BinaryOp):
        self.visitChildren(ast)
        reg = self.get_rname()
        ast.set_register(reg)
        lhs, rhs = self.get_value_of(ast.get_child(0)), self.get_value_of(ast.get_child(1))

        if isinstance(ast, AST.LogicOp):
            self.gen_logic_instr(reg, lhs, rhs, to_llvm_type(ast.get_child(0)), ast)
        elif isinstance(ast, AST.MathOp):
            self.gen_math_instr(reg, lhs, rhs, to_llvm_type(ast), ast)
        elif isinstance(ast, AST.CompOp):
            self.gen_comp_instr(reg, lhs, rhs, to_llvm_type(ast.get_child(0)), ast)

    def visitAdress(self, ast: AST.Adress):
        self.visitChildren(ast)
        reg = self.get_rname()
        ast.set_register(reg)
        self.gen_getelementptr(reg, to_llvm_type(ast.get_child(0)), ast.get_child(0).get_register())

    def visitIndir(self, ast: AST.Indir):
        self.visitChildren(ast)
        reg = self.get_rname()
        self.gen_load(reg, ast.get_child(0).get_register(), to_llvm_type(ast.get_child(0)))
        ast.set_register(reg)
        pass

    def visitIfStatement(self, ast: AST.IfStatement):
        label_true = self.get_lname()
        label_false = self.get_lname()
        label_end = self.get_lname()

        self.visit(ast.get_child(0))
        if ast.get_child_count() == 3:
            self.gen_branch_con(label_true, label_false, self.get_value_of(ast.get_child(0)))
        else:
            self.gen_branch_con(label_true, label_end, self.get_value_of(ast.get_child(0)))

        self.print_label(label_true, 'if ' + ast.get_child(0).get_register() + ' is true')
        self.visit(ast.get_child(1))
        self.gen_branch_uncon(label_end)

        if ast.get_child_count() == 3:
            self.print_label(label_false, 'if ' + ast.get_child(0).get_register() + ' is false')
            self.visit(ast.get_child(2))
            self.gen_branch_uncon(label_end)

        self.print_label(label_end, 'exit')

    def visitScope(self, ast: AST.Scope):
        self.visitChildren(ast)

    def visitWhileStatement(self, ast: AST.WhileStatement):
        loop_check = self.get_lname()
        loop_body = self.get_lname()
        loop_end = self.get_lname()
        self.begin_label_stack.append(loop_check)
        self.exit_label_stack.append(loop_end)

        self.gen_branch_uncon(loop_check)

        self.print_label(loop_check, 'while header')
        self.visit(ast.get_child(0))
        self.gen_branch_con(loop_body, loop_end, self.get_value_of(ast.get_child(0)))

        self.print_label(loop_body, 'while body')
        self.visit(ast.get_child(1))
        self.gen_branch_uncon(loop_check)

        self.begin_label_stack.pop()
        self.exit_label_stack.pop()
        self.print_label(loop_end, 'exit')

    def visitFunctionDefinition(self, ast: AST.FunctionDefinition):
        args = []
        for a in range(1, ast.get_child_count()):
            self.visit(ast.get_child(a).get_child(0))
            args.append(ast.get_child(a).get_child(0))
        self.cur_func = ast.get_name() # for array definitions
        self.gen_function_def(to_llvm_type(ast), ast.get_name(), args)
        self.visit(ast.get_child(0))
        if (to_llvm_type(ast)[0:4] == 'void'):
            self.gen_void_return()
        self.file.write('\n}')

    def visitReturnStatement(self, ast:AST.ReturnStatement):
        self.visitChildren(ast)
        self.gen_return_statement(to_llvm_type(ast), self.get_value_of(ast.get_child(0)))

    def visitFunctionCall(self, ast:AST.FunctionCall):
        self.visitChildren(ast)
        ast.set_register(self.get_rname())
        args = []
        for a in range(ast.get_child_count()):
            args.append(ast.get_child(a))
        self.gen_function_call(ast.get_register(), to_llvm_type(ast), ast.get_name() ,args)

    def visitForStatement(self, ast: AST.ForStatement):
        loop_check = self.get_lname()
        loop_body = self.get_lname()
        loop_update = self.get_lname()
        loop_end = self.get_lname()

        self.begin_label_stack.append(loop_update)
        self.exit_label_stack.append(loop_end)

        self.visit(ast.get_child(0))
        self.gen_branch_uncon(loop_check)

        self.print_label(loop_check, 'for check')
        self.visit(ast.get_child(1))
        self.gen_branch_con(loop_body, loop_end, self.get_value_of(ast.get_child(1)))

        self.print_label(loop_update, 'for update')
        self.visit(ast.get_child(2))
        self.gen_branch_uncon(loop_check)

        self.print_label(loop_body, 'for body')
        self.visit(ast.get_child(3))
        self.gen_branch_uncon(loop_update)

        self.begin_label_stack.pop()
        self.exit_label_stack.pop()
        self.print_label(loop_end, 'exit')

    def visitBreak(self, ast: AST.Break):
        self.gen_branch_uncon(self.exit_label_stack[-1])

    def visitContinue(self, ast: AST.Continue):
        self.gen_branch_uncon(self.begin_label_stack[-1])