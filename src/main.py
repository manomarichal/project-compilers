import sys
import copy
from antlr4 import *

from src.AST.CFVisitor import CFVisitor
from src.antlr.GrammarLexer import GrammarLexer
from src.antlr.GrammarParser import GrammarParser
from src.CST.Visitor import Visitor as CSTVisitor
from src.AST.DotVisitor import DotVisitor
from src.AST.SemanticVisitor import SemanticVisitor
from src.AST.LLVMVisitor import LLVMVisitor

# Mandatory
# P2
#TODO semantic erros -> zo (J)
#TODO syntax errors -> zo (J)
#TODO pointer operators & assigment (LVAL vs RVAL) -> zo (M)
#TODO pointer grammar -> ma (M)
#TODO pointer semantic errors -> deadline
#TODO constant propagation until next assignment -> zo

# P3
#TODO printf() -> ma
#TODO to LLVM -> ma
#TODO scripts + readme + verslag -> deadline

# Optional

#TODO ++--
#TODO implicit not python conversions
#TODO dont ignore comments
#TODO comment after every instruction


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.doc()

    visitor = CSTVisitor()
    ast = visitor.visit(tree)

    semantic_checker = SemanticVisitor()
    semantic_checker.visit(ast)

    constant_folding = CFVisitor()
    constant_folding.visit(ast)

    llvm = LLVMVisitor()
    llvm.visit(ast)

    astVisualiser = DotVisitor()
    astVisualiser.visit(ast)
    astVisualiser.graph.write("test_IO/result.dot")
    astVisualiser.graph.write_png("test_IO/result.png")

if __name__ == '__main__':
    main(sys.argv)
