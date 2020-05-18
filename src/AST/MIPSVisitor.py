from src.AST import AST
from src.AST.Visitor import Visitor
from termcolor import colored, cprint
from src.utility.TypeClass import TypeClass
from io import StringIO

def get_math_instruction(op:AST.MathOp, floating: bool):

    # if floating:
    #     op_str = ' f'
    # else:
    #     op_str = ''
    op_str = ''
    op_com = 'error in get_math_instruction'

    if isinstance(op, AST.Sum):
        op_str += 'addu '
        op_com = ' + '
    elif isinstance(op, AST.Sub):
        op_str += 'subu '
        op_com = ' - '
    elif isinstance(op, AST.Prod):
        op_str += 'mulu '
        op_com = ' * '
    elif isinstance(op, AST.Div):
        pass
        # if op_str == ' f': op_str = ' fdiv '
        # else: op_str += 'sdiv '
        # op_com = ' / '
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
        if node_type[a] == ']':
            break
        if node_type[a] == '*':
            ptr_depth += 1

    for i in range(int(ptr_depth)):
        base += '*'
    return base

def to_array_type(node_type: str, farg = False):
    node_type = node_type[1:len(node_type)-1]
    strs = node_type.split('x')
    strs[0] = strs[0][0:len(strs[0])-1]
    if farg:
        return to_base_type(strs[0]) + '*'
    base = '[' + strs[1] + ' x '
    base += to_base_type(strs[0])
    return check_for_pointers(strs[0], base) + ']'

def to_base_type(node_type):
    if node_type[0:3] == 'int':
        return 'i32'
    elif node_type[0:5] == 'float':
        return 'float'
    elif node_type[0:4] == 'char':
        return 'i8'
    elif node_type[0:4] == 'bool':
        return 'i1'

def to_llvm_type(node, farg = False) -> str:
    node_type = node.get_type().__repr__()

    base = ''
    if node_type == 'void':
        base = 'void'
    elif node_type[0] == '[':
        base += to_array_type(node_type, farg)
    else:
        base += to_base_type(node_type)

    llvm_type = check_for_pointers(node_type, base)
    return llvm_type

def get_constant(type_of):
    if type_of == 'i32' or type_of == 'i8':
        return '0'
    elif type_of == 'float':
        return '0.0'
    elif type_of[0] == '[':
        return "zeroinitializer"
    elif is_pointer(type_of):
        return "null"
    else:
        print("oof")

def is_pointer(type_of):
    return type_of[len(type_of)-1] == '*'

