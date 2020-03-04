import sys
from antlr4 import *
from antlr.MathLexer import MathLexer
from antlr.MathParser import MathParser
from ST.CSTVisitor import CSTVisitor
from ST.ASTDotVisitor import ASTDotVisitor


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MathLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MathParser(stream)
    tree = parser.doc()

    visitor = CSTVisitor()
    ast = visitor.visit(tree)

    astVisualiser = ASTDotVisitor()
    astVisualiser.visit(ast)
    astVisualiser.graph.write("test_IO/result.dot")


if __name__ == '__main__':
    main(sys.argv)
