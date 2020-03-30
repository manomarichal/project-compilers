# Generated from ../src/antlr/Grammar.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\62")
        buf.write("\u0108\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2")
        buf.write("\5\2\62\n\2\3\2\3\2\3\3\6\3\67\n\3\r\3\16\38\3\4\5\4<")
        buf.write("\n\4\3\4\3\4\5\4@\n\4\3\4\7\4C\n\4\f\4\16\4F\13\4\3\4")
        buf.write("\5\4I\n\4\3\5\3\5\3\6\3\6\3\6\5\6P\n\6\3\6\3\6\3\6\5\6")
        buf.write("U\n\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\7\bc\n\b\f\b\16\bf\13\b\5\bh\n\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\7\tr\n\t\f\t\16\tu\13\t\5\tw\n\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\5\13\u0081\n\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u0088\n\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u0093\n\16\3\17\3\17\3\17\3\17\7\17\u0099")
        buf.write("\n\17\f\17\16\17\u009c\13\17\3\17\5\17\u009f\n\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\24\5\24\u00bb\n\24\3\24\3\24\3\24\3\24\5")
        buf.write("\24\u00c1\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\5\25\u00cb\n\25\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u00df\n\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u00fb\n")
        buf.write("\27\f\27\16\27\u00fe\13\27\3\30\3\30\3\30\3\30\5\30\u0104")
        buf.write("\n\30\3\30\3\30\3\30\2\3,\31\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\2\f\3\2\6\b\3\2\21\22\3\2\3\5\3")
        buf.write("\2+,\4\2\27\27\31\31\4\2\30\30\32\32\3\2\32\34\4\2##&")
        buf.write("&\4\2$$\'\'\4\2%%((\2\u011b\2\61\3\2\2\2\4\66\3\2\2\2")
        buf.write("\6;\3\2\2\2\bJ\3\2\2\2\nT\3\2\2\2\fV\3\2\2\2\16X\3\2\2")
        buf.write("\2\20l\3\2\2\2\22z\3\2\2\2\24\u0080\3\2\2\2\26\u0087\3")
        buf.write("\2\2\2\30\u0089\3\2\2\2\32\u008d\3\2\2\2\34\u0094\3\2")
        buf.write("\2\2\36\u00a2\3\2\2\2 \u00a7\3\2\2\2\"\u00ab\3\2\2\2$")
        buf.write("\u00b5\3\2\2\2&\u00ba\3\2\2\2(\u00ca\3\2\2\2*\u00cc\3")
        buf.write("\2\2\2,\u00de\3\2\2\2.\u00ff\3\2\2\2\60\62\5\4\3\2\61")
        buf.write("\60\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2\2\63\64\7\2\2\3")
        buf.write("\64\3\3\2\2\2\65\67\5\n\6\2\66\65\3\2\2\2\678\3\2\2\2")
        buf.write("8\66\3\2\2\289\3\2\2\29\5\3\2\2\2:<\7\t\2\2;:\3\2\2\2")
        buf.write(";<\3\2\2\2<=\3\2\2\2=D\t\2\2\2>@\7\t\2\2?>\3\2\2\2?@\3")
        buf.write("\2\2\2@A\3\2\2\2AC\7\32\2\2B?\3\2\2\2CF\3\2\2\2DB\3\2")
        buf.write("\2\2DE\3\2\2\2EH\3\2\2\2FD\3\2\2\2GI\7\t\2\2HG\3\2\2\2")
        buf.write("HI\3\2\2\2I\7\3\2\2\2JK\7/\2\2K\t\3\2\2\2LU\5\16\b\2M")
        buf.write("P\5&\24\2NP\5\f\7\2OM\3\2\2\2ON\3\2\2\2PQ\3\2\2\2QR\7")
        buf.write("!\2\2RU\3\2\2\2SU\5\26\f\2TL\3\2\2\2TO\3\2\2\2TS\3\2\2")
        buf.write("\2U\13\3\2\2\2VW\t\3\2\2W\r\3\2\2\2XY\5\6\4\2YZ\5\b\5")
        buf.write("\2Zg\7\35\2\2[\\\5\6\4\2\\]\5\b\5\2]d\3\2\2\2^_\7\25\2")
        buf.write("\2_`\5\6\4\2`a\5\b\5\2ac\3\2\2\2b^\3\2\2\2cf\3\2\2\2d")
        buf.write("b\3\2\2\2de\3\2\2\2eh\3\2\2\2fd\3\2\2\2g[\3\2\2\2gh\3")
        buf.write("\2\2\2hi\3\2\2\2ij\7\36\2\2jk\5\24\13\2k\17\3\2\2\2lm")
        buf.write("\5\b\5\2mv\7\35\2\2ns\5&\24\2op\7\25\2\2pr\5&\24\2qo\3")
        buf.write("\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2tw\3\2\2\2us\3\2\2")
        buf.write("\2vn\3\2\2\2vw\3\2\2\2wx\3\2\2\2xy\7\36\2\2y\21\3\2\2")
        buf.write("\2z{\7\35\2\2{|\5&\24\2|}\7\36\2\2}\23\3\2\2\2~\u0081")
        buf.write("\5\n\6\2\177\u0081\5\30\r\2\u0080~\3\2\2\2\u0080\177\3")
        buf.write("\2\2\2\u0081\25\3\2\2\2\u0082\u0088\5\32\16\2\u0083\u0088")
        buf.write("\5\34\17\2\u0084\u0088\5\"\22\2\u0085\u0088\5$\23\2\u0086")
        buf.write("\u0088\5\30\r\2\u0087\u0082\3\2\2\2\u0087\u0083\3\2\2")
        buf.write("\2\u0087\u0084\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0086")
        buf.write("\3\2\2\2\u0088\27\3\2\2\2\u0089\u008a\7\37\2\2\u008a\u008b")
        buf.write("\5\4\3\2\u008b\u008c\7 \2\2\u008c\31\3\2\2\2\u008d\u008e")
        buf.write("\7\n\2\2\u008e\u008f\5\22\n\2\u008f\u0092\5\24\13\2\u0090")
        buf.write("\u0091\7\13\2\2\u0091\u0093\5\24\13\2\u0092\u0090\3\2")
        buf.write("\2\2\u0092\u0093\3\2\2\2\u0093\33\3\2\2\2\u0094\u0095")
        buf.write("\7\f\2\2\u0095\u0096\5\22\n\2\u0096\u009a\7\37\2\2\u0097")
        buf.write("\u0099\5\36\20\2\u0098\u0097\3\2\2\2\u0099\u009c\3\2\2")
        buf.write("\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009e")
        buf.write("\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009f\5 \21\2\u009e")
        buf.write("\u009d\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\u00a1\7 \2\2\u00a1\35\3\2\2\2\u00a2\u00a3\7\r\2")
        buf.write("\2\u00a3\u00a4\5*\26\2\u00a4\u00a5\7\"\2\2\u00a5\u00a6")
        buf.write("\5\4\3\2\u00a6\37\3\2\2\2\u00a7\u00a8\7\16\2\2\u00a8\u00a9")
        buf.write("\7\"\2\2\u00a9\u00aa\5\4\3\2\u00aa!\3\2\2\2\u00ab\u00ac")
        buf.write("\7\17\2\2\u00ac\u00ad\7\35\2\2\u00ad\u00ae\5&\24\2\u00ae")
        buf.write("\u00af\7!\2\2\u00af\u00b0\5&\24\2\u00b0\u00b1\7!\2\2\u00b1")
        buf.write("\u00b2\5&\24\2\u00b2\u00b3\7\36\2\2\u00b3\u00b4\5\24\13")
        buf.write("\2\u00b4#\3\2\2\2\u00b5\u00b6\7\20\2\2\u00b6\u00b7\5\22")
        buf.write("\n\2\u00b7\u00b8\5\24\13\2\u00b8%\3\2\2\2\u00b9\u00bb")
        buf.write("\7\24\2\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb")
        buf.write("\u00c0\3\2\2\2\u00bc\u00c1\5(\25\2\u00bd\u00c1\5,\27\2")
        buf.write("\u00be\u00c1\5.\30\2\u00bf\u00c1\5\20\t\2\u00c0\u00bc")
        buf.write("\3\2\2\2\u00c0\u00bd\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0")
        buf.write("\u00bf\3\2\2\2\u00c1\'\3\2\2\2\u00c2\u00c3\5\6\4\2\u00c3")
        buf.write("\u00c4\5\b\5\2\u00c4\u00c5\7\26\2\2\u00c5\u00c6\5,\27")
        buf.write("\2\u00c6\u00cb\3\2\2\2\u00c7\u00c8\5\6\4\2\u00c8\u00c9")
        buf.write("\5\b\5\2\u00c9\u00cb\3\2\2\2\u00ca\u00c2\3\2\2\2\u00ca")
        buf.write("\u00c7\3\2\2\2\u00cb)\3\2\2\2\u00cc\u00cd\t\4\2\2\u00cd")
        buf.write("+\3\2\2\2\u00ce\u00cf\b\27\1\2\u00cf\u00d0\7\35\2\2\u00d0")
        buf.write("\u00d1\5,\27\2\u00d1\u00d2\7\36\2\2\u00d2\u00df\3\2\2")
        buf.write("\2\u00d3\u00d4\t\5\2\2\u00d4\u00df\5,\27\21\u00d5\u00d6")
        buf.write("\t\6\2\2\u00d6\u00df\5,\27\20\u00d7\u00d8\t\7\2\2\u00d8")
        buf.write("\u00df\5,\27\17\u00d9\u00da\7-\2\2\u00da\u00df\5,\27\16")
        buf.write("\u00db\u00df\5\b\5\2\u00dc\u00df\5*\26\2\u00dd\u00df\5")
        buf.write("\20\t\2\u00de\u00ce\3\2\2\2\u00de\u00d3\3\2\2\2\u00de")
        buf.write("\u00d5\3\2\2\2\u00de\u00d7\3\2\2\2\u00de\u00d9\3\2\2\2")
        buf.write("\u00de\u00db\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00dd\3")
        buf.write("\2\2\2\u00df\u00fc\3\2\2\2\u00e0\u00e1\f\r\2\2\u00e1\u00e2")
        buf.write("\t\b\2\2\u00e2\u00fb\5,\27\16\u00e3\u00e4\f\f\2\2\u00e4")
        buf.write("\u00e5\t\6\2\2\u00e5\u00fb\5,\27\r\u00e6\u00e7\f\13\2")
        buf.write("\2\u00e7\u00e8\t\t\2\2\u00e8\u00fb\5,\27\f\u00e9\u00ea")
        buf.write("\f\n\2\2\u00ea\u00eb\t\n\2\2\u00eb\u00fb\5,\27\13\u00ec")
        buf.write("\u00ed\f\t\2\2\u00ed\u00ee\t\13\2\2\u00ee\u00fb\5,\27")
        buf.write("\n\u00ef\u00f0\f\b\2\2\u00f0\u00f1\7)\2\2\u00f1\u00fb")
        buf.write("\5,\27\t\u00f2\u00f3\f\7\2\2\u00f3\u00f4\7*\2\2\u00f4")
        buf.write("\u00fb\5,\27\b\u00f5\u00f6\f\6\2\2\u00f6\u00f7\7\26\2")
        buf.write("\2\u00f7\u00fb\5,\27\6\u00f8\u00f9\f\22\2\2\u00f9\u00fb")
        buf.write("\t\5\2\2\u00fa\u00e0\3\2\2\2\u00fa\u00e3\3\2\2\2\u00fa")
        buf.write("\u00e6\3\2\2\2\u00fa\u00e9\3\2\2\2\u00fa\u00ec\3\2\2\2")
        buf.write("\u00fa\u00ef\3\2\2\2\u00fa\u00f2\3\2\2\2\u00fa\u00f5\3")
        buf.write("\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa")
        buf.write("\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd-\3\2\2\2\u00fe\u00fc")
        buf.write("\3\2\2\2\u00ff\u0100\7.\2\2\u0100\u0103\7\35\2\2\u0101")
        buf.write("\u0104\5*\26\2\u0102\u0104\5\b\5\2\u0103\u0101\3\2\2\2")
        buf.write("\u0103\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0106\7")
        buf.write("\36\2\2\u0106/\3\2\2\2\32\618;?DHOTdgsv\u0080\u0087\u0092")
        buf.write("\u009a\u009e\u00ba\u00c0\u00ca\u00de\u00fa\u00fc\u0103")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'int'", "'float'", "'char'", "'const'", "'if'", "'else'", 
                     "'switch'", "'case'", "'default'", "'for'", "'while'", 
                     "'break'", "'continue'", "'void'", "'return'", "','", 
                     "'='", "'+'", "'&'", "'-'", "'*'", "'/'", "'%'", "'('", 
                     "')'", "'{'", "'}'", "';'", "':'", "'<'", "'>'", "'=='", 
                     "'<='", "'>='", "'!='", "'&&'", "'||'", "'++'", "'--'", 
                     "'!'", "'printf'" ]

    symbolicNames = [ "<INVALID>", "CHAR", "INT", "FLOAT", "INT_TYPE", "FLOAT_TYPE", 
                      "CHAR_TYPE", "CONST", "IF_KW", "ELSE_KW", "SWITCH_KW", 
                      "CASE_BRANCH", "DEFAULT_BRANCH", "FOR_KW", "WHILE_KW", 
                      "BREAK_KW", "CONT_KW", "VOID_KW", "RETURN_KW", "COMMA", 
                      "ASSIGN_OP", "PLUS", "AMP", "MINUS", "STAR", "SLASH", 
                      "PERCENT", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_C_BRACE", 
                      "RIGHT_C_BRACE", "SEMICOLON", "COLON", "SMALLER_OP", 
                      "GREATER_OP", "EQUAL_OP", "SMALLER_E_OP", "GREATER_E_OP", 
                      "NOT_EQUAL_OP", "AND_OP", "OR_OP", "INCR", "DECR", 
                      "NOT_OP", "PRINT", "ID", "WS", "COMMENT_SINGLE", "COMMENT_MULTI" ]

    RULE_doc = 0
    RULE_block = 1
    RULE_typeObj = 2
    RULE_identifier = 3
    RULE_statement = 4
    RULE_control = 5
    RULE_functionDecl = 6
    RULE_functionCall = 7
    RULE_parenCond = 8
    RULE_stateOrScope = 9
    RULE_construct = 10
    RULE_scopeConstr = 11
    RULE_ifConstr = 12
    RULE_switchConstr = 13
    RULE_caseBranch = 14
    RULE_defaultBranch = 15
    RULE_forConstr = 16
    RULE_whileConstr = 17
    RULE_general_expr = 18
    RULE_decl = 19
    RULE_literal = 20
    RULE_expr = 21
    RULE_printf = 22

    ruleNames =  [ "doc", "block", "typeObj", "identifier", "statement", 
                   "control", "functionDecl", "functionCall", "parenCond", 
                   "stateOrScope", "construct", "scopeConstr", "ifConstr", 
                   "switchConstr", "caseBranch", "defaultBranch", "forConstr", 
                   "whileConstr", "general_expr", "decl", "literal", "expr", 
                   "printf" ]

    EOF = Token.EOF
    CHAR=1
    INT=2
    FLOAT=3
    INT_TYPE=4
    FLOAT_TYPE=5
    CHAR_TYPE=6
    CONST=7
    IF_KW=8
    ELSE_KW=9
    SWITCH_KW=10
    CASE_BRANCH=11
    DEFAULT_BRANCH=12
    FOR_KW=13
    WHILE_KW=14
    BREAK_KW=15
    CONT_KW=16
    VOID_KW=17
    RETURN_KW=18
    COMMA=19
    ASSIGN_OP=20
    PLUS=21
    AMP=22
    MINUS=23
    STAR=24
    SLASH=25
    PERCENT=26
    LEFT_PAREN=27
    RIGHT_PAREN=28
    LEFT_C_BRACE=29
    RIGHT_C_BRACE=30
    SEMICOLON=31
    COLON=32
    SMALLER_OP=33
    GREATER_OP=34
    EQUAL_OP=35
    SMALLER_E_OP=36
    GREATER_E_OP=37
    NOT_EQUAL_OP=38
    AND_OP=39
    OR_OP=40
    INCR=41
    DECR=42
    NOT_OP=43
    PRINT=44
    ID=45
    WS=46
    COMMENT_SINGLE=47
    COMMENT_MULTI=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_doc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoc" ):
                return visitor.visitDoc(self)
            else:
                return visitor.visitChildren(self)




    def doc(self):

        localctx = GrammarParser.DocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_doc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.CHAR) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT) | (1 << GrammarParser.INT_TYPE) | (1 << GrammarParser.FLOAT_TYPE) | (1 << GrammarParser.CHAR_TYPE) | (1 << GrammarParser.CONST) | (1 << GrammarParser.IF_KW) | (1 << GrammarParser.SWITCH_KW) | (1 << GrammarParser.FOR_KW) | (1 << GrammarParser.WHILE_KW) | (1 << GrammarParser.BREAK_KW) | (1 << GrammarParser.CONT_KW) | (1 << GrammarParser.RETURN_KW) | (1 << GrammarParser.PLUS) | (1 << GrammarParser.AMP) | (1 << GrammarParser.MINUS) | (1 << GrammarParser.STAR) | (1 << GrammarParser.LEFT_PAREN) | (1 << GrammarParser.LEFT_C_BRACE) | (1 << GrammarParser.INCR) | (1 << GrammarParser.DECR) | (1 << GrammarParser.NOT_OP) | (1 << GrammarParser.PRINT) | (1 << GrammarParser.ID))) != 0):
                self.state = 46
                self.block()


            self.state = 49
            self.match(GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = GrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self.statement()
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.CHAR) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT) | (1 << GrammarParser.INT_TYPE) | (1 << GrammarParser.FLOAT_TYPE) | (1 << GrammarParser.CHAR_TYPE) | (1 << GrammarParser.CONST) | (1 << GrammarParser.IF_KW) | (1 << GrammarParser.SWITCH_KW) | (1 << GrammarParser.FOR_KW) | (1 << GrammarParser.WHILE_KW) | (1 << GrammarParser.BREAK_KW) | (1 << GrammarParser.CONT_KW) | (1 << GrammarParser.RETURN_KW) | (1 << GrammarParser.PLUS) | (1 << GrammarParser.AMP) | (1 << GrammarParser.MINUS) | (1 << GrammarParser.STAR) | (1 << GrammarParser.LEFT_PAREN) | (1 << GrammarParser.LEFT_C_BRACE) | (1 << GrammarParser.INCR) | (1 << GrammarParser.DECR) | (1 << GrammarParser.NOT_OP) | (1 << GrammarParser.PRINT) | (1 << GrammarParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeObjContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(GrammarParser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(GrammarParser.FLOAT_TYPE, 0)

        def CHAR_TYPE(self):
            return self.getToken(GrammarParser.CHAR_TYPE, 0)

        def CONST(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.CONST)
            else:
                return self.getToken(GrammarParser.CONST, i)

        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.STAR)
            else:
                return self.getToken(GrammarParser.STAR, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_typeObj

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeObj" ):
                return visitor.visitTypeObj(self)
            else:
                return visitor.visitChildren(self)




    def typeObj(self):

        localctx = GrammarParser.TypeObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_typeObj)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.CONST:
                self.state = 56
                self.match(GrammarParser.CONST)


            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.INT_TYPE) | (1 << GrammarParser.FLOAT_TYPE) | (1 << GrammarParser.CHAR_TYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==GrammarParser.CONST:
                        self.state = 60
                        self.match(GrammarParser.CONST)


                    self.state = 63
                    self.match(GrammarParser.STAR) 
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.CONST:
                self.state = 69
                self.match(GrammarParser.CONST)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = GrammarParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(GrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDecl(self):
            return self.getTypedRuleContext(GrammarParser.FunctionDeclContext,0)


        def SEMICOLON(self):
            return self.getToken(GrammarParser.SEMICOLON, 0)

        def general_expr(self):
            return self.getTypedRuleContext(GrammarParser.General_exprContext,0)


        def control(self):
            return self.getTypedRuleContext(GrammarParser.ControlContext,0)


        def construct(self):
            return self.getTypedRuleContext(GrammarParser.ConstructContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.functionDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [GrammarParser.CHAR, GrammarParser.INT, GrammarParser.FLOAT, GrammarParser.INT_TYPE, GrammarParser.FLOAT_TYPE, GrammarParser.CHAR_TYPE, GrammarParser.CONST, GrammarParser.RETURN_KW, GrammarParser.PLUS, GrammarParser.AMP, GrammarParser.MINUS, GrammarParser.STAR, GrammarParser.LEFT_PAREN, GrammarParser.INCR, GrammarParser.DECR, GrammarParser.NOT_OP, GrammarParser.PRINT, GrammarParser.ID]:
                    self.state = 75
                    self.general_expr()
                    pass
                elif token in [GrammarParser.BREAK_KW, GrammarParser.CONT_KW]:
                    self.state = 76
                    self.control()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 79
                self.match(GrammarParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.construct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ControlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_KW(self):
            return self.getToken(GrammarParser.BREAK_KW, 0)

        def CONT_KW(self):
            return self.getToken(GrammarParser.CONT_KW, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_control

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControl" ):
                return visitor.visitControl(self)
            else:
                return visitor.visitChildren(self)




    def control(self):

        localctx = GrammarParser.ControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_control)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not(_la==GrammarParser.BREAK_KW or _la==GrammarParser.CONT_KW):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeObj(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.TypeObjContext)
            else:
                return self.getTypedRuleContext(GrammarParser.TypeObjContext,i)


        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(GrammarParser.IdentifierContext,i)


        def LEFT_PAREN(self):
            return self.getToken(GrammarParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(GrammarParser.RIGHT_PAREN, 0)

        def stateOrScope(self):
            return self.getTypedRuleContext(GrammarParser.StateOrScopeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_functionDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = GrammarParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.typeObj()
            self.state = 87
            self.identifier()
            self.state = 88
            self.match(GrammarParser.LEFT_PAREN)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.INT_TYPE) | (1 << GrammarParser.FLOAT_TYPE) | (1 << GrammarParser.CHAR_TYPE) | (1 << GrammarParser.CONST))) != 0):
                self.state = 89
                self.typeObj()
                self.state = 90
                self.identifier()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.COMMA:
                    self.state = 92
                    self.match(GrammarParser.COMMA)
                    self.state = 93
                    self.typeObj()
                    self.state = 94
                    self.identifier()
                    self.state = 100
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 103
            self.match(GrammarParser.RIGHT_PAREN)
            self.state = 104
            self.stateOrScope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


        def LEFT_PAREN(self):
            return self.getToken(GrammarParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(GrammarParser.RIGHT_PAREN, 0)

        def general_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.General_exprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.General_exprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.COMMA)
            else:
                return self.getToken(GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = GrammarParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.identifier()
            self.state = 107
            self.match(GrammarParser.LEFT_PAREN)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.CHAR) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT) | (1 << GrammarParser.INT_TYPE) | (1 << GrammarParser.FLOAT_TYPE) | (1 << GrammarParser.CHAR_TYPE) | (1 << GrammarParser.CONST) | (1 << GrammarParser.RETURN_KW) | (1 << GrammarParser.PLUS) | (1 << GrammarParser.AMP) | (1 << GrammarParser.MINUS) | (1 << GrammarParser.STAR) | (1 << GrammarParser.LEFT_PAREN) | (1 << GrammarParser.INCR) | (1 << GrammarParser.DECR) | (1 << GrammarParser.NOT_OP) | (1 << GrammarParser.PRINT) | (1 << GrammarParser.ID))) != 0):
                self.state = 108
                self.general_expr()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.COMMA:
                    self.state = 109
                    self.match(GrammarParser.COMMA)
                    self.state = 110
                    self.general_expr()
                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 118
            self.match(GrammarParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenCondContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(GrammarParser.LEFT_PAREN, 0)

        def general_expr(self):
            return self.getTypedRuleContext(GrammarParser.General_exprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(GrammarParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_parenCond

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenCond" ):
                return visitor.visitParenCond(self)
            else:
                return visitor.visitChildren(self)




    def parenCond(self):

        localctx = GrammarParser.ParenCondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parenCond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(GrammarParser.LEFT_PAREN)
            self.state = 121
            self.general_expr()
            self.state = 122
            self.match(GrammarParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateOrScopeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def scopeConstr(self):
            return self.getTypedRuleContext(GrammarParser.ScopeConstrContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_stateOrScope

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateOrScope" ):
                return visitor.visitStateOrScope(self)
            else:
                return visitor.visitChildren(self)




    def stateOrScope(self):

        localctx = GrammarParser.StateOrScopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stateOrScope)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.scopeConstr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifConstr(self):
            return self.getTypedRuleContext(GrammarParser.IfConstrContext,0)


        def switchConstr(self):
            return self.getTypedRuleContext(GrammarParser.SwitchConstrContext,0)


        def forConstr(self):
            return self.getTypedRuleContext(GrammarParser.ForConstrContext,0)


        def whileConstr(self):
            return self.getTypedRuleContext(GrammarParser.WhileConstrContext,0)


        def scopeConstr(self):
            return self.getTypedRuleContext(GrammarParser.ScopeConstrContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_construct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstruct" ):
                return visitor.visitConstruct(self)
            else:
                return visitor.visitChildren(self)




    def construct(self):

        localctx = GrammarParser.ConstructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_construct)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.IF_KW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.ifConstr()
                pass
            elif token in [GrammarParser.SWITCH_KW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.switchConstr()
                pass
            elif token in [GrammarParser.FOR_KW]:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.forConstr()
                pass
            elif token in [GrammarParser.WHILE_KW]:
                self.enterOuterAlt(localctx, 4)
                self.state = 131
                self.whileConstr()
                pass
            elif token in [GrammarParser.LEFT_C_BRACE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
                self.scopeConstr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScopeConstrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_C_BRACE(self):
            return self.getToken(GrammarParser.LEFT_C_BRACE, 0)

        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


        def RIGHT_C_BRACE(self):
            return self.getToken(GrammarParser.RIGHT_C_BRACE, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_scopeConstr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScopeConstr" ):
                return visitor.visitScopeConstr(self)
            else:
                return visitor.visitChildren(self)




    def scopeConstr(self):

        localctx = GrammarParser.ScopeConstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_scopeConstr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(GrammarParser.LEFT_C_BRACE)
            self.state = 136
            self.block()
            self.state = 137
            self.match(GrammarParser.RIGHT_C_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfConstrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_KW(self):
            return self.getToken(GrammarParser.IF_KW, 0)

        def parenCond(self):
            return self.getTypedRuleContext(GrammarParser.ParenCondContext,0)


        def stateOrScope(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StateOrScopeContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StateOrScopeContext,i)


        def ELSE_KW(self):
            return self.getToken(GrammarParser.ELSE_KW, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_ifConstr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfConstr" ):
                return visitor.visitIfConstr(self)
            else:
                return visitor.visitChildren(self)




    def ifConstr(self):

        localctx = GrammarParser.IfConstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifConstr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(GrammarParser.IF_KW)
            self.state = 140
            self.parenCond()
            self.state = 141
            self.stateOrScope()
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 142
                self.match(GrammarParser.ELSE_KW)
                self.state = 143
                self.stateOrScope()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchConstrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH_KW(self):
            return self.getToken(GrammarParser.SWITCH_KW, 0)

        def parenCond(self):
            return self.getTypedRuleContext(GrammarParser.ParenCondContext,0)


        def LEFT_C_BRACE(self):
            return self.getToken(GrammarParser.LEFT_C_BRACE, 0)

        def RIGHT_C_BRACE(self):
            return self.getToken(GrammarParser.RIGHT_C_BRACE, 0)

        def caseBranch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.CaseBranchContext)
            else:
                return self.getTypedRuleContext(GrammarParser.CaseBranchContext,i)


        def defaultBranch(self):
            return self.getTypedRuleContext(GrammarParser.DefaultBranchContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_switchConstr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchConstr" ):
                return visitor.visitSwitchConstr(self)
            else:
                return visitor.visitChildren(self)




    def switchConstr(self):

        localctx = GrammarParser.SwitchConstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_switchConstr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(GrammarParser.SWITCH_KW)
            self.state = 147
            self.parenCond()
            self.state = 148
            self.match(GrammarParser.LEFT_C_BRACE)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.CASE_BRANCH:
                self.state = 149
                self.caseBranch()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.DEFAULT_BRANCH:
                self.state = 155
                self.defaultBranch()


            self.state = 158
            self.match(GrammarParser.RIGHT_C_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseBranchContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE_BRANCH(self):
            return self.getToken(GrammarParser.CASE_BRANCH, 0)

        def literal(self):
            return self.getTypedRuleContext(GrammarParser.LiteralContext,0)


        def COLON(self):
            return self.getToken(GrammarParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_caseBranch

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseBranch" ):
                return visitor.visitCaseBranch(self)
            else:
                return visitor.visitChildren(self)




    def caseBranch(self):

        localctx = GrammarParser.CaseBranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_caseBranch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(GrammarParser.CASE_BRANCH)
            self.state = 161
            self.literal()
            self.state = 162
            self.match(GrammarParser.COLON)
            self.state = 163
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultBranchContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT_BRANCH(self):
            return self.getToken(GrammarParser.DEFAULT_BRANCH, 0)

        def COLON(self):
            return self.getToken(GrammarParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_defaultBranch

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultBranch" ):
                return visitor.visitDefaultBranch(self)
            else:
                return visitor.visitChildren(self)




    def defaultBranch(self):

        localctx = GrammarParser.DefaultBranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_defaultBranch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(GrammarParser.DEFAULT_BRANCH)
            self.state = 166
            self.match(GrammarParser.COLON)
            self.state = 167
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForConstrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_KW(self):
            return self.getToken(GrammarParser.FOR_KW, 0)

        def LEFT_PAREN(self):
            return self.getToken(GrammarParser.LEFT_PAREN, 0)

        def general_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.General_exprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.General_exprContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SEMICOLON)
            else:
                return self.getToken(GrammarParser.SEMICOLON, i)

        def RIGHT_PAREN(self):
            return self.getToken(GrammarParser.RIGHT_PAREN, 0)

        def stateOrScope(self):
            return self.getTypedRuleContext(GrammarParser.StateOrScopeContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_forConstr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForConstr" ):
                return visitor.visitForConstr(self)
            else:
                return visitor.visitChildren(self)




    def forConstr(self):

        localctx = GrammarParser.ForConstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forConstr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(GrammarParser.FOR_KW)
            self.state = 170
            self.match(GrammarParser.LEFT_PAREN)
            self.state = 171
            self.general_expr()
            self.state = 172
            self.match(GrammarParser.SEMICOLON)
            self.state = 173
            self.general_expr()
            self.state = 174
            self.match(GrammarParser.SEMICOLON)
            self.state = 175
            self.general_expr()
            self.state = 176
            self.match(GrammarParser.RIGHT_PAREN)
            self.state = 177
            self.stateOrScope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileConstrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE_KW(self):
            return self.getToken(GrammarParser.WHILE_KW, 0)

        def parenCond(self):
            return self.getTypedRuleContext(GrammarParser.ParenCondContext,0)


        def stateOrScope(self):
            return self.getTypedRuleContext(GrammarParser.StateOrScopeContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_whileConstr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileConstr" ):
                return visitor.visitWhileConstr(self)
            else:
                return visitor.visitChildren(self)




    def whileConstr(self):

        localctx = GrammarParser.WhileConstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_whileConstr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(GrammarParser.WHILE_KW)
            self.state = 180
            self.parenCond()
            self.state = 181
            self.stateOrScope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class General_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(GrammarParser.DeclContext,0)


        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def printf(self):
            return self.getTypedRuleContext(GrammarParser.PrintfContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(GrammarParser.FunctionCallContext,0)


        def RETURN_KW(self):
            return self.getToken(GrammarParser.RETURN_KW, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_general_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneral_expr" ):
                return visitor.visitGeneral_expr(self)
            else:
                return visitor.visitChildren(self)




    def general_expr(self):

        localctx = GrammarParser.General_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_general_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.RETURN_KW:
                self.state = 183
                self.match(GrammarParser.RETURN_KW)


            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 186
                self.decl()
                pass

            elif la_ == 2:
                self.state = 187
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 188
                self.printf()
                pass

            elif la_ == 4:
                self.state = 189
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeObj(self):
            return self.getTypedRuleContext(GrammarParser.TypeObjContext,0)


        def identifier(self):
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


        def ASSIGN_OP(self):
            return self.getToken(GrammarParser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = GrammarParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_decl)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.typeObj()
                self.state = 193
                self.identifier()
                self.state = 194
                self.match(GrammarParser.ASSIGN_OP)
                self.state = 195
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.typeObj()
                self.state = 198
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GrammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(GrammarParser.FLOAT, 0)

        def CHAR(self):
            return self.getToken(GrammarParser.CHAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = GrammarParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.CHAR) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(GrammarParser.LEFT_PAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


        def RIGHT_PAREN(self):
            return self.getToken(GrammarParser.RIGHT_PAREN, 0)

        def DECR(self):
            return self.getToken(GrammarParser.DECR, 0)

        def INCR(self):
            return self.getToken(GrammarParser.INCR, 0)

        def MINUS(self):
            return self.getToken(GrammarParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(GrammarParser.PLUS, 0)

        def AMP(self):
            return self.getToken(GrammarParser.AMP, 0)

        def STAR(self):
            return self.getToken(GrammarParser.STAR, 0)

        def NOT_OP(self):
            return self.getToken(GrammarParser.NOT_OP, 0)

        def identifier(self):
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


        def literal(self):
            return self.getTypedRuleContext(GrammarParser.LiteralContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(GrammarParser.FunctionCallContext,0)


        def SLASH(self):
            return self.getToken(GrammarParser.SLASH, 0)

        def PERCENT(self):
            return self.getToken(GrammarParser.PERCENT, 0)

        def SMALLER_OP(self):
            return self.getToken(GrammarParser.SMALLER_OP, 0)

        def SMALLER_E_OP(self):
            return self.getToken(GrammarParser.SMALLER_E_OP, 0)

        def GREATER_OP(self):
            return self.getToken(GrammarParser.GREATER_OP, 0)

        def GREATER_E_OP(self):
            return self.getToken(GrammarParser.GREATER_E_OP, 0)

        def EQUAL_OP(self):
            return self.getToken(GrammarParser.EQUAL_OP, 0)

        def NOT_EQUAL_OP(self):
            return self.getToken(GrammarParser.NOT_EQUAL_OP, 0)

        def AND_OP(self):
            return self.getToken(GrammarParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(GrammarParser.OR_OP, 0)

        def ASSIGN_OP(self):
            return self.getToken(GrammarParser.ASSIGN_OP, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 205
                self.match(GrammarParser.LEFT_PAREN)
                self.state = 206
                self.expr(0)
                self.state = 207
                self.match(GrammarParser.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.state = 209
                _la = self._input.LA(1)
                if not(_la==GrammarParser.INCR or _la==GrammarParser.DECR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 210
                self.expr(15)
                pass

            elif la_ == 3:
                self.state = 211
                _la = self._input.LA(1)
                if not(_la==GrammarParser.PLUS or _la==GrammarParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 212
                self.expr(14)
                pass

            elif la_ == 4:
                self.state = 213
                _la = self._input.LA(1)
                if not(_la==GrammarParser.AMP or _la==GrammarParser.STAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 214
                self.expr(13)
                pass

            elif la_ == 5:
                self.state = 215
                self.match(GrammarParser.NOT_OP)
                self.state = 216
                self.expr(12)
                pass

            elif la_ == 6:
                self.state = 217
                self.identifier()
                pass

            elif la_ == 7:
                self.state = 218
                self.literal()
                pass

            elif la_ == 8:
                self.state = 219
                self.functionCall()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 248
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 222
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 223
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.STAR) | (1 << GrammarParser.SLASH) | (1 << GrammarParser.PERCENT))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 224
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 225
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 226
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.PLUS or _la==GrammarParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 227
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 228
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 229
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.SMALLER_OP or _la==GrammarParser.SMALLER_E_OP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 230
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 231
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 232
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.GREATER_OP or _la==GrammarParser.GREATER_E_OP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 233
                        self.expr(9)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 234
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 235
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.EQUAL_OP or _la==GrammarParser.NOT_EQUAL_OP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 236
                        self.expr(8)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 237
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 238
                        self.match(GrammarParser.AND_OP)
                        self.state = 239
                        self.expr(7)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 240
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 241
                        self.match(GrammarParser.OR_OP)
                        self.state = 242
                        self.expr(6)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 243
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 244
                        self.match(GrammarParser.ASSIGN_OP)
                        self.state = 245
                        self.expr(4)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 246
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 247
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.INCR or _la==GrammarParser.DECR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrintfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(GrammarParser.PRINT, 0)

        def LEFT_PAREN(self):
            return self.getToken(GrammarParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(GrammarParser.RIGHT_PAREN, 0)

        def literal(self):
            return self.getTypedRuleContext(GrammarParser.LiteralContext,0)


        def identifier(self):
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_printf

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintf" ):
                return visitor.visitPrintf(self)
            else:
                return visitor.visitChildren(self)




    def printf(self):

        localctx = GrammarParser.PrintfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_printf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(GrammarParser.PRINT)
            self.state = 254
            self.match(GrammarParser.LEFT_PAREN)
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.CHAR, GrammarParser.INT, GrammarParser.FLOAT]:
                self.state = 255
                self.literal()
                pass
            elif token in [GrammarParser.ID]:
                self.state = 256
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 259
            self.match(GrammarParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 16)
         




