import sys
from antlr4 import *
from src.antlr.MathLexer import MathLexer
from src.antlr.MathParser import MathParser
from src.CSTVisitor import CSTVisitor
from src.ASTDotVisitor import ASTDotVisitor

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MathLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MathParser(stream)
    tree = parser.doc()

    visitor = CSTVisitor()
    AST = visitor.visit(tree)
    dot = ASTDotVisitor.visit(AST)

    pass


if __name__ == '__main__':
    main(sys.argv)
