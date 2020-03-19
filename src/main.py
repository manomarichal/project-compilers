import sys
import copy
from antlr4 import *

from src.antlr.GrammarLexer import GrammarLexer
from src.antlr.GrammarParser import GrammarParser

from src.AST.Visitor import Visitor as ASTVisitor
from src.AST.AST import Component
from src.utility.SemanticExceptions import SemanticError, SemanticWarning

from src.AST.CFVisitor import CFVisitor
from src.CST.Visitor import Visitor as CSTVisitor
from src.AST.DotVisitor import DotVisitor
from src.AST.LLVMVisitor import LLVMVisitor
from src.AST.TypeVisitor import TypeVisitor
from src.AST.SemanticVisitor import UntypedSemanticVisitor, TypedSemanticsVisitor

from src.AST.DotVisitor import label_big as label_style
from src.utility.SemanticExceptions import ImplicitConversionWarning

# LLVM
#TODO comparison operators
#TODO boolean operators
#TODO floating points afprinten
#TODO pointer types
#TODO constant propagation
#TODO constants

tmp_errors = [ImplicitConversionWarning]


def ast_pass(visitor: ASTVisitor, tree: Component):
    return visitor, visitor.visit(tree)


def ast_error_pass(visitor: ASTVisitor, tree: Component):
    try:
        visitor.visit(tree)
    except SemanticError as oops:
        print(oops.__repr__(), file=sys.stderr)
        exit(1)
    else:
        hit_tmp_error = False
        for error in visitor.errors:
            print(error.__repr__(), file=sys.stderr)
        for warning in visitor.warnings:
            print(warning.__repr__(), file=sys.stderr)
            for tmp_error in tmp_errors:
                if isinstance(warning, tmp_error):
                    hit_tmp_error = True
                    print("^^ UNSUPPORTED WARNING ^^", file=sys.stderr)
        if len(visitor.errors) > 0:
            exit(1)
        if hit_tmp_error:
            print("Terminating because of currently unsupported warnings", file=sys.stderr)
            exit(1)


def ast_visualise(ast: Component, filename: str, style):
    graph = ast_pass(DotVisitor(style), ast)[0].graph
    graph.write(filename + ".dot")
    graph.write_png(filename + ".png")


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.doc()
    visitor = CSTVisitor()
    ast = visitor.visit(tree)

    ast_error_pass(UntypedSemanticVisitor(), ast)

    ast_error_pass(TypeVisitor(), ast)

    ast_error_pass(TypedSemanticsVisitor(), ast)

    ast_visualise(ast, "./test_IO/typed", label_style)

    # ast_pass(CFVisitor(), ast)

    fname = argv[1][0:(len(argv[1]) - 1)]

    ast_visualise(ast, fname, label_style)

    tfile = open(fname + 'll', 'w+')
    llvm = LLVMVisitor(tfile)
    llvm.visit(ast)
    llvm.close()


if __name__ == '__main__':
    main(sys.argv)
