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

# Mandatory
# P2
#TODO semantic erros -> zo (J)
#TODO syntax errors -> zo (J)
#TODO pointer operators & assigment (LVAL vs RVAL) -> zo (M)
#TODO pointer grammar -> ma (M)
#TODO pointer semantic errors -> deadline
#TODO constant propagation until next assignment -> zo

# P3
#TODO printf()
#TODO to LLVM
#TODO scripts + readme + verslag -> deadline

# Optional

#TODO ++--
#TODO implicit not python conversions
#TODO dont ignore comments
#TODO comment after every instruction


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

    astVisualiser = DotVisitor()
    astVisualiser.visit(ast)
    astVisualiser.graph.write("test_IO/result.dot")
    astVisualiser.graph.write_png("test_IO/result.png")

    tfile = open('./test_IO/result.ll', 'w+')
    llvm = LLVMVisitor(tfile)
    llvm.visit(ast)
    llvm.close()




if __name__ == '__main__':
    main(sys.argv)
