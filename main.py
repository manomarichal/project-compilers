import sys
from antlr4 import *
from antlr.MathLexer import MathLexer
from antlr.MathParser import MathParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MathLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MathParser(stream)
    tree = parser.startRule()

if __name__ == '__main__':
    main(sys.argv)