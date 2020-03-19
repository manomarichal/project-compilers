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

# LLVM
#TODO comparison operators
#TODO boolean operators
#TODO floating points afprinten
#TODO pointer types
#TODO constant propagation

def ast_pass(visitor: ASTVisitor, tree: Component):
    try:
        visitor.visit(tree)
    except SemanticError as oops:
        print(oops, sys.stderr)
        exit(1)

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.doc()
    visitor = CSTVisitor()
    ast = visitor.visit(tree)

    # semantic_checker = SemanticVisitor()
    # semantic_checker.visit(ast)

    assign_types = TypeVisitor()
    assign_types.visit(ast)

    # constant_folding = CFVisitor()
    # constant_folding.visit(ast)

    fname = argv[1][0:(len(argv[1])-1)]
    astVisualiser = DotVisitor()
    astVisualiser.visit(ast)
    astVisualiser.graph.write(fname + "dot")
    astVisualiser.graph.write_png(fname + "png")

    tfile = open(fname + 'll', 'w+')
    llvm = LLVMVisitor(tfile)
    llvm.visit(ast)
    llvm.close()




if __name__ == '__main__':
    main(sys.argv)
