from src.AST import AST
from src.AST.Visitor import Visitor

class LLVMVisitor(Visitor):

    _rcounter = 0

    def _to_llvm_type(ast, var) -> str:
        var_type = var.get_type().__repr__()
        if var_type == 'int':
            return 'i32'
        elif var_type == 'float':
            return 'float'
        elif var_type == 'char':
            return 'i32'
        elif var_type == 'None':
            #TODO literals hebben soms none type
            return 'none'
        else:
            print('invalid type')
            exit(0)

    def _get_rname(self) -> str:
        self._rcounter += 1
        return '%t' + str(self._rcounter)

    def visitComposite(self, ast: AST.Composite):
        self.visitChildren(ast)

    def visitDecl(self, ast: AST.Decl):
        var: AST.Variable = ast.get_child(0)
        comment = 'allocate ' + var.get_name() + ' in ' + var.get_register()

        print('\n// ' + comment)
        print('%' + var.get_name() + ' = alloca ' + self._to_llvm_type(var))

    def visitAssignOp(self, ast:AST.AssignOp):
        self.visitChildren(ast)

        # assignment could also be a definition
        if isinstance(ast.get_child(0), AST.Decl):
            var: AST.Variable = ast.get_child(0).get_child(0)
        else:
            var: AST.Variable = ast.get_child(0)

        reg = '%' + var.get_name()

        print('\n// assign ' + ast.get_child(1).get_register() + ' to ' + reg)
        print(reg + ' = load ' + self._to_llvm_type(var) + '*, ' + str(ast.get_child(1).get_register()))

    def visitSum(self, ast: AST.Sum):
        self.visitChildren(ast)
        ast.set_register(self._get_rname())

    def visitLiteral(self, ast: AST.Literal):
        reg = self._get_rname()
        print('\n// load ' + str(ast.get_value()) + ' in ' + reg)
        print(reg + ' = load ' + self._to_llvm_type(ast) + ', ' + str(ast.get_value()))
        ast.set_register(reg)


    








