import sys
import copy
from antlr4 import *
from antlr.MathLexer import MathLexer
from antlr.MathParser import MathParser
from ST.CSTVisitor import CSTVisitor
from ST.ASTDotVisitor import ASTDotVisitor
from ST.ASTCFVisitor import ASTCFVisitor


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MathLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MathParser(stream)
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
