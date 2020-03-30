import sys
import os.path
import copy
from antlr4 import *

run_from = os.path.abspath("./")
if run_from not in sys.path:
    sys.path.append(run_from)


from src.antlr.GrammarLexer import GrammarLexer
from src.antlr.GrammarParser import GrammarParser

from src.AST.Visitor import Visitor as ASTVisitor
from src.AST.AST import Component
from src.utility.SemanticExceptions import SemanticError, SemanticWarning

from src.AST.ConstantFoldingVisitor import ConstantFoldingVisitor
from src.CST.Visitor import Visitor as CSTVisitor
from src.AST.DotVisitor import DotVisitor
from src.AST.LLVMVisitor import LLVMVisitor
from src.AST.TypeVisitor import TypeVisitor
from src.AST.SemanticVisitor import UntypedSemanticVisitor, TypedSemanticsVisitor

from src.AST.DotVisitor import label_big as label_style

# LLVM
# TODO comparison operators
# TODO boolean operators
# TODO floating points afprinten
# TODO pointer types
# TODO constant propagation
# TODO constants


def ast_pass(visitor: ASTVisitor, tree: Component):
    return visitor, visitor.visit(tree)


def ast_error_pass(visitor: ASTVisitor, tree: Component):
    try:
        visitor.visit(tree)
    except SemanticError as oops:
        print(oops.__repr__(), file=sys.stderr)
        exit(1)
    else:
        for error in visitor.errors:
            print(error.__repr__(), file=sys.stderr)
        for warning in visitor.warnings:
            print(warning.__repr__(), file=sys.stderr)
        if len(visitor.errors) > 0:
            exit(1)


def ast_visualise(ast: Component, filename: str, style=label_style):
    graph = ast_pass(DotVisitor(style), ast)[0].graph
    graph.write(filename + ".dot")
    graph.write_png(filename + ".png")


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)

    parser = GrammarParser(stream)
    tree = parser.doc()

    fname = argv[1][0:(len(argv[1]) - 2)]

    if parser.getNumberOfSyntaxErrors() != 0:
        exit(1)

    visitor = CSTVisitor()
    ast = visitor.visit(tree)

    # ast_error_pass(UntypedSemanticVisitor(), ast)

    ast_error_pass(TypeVisitor(), ast)

    # ast_error_pass(TypedSemanticsVisitor(), ast)

    if len(argv) == 3:
        if argv[2] == '-cf':
            ast_pass(ConstantFoldingVisitor(), ast)

    ast_visualise(ast, fname, label_style)
    tfile = open(fname + '.ll', 'w+')
    llvm = LLVMVisitor(tfile)
    llvm.visit(ast)
    llvm.close()


if __name__ == '__main__':
    main(sys.argv)
