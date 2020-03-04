import sys
from antlr4 import *
from src.antlr.MathLexer import MathLexer
from src.antlr.MathParser import MathParser
from src.MathCSTVisitor import CustomVisitor

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MathLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MathParser(stream)
    tree = parser.doc()

    visitor = CustomVisitor()
    AST = visitor.visit(tree)
    pass


if __name__ == '__main__':
    main(sys.argv)
