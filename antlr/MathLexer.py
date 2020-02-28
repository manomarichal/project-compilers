# Generated from Math.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("]\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\6\2+\n\2\r\2\16\2,\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\24")
        buf.write("\6\24X\n\24\r\24\16\24Y\3\24\3\24\2\2\25\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25\3\2\4\3\2\62;\5\2\13\f\17\17\"")
        buf.write("\"\2^\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\3*\3\2\2\2\5.\3\2\2\2\7\60\3")
        buf.write("\2\2\2\t\62\3\2\2\2\13\64\3\2\2\2\r\66\3\2\2\2\178\3\2")
        buf.write("\2\2\21:\3\2\2\2\23<\3\2\2\2\25>\3\2\2\2\27@\3\2\2\2\31")
        buf.write("B\3\2\2\2\33E\3\2\2\2\35H\3\2\2\2\37K\3\2\2\2!N\3\2\2")
        buf.write("\2#Q\3\2\2\2%T\3\2\2\2\'W\3\2\2\2)+\t\2\2\2*)\3\2\2\2")
        buf.write("+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-\4\3\2\2\2./\7-\2\2/\6")
        buf.write("\3\2\2\2\60\61\7/\2\2\61\b\3\2\2\2\62\63\7,\2\2\63\n\3")
        buf.write("\2\2\2\64\65\7\61\2\2\65\f\3\2\2\2\66\67\7*\2\2\67\16")
        buf.write("\3\2\2\289\7+\2\29\20\3\2\2\2:;\7=\2\2;\22\3\2\2\2<=\7")
        buf.write("\'\2\2=\24\3\2\2\2>?\7>\2\2?\26\3\2\2\2@A\7@\2\2A\30\3")
        buf.write("\2\2\2BC\7?\2\2CD\7?\2\2D\32\3\2\2\2EF\7>\2\2FG\7?\2\2")
        buf.write("G\34\3\2\2\2HI\7@\2\2IJ\7?\2\2J\36\3\2\2\2KL\7#\2\2LM")
        buf.write("\7?\2\2M \3\2\2\2NO\7(\2\2OP\7(\2\2P\"\3\2\2\2QR\7~\2")
        buf.write("\2RS\7~\2\2S$\3\2\2\2TU\7#\2\2U&\3\2\2\2VX\t\3\2\2WV\3")
        buf.write("\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\b\24")
        buf.write("\2\2\\(\3\2\2\2\5\2,Y\3\b\2\2")
        return buf.getvalue()


class MathLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    PLUS = 2
    MINUS = 3
    STAR = 4
    SLASH = 5
    LEFT_PAREN = 6
    RIGHT_PAREN = 7
    SEMICOLON = 8
    PERCENT = 9
    SMALLER_OP = 10
    GREATER_OP = 11
    EQUAL_OP = 12
    SMALLER_E_OP = 13
    GREATER_E_OP = 14
    NOT_EQUAL_OP = 15
    AND_OP = 16
    OR_OP = 17
    NOT_OP_OP = 18
    WS = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'", "';'", "'%'", "'<'", 
            "'>'", "'=='", "'<='", "'>='", "'!='", "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "PLUS", "MINUS", "STAR", "SLASH", "LEFT_PAREN", "RIGHT_PAREN", 
            "SEMICOLON", "PERCENT", "SMALLER_OP", "GREATER_OP", "EQUAL_OP", 
            "SMALLER_E_OP", "GREATER_E_OP", "NOT_EQUAL_OP", "AND_OP", "OR_OP", 
            "NOT_OP_OP", "WS" ]

    ruleNames = [ "INT", "PLUS", "MINUS", "STAR", "SLASH", "LEFT_PAREN", 
                  "RIGHT_PAREN", "SEMICOLON", "PERCENT", "SMALLER_OP", "GREATER_OP", 
                  "EQUAL_OP", "SMALLER_E_OP", "GREATER_E_OP", "NOT_EQUAL_OP", 
                  "AND_OP", "OR_OP", "NOT_OP_OP", "WS" ]

    grammarFileName = "Math.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