class MIPSVisitor(Visitor):
    file = None
    _rcounter = 0 # counter to keep track of registers used
    _lcounter = 0 # counter to keep track of labels used
    _scounter = 0 # counter to keep track of strings used
    _offset = 0
    _tcounter = 0
    exit_label_stack = []
    begin_label_stack = []
    scope_counter = 0

    def __init__(self, file):
        self.header_buf = StringIO()
        self.body_buf = StringIO()
        self.print_to_header(" .text")
        self.print_to_header(".globl main")
        self.file = file

    # HELPER FUNCTIONS
    def print_to_file(self, string, comment=None, ws_str ='\n', ws_comment='\n', modifier = 0):
        for a in range(self.scope_counter + modifier):
            ws_str += '\t'
            ws_comment += '\t'
        # self.body_buf.write(ws_comment + '# ' + comment)
        self.body_buf.write(ws_str + string)

    def print_to_header(self, string):
        self.header_buf.write('\n' + string)

    def close(self):
        self.file.write(self.header_buf.getvalue() + '\n')
        self.file.write(self.body_buf.getvalue() + '\n')
        self.file.close()

    def get_rname(self) -> str:
        self._rcounter += 1
        return '%t' + str(self._rcounter)
    
    # TODO multiple types
    def incr_offset(self):
        self._offset -= 4
        return self._offset

    def reset_offset(self):
        self._offset = -4

    def get_treg(self):
        self._tcounter += 1
        if self._tcounter > 8:
            print("max temp registers reached")
        return '$t' + str(self._tcounter-1)

    def reset_treg(self):
        self._tcounter = 0

    def get_lname(self) -> str:
        self._lcounter += 1
        return 'l' + str(self._lcounter)

    def get_strname(self) -> str:
        self._scounter += 1
        return '@.str.' + str(self._scounter)

    def get_register_of(self, ast: AST.Component):
        if isinstance(ast, AST.Index):
            reg = self.get_rname()
            self.gen_getelemntptr_offset(reg, to_llvm_type(ast.get_child(0)), ast.get_child(0).get_register(), 0, self.get_value_of(ast.get_child(1)))
            return reg
        return ast.get_register()

    def get_value_of(self, ast: AST.Component):
        reg = self.get_treg()
        self.gen_load(reg, ast.get_offset())
        return reg


    # GENERATOR FUNCTIONS
    def print_label(self, label, label_comment):
        self.body_buf.write('\n\n# ' + label_comment)
        self.body_buf.write('\n' + label + ':')
        return label

    def gen_load(self, reg, offset):
        comment = 'load '
        string = 'lw ' + reg + ', ' + str(offset) + '($fp)'
        self.print_to_file(string, comment)

    def gen_load_im(self, reg, value):
        comment = 'load '
        string = 'li ' + reg + ', ' + str(value)
        self.print_to_file(string, comment)

    def gen_store(self, value, offset):
        comment = 'store '
        string = 'sw ' + str(value) + ', ' + str(offset)  + '($fp)'
        self.print_to_file(string, comment)

    def gen_binary_instruction(self, res, lhs, rhs, op_str, op_com):
        comment = res + ' = ' + str(lhs) + op_com + str(rhs)
        string = op_str + res + ', ' + str(lhs) + ', ' + str(rhs)
        self.print_to_file(string, comment)

    def gen_not(self, res, lhs, type_of):
        comment = res + ' = ' + str(lhs) + ' xor 1'
        string = res + ' = xor ' + type_of + ' ' + str(lhs) + ', 1'
        self.print_to_file(string, comment)

    def gen_math_instr(self, res, lhs, rhs, type_of, op: AST.MathOp):
        op_str, op_com = get_math_instruction(op, type_of == 'float')
        self.gen_binary_instruction(res, lhs, rhs, op_str, op_com)

    def gen_comp_instr(self, res, lhs, rhs, type_of, op: AST.CompOp):
        op_str, op_com = get_comp_instruction(op, type_of == 'float')
        self.gen_binary_instruction(res, lhs, rhs, type_of, op_str, op_com)

    def gen_logic_instr(self, res, lhs, rhs, type_of, op: AST.LogicOp):
        op_str, op_com = get_logic_instruction(op)
        self.gen_binary_instruction(res, lhs, rhs, type_of, op_str, op_com)

    #   %12 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([11 x i8], [11 x i8]* @.str, i32 0, i32 0), i32 %7, i32 %9, i32 %11)
    def gen_printf(self, meta_size, str_name, args):
        comment = 'print'
        string = self.get_rname() + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([" + str(meta_size) \
                 + " x i8],[" + str(meta_size) + " x i8]* " + str_name + ",i32 0, i32 0)"
        for arg in args:
            if (arg[0]) == 'float':
                c_reg = self.get_rname()
                self.gen_fpext(c_reg, 'float', 'double', str(arg[1]))
                string += ', ' + 'double'+ " " + c_reg
            else:
                string += ', ' + str(arg[0]) + " " + str(arg[1])

        string += ")"
        self.print_to_file(string, comment)

    #   %4 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str, i32 0, i32 0), i8* %3)
    def gen_scanf(self, meta_size, str_name, args):
        comment = 'scan'
        string = self.get_rname() + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([" + str(meta_size) \
                 + " x i8],[" + str(meta_size) + " x i8]* " + str_name + ",i32 0, i32 0)"
        for arg in args:
            if (to_llvm_type(arg)) == 'float':
                c_reg = self.get_rname()
                self.gen_fpext(c_reg, 'float', 'double', str(self.get_value_of(arg)))
                string += ', ' + 'double'+ " " + c_reg
            else:
                string += ', ' + str(to_llvm_type(arg)) + " " + str(self.get_value_of(arg))

        string += ")"
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

    def gen_getelemntptr_offset(self, reg, type_of, base_ptr, base = None, offset=None):
        comment = 'get value stored at ' + base_ptr + ' at base ' + str(base) + ' + offset' + str(offset)
        string = reg + ' = getelementptr ' + type_of + ', ' + type_of + '* ' + base_ptr + ', i32 ' + str(base) + ', i32 ' + str(offset)
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
        self.reset_offset()
        self.print_label(name, "define function " + name)


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
        pass
        # comment = 'return register ' + str(reg)
        # string = "ret " + rtype + ' ' + str(reg)
        # self.print_to_file(string, comment)

    def gen_void_return(self):
        self.print_to_file("ret void", "return void")

    def gen_str_constant(self, meta: str, meta_size):
        name = self.get_strname()
        self.print_to_header(name + ' = private unnamed_addr constant [' + str(meta_size) + ' x i8] c' + meta)
        return name

    def gen_default_return(self, rtype):
        if (rtype[0:4] == 'void'):
            self.gen_void_return()
            return
        constant = get_constant(rtype)
        self.gen_return_statement(rtype, constant)
        pass

    def gen_global_var_assign(self, ast: AST.AssignOp):
        var: AST.Variable = ast.get_child(0).get_child(0)
        var.set_register('@' + var.get_name())
        string = '@' + var.get_name() + ' = global ' + to_llvm_type(var) + ' ' + str(self.get_value_of(ast.get_child(1)))
        self.print_to_header(string)

    def gen_global_var_decl(self, ast: AST.Decl):
        var: AST.Variable = ast.get_child(0)
        var.set_register('@' + var.get_name())
        string = '@' + var.get_name() + ' = global ' + to_llvm_type(var) + ' ' + get_constant(to_llvm_type(var))
        self.print_to_header(string)

    # VISITOR FUNCTIONS
    def visitComposite(self, ast: AST.Composite):
        self.visitChildren(ast)

    def visitLiteral(self, ast: AST.Literal):
        self.reset_treg()
        reg = self.get_treg()
        self.gen_load_im(reg, ast.get_value())
        offset = self.incr_offset()
        ast.set_offset(offset)
        self.gen_store(reg,offset)

    def visitDecl(self, ast: AST.Decl):
        # TODO
        # if self.scope_counter == 0:
        #     self.gen_global_var_decl(ast)
        #     return
        var: AST.Variable = ast.get_child(0)
        var.set_offset(self.incr_offset())

    def visitAssignOp(self, ast: AST.AssignOp):
        # TODO
        # if self.scope_counter == 0:
        #     self.gen_global_var_assign(ast)
        #     return

        self.visitChildren(ast)
        # assignment could also be a definition
        if isinstance(ast.get_child(0), AST.Decl):
            var: AST.Variable = ast.get_child(0).get_child(0)
        else:
            var: AST.Variable = ast.get_child(0)

        self.gen_store(self.get_value_of(ast.get_child(1)), var.get_offset())

    def visitPrintf(self, ast: AST.Printf):  #
        self.visitChildren(ast)
        str_name = self.gen_str_constant(ast.get_meta(), ast.get_meta_size())
        args = []
        for i in range(ast.get_child_count()):
            args.append([to_llvm_type(ast.get_child(i)), self.get_value_of(ast.get_child(i))])
        self.gen_printf(ast.get_meta_size(), str_name, args)

    def visitScanf(self, ast: AST.Scanf):  #
        self.visitChildren(ast)
        str_name = self.gen_str_constant(ast.get_meta(), ast.get_meta_size())
        self.gen_scanf(ast.get_meta_size(), str_name, ast._children)


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

    def visitNot(self, ast: AST.Not):
        self.visitChildren(ast)
        var_reg = self.get_value_of(ast.get_child(0))
        reg = self.get_rname()
        ast.set_register(reg)
        self.gen_not(reg, var_reg, to_llvm_type(ast.get_child(0)))

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
            self.gen_comp_instr(reg, var_reg, 0, 'i32', AST.NotEqual())
        elif ast.get_conversion_type() == AST.conv_type.INT_TO_FLOAT:
            self.gen_sitofp(reg, 'i32', 'float', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.BOOL_TO_INT:
            self.gen_zext(reg, 'i1', 'i32', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.BOOL_TO_FLOAT:
            self.gen_uitofp(reg, 'i1', 'float', var_reg)
        elif ast.get_conversion_type() == AST.conv_type.FLOAT_TO_BOOL:
            self.gen_comp_instr(reg, var_reg, 0.0, 'float', AST.NotEqual())
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
            self.gen_comp_instr(reg, var_reg, 0, 'i8', AST.NotEqual())
        elif ast.get_conversion_type() == AST.conv_type.CHAR_TO_INT:
            self.gen_zext(reg, 'i8', 'i32', var_reg)


    def visitBinaryOp(self, ast: AST.BinaryOp):
        self.visitChildren(ast)
        reg = self.get_treg()
        lhs, rhs = self.get_value_of(ast.get_child(0)), self.get_value_of(ast.get_child(1))

        if isinstance(ast, AST.LogicOp):
            self.gen_logic_instr(reg, lhs, rhs, to_llvm_type(ast.get_child(0)), ast)
        elif isinstance(ast, AST.MathOp):
            self.gen_math_instr(reg, lhs, rhs, to_llvm_type(ast), ast)
        elif isinstance(ast, AST.CompOp):
            self.gen_comp_instr(reg, lhs, rhs, to_llvm_type(ast.get_child(0)), ast)

        offset = self.incr_offset()
        ast.set_offset(offset)
        self.gen_store(reg, offset)
        self.reset_treg()

    def visitAdress(self, ast: AST.Adress):
        self.visitChildren(ast)
        reg = self.get_rname()
        ast.set_register(reg)
        self.gen_getelementptr(reg, to_llvm_type(ast.get_child(0)), ast.get_child(0).get_register())

    def visitIndir(self, ast: AST.Indir):
        self.visitChildren(ast)
        reg = self.get_rname()
        self.gen_load(reg, self.get_register_of(ast.get_child(0)), to_llvm_type(ast.get_child(0)))
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

    def visitFunctionDeclaration(self, ast: AST.FunctionDeclaration):
        pass

    def visitFunctionDefinition(self, ast: AST.FunctionDefinition):
        self.scope_counter += 1
        args = []
        for a in range(1, ast.get_child_count()):
            self.visit(ast.get_child(a).get_child(0))
            args.append(ast.get_child(a).get_child(0))
        self.cur_func = ast.get_name() # for array definitions
        self.gen_function_def(to_llvm_type(ast), ast.get_name(), args)
        self.visit(ast.get_child(0))

        if not ast.guarantied_return:
            self.gen_default_return(to_llvm_type(ast))

        self.scope_counter -= 1

    def visitReturnStatement(self, ast:AST.ReturnStatement):
        self.visitChildren(ast)
        # if to_llvm_type(ast)[0:4] == 'void':
        #     self.gen_void_return()
        #     return
        # self.gen_return_statement(to_llvm_type(ast), self.get_value_of(ast.get_child(0)))

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