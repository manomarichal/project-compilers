# external libraries
import sys
import copy
from antlr4 import *

# generated ANTLR code
from src.antlr.GrammarLexer import GrammarLexer
from src.antlr.GrammarParser import GrammarParser

# generic compiler code
from src.AST.Visitor import Visitor as ASTVisitor
from src.AST.AST import Component
from src.utility.SemanticExceptions import SemanticError, SemanticWarning

# AST passes
from src.AST.CFVisitor import CFVisitor
from src.CST.Visitor import Visitor as CSTVisitor
from src.AST.DotVisitor import DotVisitor
from src.AST.LLVMVisitor import LLVMVisitor
from src.AST.TypeVisitor import TypeVisitor

# config through import & alias
from src.AST.DotVisitor import label_small as label_style


# Mandatory
# P2
# TODO semantic erros -> zo (J)
# TODO syntax errors -> zo (J)
# TODO pointer operators & assigment (LVAL vs RVAL) -> zo (M)
# TODO pointer grammar -> ma (M)
# TODO pointer semantic errors -> deadline
# TODO constant propagation until next assignment -> zo

# P3
# TODO printf() -> ma
# TODO to LLVM -> ma
# TODO scripts + readme + verslag -> deadline

# Optional
# TODO ++--
# TODO implicit not python conversions
# TODO dont ignore comments
# TODO comment after every instruction


def ast_pass(visitor: ASTVisitor, tree: Component):
    try:
        return visitor, visitor.visit(tree)
    except SemanticError as oops:
        print(oops, sys.stderr)
        exit(1)
    except SemanticWarning as oops:
        print(oops, sys.stderr)



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

    ast_pass(TypeVisitor(), ast)

    ast_pass(CFVisitor(), ast)

    tfile = open('./test_IO/result.ll', 'w+')
    ast_pass(LLVMVisitor(tfile), ast)
    tfile.write('\n}')
    tfile.close()

    visualisation: DotVisitor = ast_pass(DotVisitor(label_style), ast)[0]
    visualisation.graph.write("test_IO/result.dot")
    visualisation.graph.write_png("test_IO/result.png")


if __name__ == '__main__':
    main(sys.argv)
