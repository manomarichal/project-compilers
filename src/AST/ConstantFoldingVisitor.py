from src.AST import AST
from src.AST.Visitor import Visitor
from src.utility.TypeClass import *


# TODO: incr & decrement (pre & post), addres & indirection, assignment


class ConstantFoldingVisitor(Visitor):
    @staticmethod
    def is_foldable(nodes):
        return all(isinstance(node, AST.Literal) for node in nodes)

    @staticmethod
    def fix_type(val, supposed_type):
        if supposed_type == bool_type:
            return bool(val)
        if supposed_type == char_type:
            return int(val)
        if supposed_type == int_type:
            return int(val)
        if supposed_type == float_type:
            return float(val)
        return val

    def visitLeaf(self, node):
        return node

    def visitComposite(self, node):
        return self.visitChildren(node)

    def full_fold(self, ast: AST.Composite, op):
        children = self.visitChildren(ast)
        if self.is_foldable(children):
            children = [child.get_value() for child in children]
            new_val = op(*children)
            new_val = self.fix_type(new_val, ast.get_type())
            new_lit = AST.Literal(new_val)
            new_lit.set_type(ast.get_type())
            ast.get_parent().replace_child(ast, new_lit)
            return new_lit
        return ast

    def visitPos(self, ast):
        return self.full_fold(ast, lambda a: a)

    def visitNeg(self, ast):
        return self.full_fold(ast, lambda a: -a)

    def visitCastOp(self, ast):
        return self.full_fold(ast, lambda a: a)

    def visitProd(self, ast):
        return self.full_fold(ast, lambda a, b: a*b)

    def visitDiv(self, ast):
        return self.full_fold(ast, lambda a, b: a/b)

    def visitMod(self, ast):
        return self.full_fold(ast, lambda a, b: a % b)

    def visitSum(self, ast):
        return self.full_fold(ast, lambda a, b: a+b)

    def visitSub(self, ast):
        return self.full_fold(ast, lambda a, b: a-b)

    def visitNot(self, ast):
        return self.full_fold(ast, lambda a: not a)

    def visitAnd(self, ast):
        return self.full_fold(ast, lambda a, b: a and b)

    def visitOr(self, ast):
        return self.full_fold(ast, lambda a, b: a or b)

    def visitEqual(self, ast):
        return self.full_fold(ast, lambda a, b: a == b)

    def visitNotEqual(self, ast):
        return self.full_fold(ast, lambda a, b: a != b)

    def visitLess(self, ast):
        return self.full_fold(ast, lambda a, b: a < b)

    def visitLessE(self, ast):
        return self.full_fold(ast, lambda a, b: a <= b)

    def visitMore(self, ast):
        return self.full_fold(ast, lambda a, b: a > b)

    def visitMoreE(self, ast):
        return self.full_fold(ast, lambda a, b: a >= b)
