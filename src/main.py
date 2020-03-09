import sys
import copy
from antlr4 import *
from src.antlr.GrammarLexer import GrammarLexer
from src.antlr.GrammarParser import GrammarParser
from src.ST.CSTVisitor import CSTVisitor
from src.ST.ASTDotVisitor import ASTDotVisitor


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.doc()

    visitor = CSTVisitor()
    ast = visitor.visit(tree)

    astCF = ASTCFVisitor()
    astCF.visit(ast)

    astVisualiser = ASTDotVisitor()
    astVisualiser.visit(ast)
    astVisualiser.graph.write("test_IO/result.dot")
    astVisualiser.graph.write_png("test_IO/result.png")

if __name__ == '__main__':
    main(sys.argv)
