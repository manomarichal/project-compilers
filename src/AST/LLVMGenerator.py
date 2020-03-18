from src.AST import AST
from src.AST.Visitor import Visitor
from termcolor import colored, cprint
import llvmlite.ir as ir

_rcounter = 0

int_type = ir.IntType(32)
float_type = ir.FloatType()
f_int_type = ir.FunctionType(int_type, ())


def to_llvm_type(var) -> str:
    var_type = var.get_type().__repr__()
    if var_type == 'int':
        return int_type
    elif var_type == 'float':
        return 'float'
    elif var_type == 'char':
        return 'i8'
    elif var_type == 'None':
        # TODO literals hebben soms none type
        return 'none'
    else:
        print('invalid type')
        exit(0)


class LLVMVisitor(Visitor):
    main_mod = None
    main_func = None
    builder = None

    def __init__(self):
        self.main_mod = ir.Module('../test_IO/result.ll')
        self.main_func = ir.Function(self.main_mod, f_int_type, name="main")
        block = self.main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    def output(self, file):
        file.write(self.main_mod.__repr__())

    def load_var_in_reg(self, var: AST.Variable):
        reg = self.get_rname()
        return reg

    def get_ir_rep(self, ast: AST.Component):
        if isinstance(ast, AST.Variable):
            return self.builder.load_reg(to_llvm_type(ast), ast.get_register())
        if isinstance(ast, AST.Literal):
            return ir.Constant(to_llvm_type(ast), ast.get_value())

    # VISITOR FUNCTIONS
    def visitComposite(self, ast: AST.Composite):
        self.visitChildren(ast)

    def visitLiteral(self, ast: AST.Literal):
        ast.set_ir_rep(ir.Constant(to_llvm_type(ast), ast.get_value()))

    def visitDecl(self, ast: AST.Decl):
        rname = '%' + ast.get_child(0).get_name()
        ast.get_child(0).set_ir_rep(self.builder.alloca(to_llvm_type(ast), name=rname))

    def visitAssignOp(self, ast: AST.AssignOp):
        self.visitChildren(ast)

        # assignment could also be a definition
        if isinstance(ast.get_child(0), AST.Decl):
            self.builder.store(ast.get_child(1).get_ir_rep(), ast.get_child(0).get_child(0).get_ir_rep())

        elif isinstance(ast.get_child(0), AST.Variable):
            self.builder.store(ast.get_child(1).get_ir_rep(), ast.get_child(0).get_ir_rep())

    def visitMathOp(self, ast: AST.MathOp):
        self.visitChildren(ast)
        lhs = self.get_ir_rep(ast.get_child(0))
        rhs = self.get_ir_rep(ast.get_child(1))

        if isinstance(ast, AST.Sum):
            ast.set_ir_rep(self.builder.fadd(lhs, rhs))
        elif isinstance(ast, AST.Sub):
            ast.set_ir_rep(self.builder.fsub(lhs, rhs))
        elif isinstance(ast, AST.Prod):
            ast.set_ir_rep(self.builder.fmul(lhs, rhs))
        elif isinstance(ast, AST.Div):
            ast.set_ir_rep(self.builder.fdiv(lhs, rhs))
        # TODO mod

    def visitPrintf(self, ast: AST.Printf):  # TODO
        pass









