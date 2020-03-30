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
        buf.write("\u010c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\5\2\64\n\2\3\2\3\2\3\3\6\39\n\3\r\3\16\3:\3")
        buf.write("\4\5\4>\n\4\3\4\3\4\5\4B\n\4\3\4\7\4E\n\4\f\4\16\4H\13")
        buf.write("\4\3\4\5\4K\n\4\3\5\3\5\3\6\3\6\3\6\5\6R\n\6\3\6\3\6\3")
        buf.write("\6\5\6W\n\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\7\be\n\b\f\b\16\bh\13\b\5\bj\n\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\7\tt\n\t\f\t\16\tw\13\t\5\ty\n\t\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u0085\n")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\5\r\u008c\n\r\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\5\17\u0097\n\17\3\20\3\20")
        buf.write("\3\20\3\20\7\20\u009d\n\20\f\20\16\20\u00a0\13\20\3\20")
        buf.write("\5\20\u00a3\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\5\25\u00bf\n")
        buf.write("\25\3\25\3\25\3\25\3\25\5\25\u00c5\n\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\5\26\u00cf\n\26\3\27\3\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\5\30\u00e3\n\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\7\30\u00ff\n\30\f\30\16\30\u0102\13\30\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u0108\n\31\3\31\3\31\3\31\2\3.\32")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\2")
        buf.write("\f\3\2\6\b\3\2\21\22\3\2\3\5\3\2+,\4\2\27\27\31\31\4\2")
        buf.write("\30\30\32\32\3\2\32\34\4\2##&&\4\2$$\'\'\4\2%%((\2\u011e")
        buf.write("\2\63\3\2\2\2\48\3\2\2\2\6=\3\2\2\2\bL\3\2\2\2\nV\3\2")
        buf.write("\2\2\fX\3\2\2\2\16Z\3\2\2\2\20n\3\2\2\2\22|\3\2\2\2\24")
        buf.write("~\3\2\2\2\26\u0084\3\2\2\2\30\u008b\3\2\2\2\32\u008d\3")
        buf.write("\2\2\2\34\u0091\3\2\2\2\36\u0098\3\2\2\2 \u00a6\3\2\2")
        buf.write("\2\"\u00ab\3\2\2\2$\u00af\3\2\2\2&\u00b9\3\2\2\2(\u00be")
        buf.write("\3\2\2\2*\u00ce\3\2\2\2,\u00d0\3\2\2\2.\u00e2\3\2\2\2")
        buf.write("\60\u0103\3\2\2\2\62\64\5\4\3\2\63\62\3\2\2\2\63\64\3")
        buf.write("\2\2\2\64\65\3\2\2\2\65\66\7\2\2\3\66\3\3\2\2\2\679\5")
        buf.write("\n\6\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;\5\3")
        buf.write("\2\2\2<>\7\t\2\2=<\3\2\2\2=>\3\2\2\2>?\3\2\2\2?F\t\2\2")
        buf.write("\2@B\7\t\2\2A@\3\2\2\2AB\3\2\2\2BC\3\2\2\2CE\7\32\2\2")
        buf.write("DA\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2GJ\3\2\2\2HF\3")
        buf.write("\2\2\2IK\7\t\2\2JI\3\2\2\2JK\3\2\2\2K\7\3\2\2\2LM\7/\2")
        buf.write("\2M\t\3\2\2\2NW\5\16\b\2OR\5(\25\2PR\5\f\7\2QO\3\2\2\2")
        buf.write("QP\3\2\2\2RS\3\2\2\2ST\7!\2\2TW\3\2\2\2UW\5\30\r\2VN\3")
        buf.write("\2\2\2VQ\3\2\2\2VU\3\2\2\2W\13\3\2\2\2XY\t\3\2\2Y\r\3")
        buf.write("\2\2\2Z[\5\6\4\2[\\\5\b\5\2\\i\7\35\2\2]^\5\6\4\2^_\5")
        buf.write("\b\5\2_f\3\2\2\2`a\7\25\2\2ab\5\6\4\2bc\5\b\5\2ce\3\2")
        buf.write("\2\2d`\3\2\2\2eh\3\2\2\2fd\3\2\2\2fg\3\2\2\2gj\3\2\2\2")
        buf.write("hf\3\2\2\2i]\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl\7\36\2\2lm")
        buf.write("\5\26\f\2m\17\3\2\2\2no\5\b\5\2ox\7\35\2\2pu\5\22\n\2")
        buf.write("qr\7\25\2\2rt\5\22\n\2sq\3\2\2\2tw\3\2\2\2us\3\2\2\2u")
        buf.write("v\3\2\2\2vy\3\2\2\2wu\3\2\2\2xp\3\2\2\2xy\3\2\2\2yz\3")
        buf.write("\2\2\2z{\7\36\2\2{\21\3\2\2\2|}\5(\25\2}\23\3\2\2\2~\177")
        buf.write("\7\35\2\2\177\u0080\5(\25\2\u0080\u0081\7\36\2\2\u0081")
        buf.write("\25\3\2\2\2\u0082\u0085\5\n\6\2\u0083\u0085\5\32\16\2")
        buf.write("\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085\27\3\2")
        buf.write("\2\2\u0086\u008c\5\34\17\2\u0087\u008c\5\36\20\2\u0088")
        buf.write("\u008c\5$\23\2\u0089\u008c\5&\24\2\u008a\u008c\5\32\16")
        buf.write("\2\u008b\u0086\3\2\2\2\u008b\u0087\3\2\2\2\u008b\u0088")
        buf.write("\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c")
        buf.write("\31\3\2\2\2\u008d\u008e\7\37\2\2\u008e\u008f\5\4\3\2\u008f")
        buf.write("\u0090\7 \2\2\u0090\33\3\2\2\2\u0091\u0092\7\n\2\2\u0092")
        buf.write("\u0093\5\24\13\2\u0093\u0096\5\26\f\2\u0094\u0095\7\13")
        buf.write("\2\2\u0095\u0097\5\26\f\2\u0096\u0094\3\2\2\2\u0096\u0097")
        buf.write("\3\2\2\2\u0097\35\3\2\2\2\u0098\u0099\7\f\2\2\u0099\u009a")
        buf.write("\5\24\13\2\u009a\u009e\7\37\2\2\u009b\u009d\5 \21\2\u009c")
        buf.write("\u009b\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009e\u009f\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e\3")
        buf.write("\2\2\2\u00a1\u00a3\5\"\22\2\u00a2\u00a1\3\2\2\2\u00a2")
        buf.write("\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\7 \2\2")
        buf.write("\u00a5\37\3\2\2\2\u00a6\u00a7\7\r\2\2\u00a7\u00a8\5,\27")
        buf.write("\2\u00a8\u00a9\7\"\2\2\u00a9\u00aa\5\4\3\2\u00aa!\3\2")
        buf.write("\2\2\u00ab\u00ac\7\16\2\2\u00ac\u00ad\7\"\2\2\u00ad\u00ae")
        buf.write("\5\4\3\2\u00ae#\3\2\2\2\u00af\u00b0\7\17\2\2\u00b0\u00b1")
        buf.write("\7\35\2\2\u00b1\u00b2\5(\25\2\u00b2\u00b3\7!\2\2\u00b3")
        buf.write("\u00b4\5(\25\2\u00b4\u00b5\7!\2\2\u00b5\u00b6\5(\25\2")
        buf.write("\u00b6\u00b7\7\36\2\2\u00b7\u00b8\5\26\f\2\u00b8%\3\2")
        buf.write("\2\2\u00b9\u00ba\7\20\2\2\u00ba\u00bb\5\24\13\2\u00bb")
        buf.write("\u00bc\5\26\f\2\u00bc\'\3\2\2\2\u00bd\u00bf\7\24\2\2\u00be")
        buf.write("\u00bd\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c4\3\2\2\2")
        buf.write("\u00c0\u00c5\5*\26\2\u00c1\u00c5\5.\30\2\u00c2\u00c5\5")
        buf.write("\60\31\2\u00c3\u00c5\5\20\t\2\u00c4\u00c0\3\2\2\2\u00c4")
        buf.write("\u00c1\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c3\3\2\2\2")
        buf.write("\u00c5)\3\2\2\2\u00c6\u00c7\5\6\4\2\u00c7\u00c8\5\b\5")
        buf.write("\2\u00c8\u00c9\7\26\2\2\u00c9\u00ca\5.\30\2\u00ca\u00cf")
        buf.write("\3\2\2\2\u00cb\u00cc\5\6\4\2\u00cc\u00cd\5\b\5\2\u00cd")
        buf.write("\u00cf\3\2\2\2\u00ce\u00c6\3\2\2\2\u00ce\u00cb\3\2\2\2")
        buf.write("\u00cf+\3\2\2\2\u00d0\u00d1\t\4\2\2\u00d1-\3\2\2\2\u00d2")
        buf.write("\u00d3\b\30\1\2\u00d3\u00d4\7\35\2\2\u00d4\u00d5\5.\30")
        buf.write("\2\u00d5\u00d6\7\36\2\2\u00d6\u00e3\3\2\2\2\u00d7\u00d8")
        buf.write("\t\5\2\2\u00d8\u00e3\5.\30\21\u00d9\u00da\t\6\2\2\u00da")
        buf.write("\u00e3\5.\30\20\u00db\u00dc\t\7\2\2\u00dc\u00e3\5.\30")
        buf.write("\17\u00dd\u00de\7-\2\2\u00de\u00e3\5.\30\16\u00df\u00e3")
        buf.write("\5\b\5\2\u00e0\u00e3\5,\27\2\u00e1\u00e3\5\20\t\2\u00e2")
        buf.write("\u00d2\3\2\2\2\u00e2\u00d7\3\2\2\2\u00e2\u00d9\3\2\2\2")
        buf.write("\u00e2\u00db\3\2\2\2\u00e2\u00dd\3\2\2\2\u00e2\u00df\3")
        buf.write("\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3\u0100")
        buf.write("\3\2\2\2\u00e4\u00e5\f\r\2\2\u00e5\u00e6\t\b\2\2\u00e6")
        buf.write("\u00ff\5.\30\16\u00e7\u00e8\f\f\2\2\u00e8\u00e9\t\6\2")
        buf.write("\2\u00e9\u00ff\5.\30\r\u00ea\u00eb\f\13\2\2\u00eb\u00ec")
        buf.write("\t\t\2\2\u00ec\u00ff\5.\30\f\u00ed\u00ee\f\n\2\2\u00ee")
        buf.write("\u00ef\t\n\2\2\u00ef\u00ff\5.\30\13\u00f0\u00f1\f\t\2")
        buf.write("\2\u00f1\u00f2\t\13\2\2\u00f2\u00ff\5.\30\n\u00f3\u00f4")
        buf.write("\f\b\2\2\u00f4\u00f5\7)\2\2\u00f5\u00ff\5.\30\t\u00f6")
        buf.write("\u00f7\f\7\2\2\u00f7\u00f8\7*\2\2\u00f8\u00ff\5.\30\b")
        buf.write("\u00f9\u00fa\f\6\2\2\u00fa\u00fb\7\26\2\2\u00fb\u00ff")
        buf.write("\5.\30\6\u00fc\u00fd\f\22\2\2\u00fd\u00ff\t\5\2\2\u00fe")
        buf.write("\u00e4\3\2\2\2\u00fe\u00e7\3\2\2\2\u00fe\u00ea\3\2\2\2")
        buf.write("\u00fe\u00ed\3\2\2\2\u00fe\u00f0\3\2\2\2\u00fe\u00f3\3")
        buf.write("\2\2\2\u00fe\u00f6\3\2\2\2\u00fe\u00f9\3\2\2\2\u00fe\u00fc")
        buf.write("\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe\3\2\2\2\u0100")
        buf.write("\u0101\3\2\2\2\u0101/\3\2\2\2\u0102\u0100\3\2\2\2\u0103")
        buf.write("\u0104\7.\2\2\u0104\u0107\7\35\2\2\u0105\u0108\5,\27\2")
        buf.write("\u0106\u0108\5\b\5\2\u0107\u0105\3\2\2\2\u0107\u0106\3")
        buf.write("\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a\7\36\2\2\u010a")
        buf.write("\61\3\2\2\2\32\63:=AFJQVfiux\u0084\u008b\u0096\u009e\u00a2")
        buf.write("\u00be\u00c4\u00ce\u00e2\u00fe\u0100\u0107")
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
    RULE_functionArgument = 8
    RULE_parenCond = 9
    RULE_stateOrScope = 10
    RULE_construct = 11
    RULE_scopeConstr = 12
    RULE_ifConstr = 13
    RULE_switchConstr = 14
    RULE_caseBranch = 15
    RULE_defaultBranch = 16
    RULE_forConstr = 17
    RULE_whileConstr = 18
    RULE_general_expr = 19
    RULE_decl = 20
    RULE_literal = 21
    RULE_expr = 22
    RULE_printf = 23

    ruleNames =  [ "doc", "block", "typeObj", "identifier", "statement", 
                   "control", "functionDecl", "functionCall", "functionArgument", 
                   "parenCond", "stateOrScope", "construct", "scopeConstr", 
                   "ifConstr", "switchConstr", "caseBranch", "defaultBranch", 
                   "forConstr", "whileConstr", "general_expr", "decl", "literal", 
                   "expr", "printf" ]

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
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.CHAR) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT) | (1 << GrammarParser.INT_TYPE) | (1 << GrammarParser.FLOAT_TYPE) | (1 << GrammarParser.CHAR_TYPE) | (1 << GrammarParser.CONST) | (1 << GrammarParser.IF_KW) | (1 << GrammarParser.SWITCH_KW) | (1 << GrammarParser.FOR_KW) | (1 << GrammarParser.WHILE_KW) | (1 << GrammarParser.BREAK_KW) | (1 << GrammarParser.CONT_KW) | (1 << GrammarParser.RETURN_KW) | (1 << GrammarParser.PLUS) | (1 << GrammarParser.AMP) | (1 << GrammarParser.MINUS) | (1 << GrammarParser.STAR) | (1 << GrammarParser.LEFT_PAREN) | (1 << GrammarParser.LEFT_C_BRACE) | (1 << GrammarParser.INCR) | (1 << GrammarParser.DECR) | (1 << GrammarParser.NOT_OP) | (1 << GrammarParser.PRINT) | (1 << GrammarParser.ID))) != 0):
                self.state = 48
                self.block()


            self.state = 51
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
            self.state = 54 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 53
                self.statement()
                self.state = 56 
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
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.CONST:
                self.state = 58
                self.match(GrammarParser.CONST)


            self.state = 61
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.INT_TYPE) | (1 << GrammarParser.FLOAT_TYPE) | (1 << GrammarParser.CHAR_TYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 63
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==GrammarParser.CONST:
                        self.state = 62
                        self.match(GrammarParser.CONST)


                    self.state = 65
                    self.match(GrammarParser.STAR) 
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.CONST:
                self.state = 71
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
            self.state = 74
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
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.functionDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [GrammarParser.CHAR, GrammarParser.INT, GrammarParser.FLOAT, GrammarParser.INT_TYPE, GrammarParser.FLOAT_TYPE, GrammarParser.CHAR_TYPE, GrammarParser.CONST, GrammarParser.RETURN_KW, GrammarParser.PLUS, GrammarParser.AMP, GrammarParser.MINUS, GrammarParser.STAR, GrammarParser.LEFT_PAREN, GrammarParser.INCR, GrammarParser.DECR, GrammarParser.NOT_OP, GrammarParser.PRINT, GrammarParser.ID]:
                    self.state = 77
                    self.general_expr()
                    pass
                elif token in [GrammarParser.BREAK_KW, GrammarParser.CONT_KW]:
                    self.state = 78
                    self.control()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 81
                self.match(GrammarParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
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
            self.state = 86
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
            self.state = 88
            self.typeObj()
            self.state = 89
            self.identifier()
            self.state = 90
            self.match(GrammarParser.LEFT_PAREN)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.INT_TYPE) | (1 << GrammarParser.FLOAT_TYPE) | (1 << GrammarParser.CHAR_TYPE) | (1 << GrammarParser.CONST))) != 0):
                self.state = 91
                self.typeObj()
                self.state = 92
                self.identifier()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.COMMA:
                    self.state = 94
                    self.match(GrammarParser.COMMA)
                    self.state = 95
                    self.typeObj()
                    self.state = 96
                    self.identifier()
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 105
            self.match(GrammarParser.RIGHT_PAREN)
            self.state = 106
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

        def functionArgument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.FunctionArgumentContext)
            else:
                return self.getTypedRuleContext(GrammarParser.FunctionArgumentContext,i)


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
            self.state = 108
            self.identifier()
            self.state = 109
            self.match(GrammarParser.LEFT_PAREN)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.CHAR) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT) | (1 << GrammarParser.INT_TYPE) | (1 << GrammarParser.FLOAT_TYPE) | (1 << GrammarParser.CHAR_TYPE) | (1 << GrammarParser.CONST) | (1 << GrammarParser.RETURN_KW) | (1 << GrammarParser.PLUS) | (1 << GrammarParser.AMP) | (1 << GrammarParser.MINUS) | (1 << GrammarParser.STAR) | (1 << GrammarParser.LEFT_PAREN) | (1 << GrammarParser.INCR) | (1 << GrammarParser.DECR) | (1 << GrammarParser.NOT_OP) | (1 << GrammarParser.PRINT) | (1 << GrammarParser.ID))) != 0):
                self.state = 110
                self.functionArgument()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.COMMA:
                    self.state = 111
                    self.match(GrammarParser.COMMA)
                    self.state = 112
                    self.functionArgument()
                    self.state = 117
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 120
            self.match(GrammarParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def general_expr(self):
            return self.getTypedRuleContext(GrammarParser.General_exprContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_functionArgument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionArgument" ):
                return visitor.visitFunctionArgument(self)
            else:
                return visitor.visitChildren(self)




    def functionArgument(self):

        localctx = GrammarParser.FunctionArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.general_expr()
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
        self.enterRule(localctx, 18, self.RULE_parenCond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(GrammarParser.LEFT_PAREN)
            self.state = 125
            self.general_expr()
            self.state = 126
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
        self.enterRule(localctx, 20, self.RULE_stateOrScope)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
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
        self.enterRule(localctx, 22, self.RULE_construct)
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.IF_KW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.ifConstr()
                pass
            elif token in [GrammarParser.SWITCH_KW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.switchConstr()
                pass
            elif token in [GrammarParser.FOR_KW]:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.forConstr()
                pass
            elif token in [GrammarParser.WHILE_KW]:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.whileConstr()
                pass
            elif token in [GrammarParser.LEFT_C_BRACE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 136
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
        self.enterRule(localctx, 24, self.RULE_scopeConstr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(GrammarParser.LEFT_C_BRACE)
            self.state = 140
            self.block()
            self.state = 141
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
        self.enterRule(localctx, 26, self.RULE_ifConstr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(GrammarParser.IF_KW)
            self.state = 144
            self.parenCond()
            self.state = 145
            self.stateOrScope()
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 146
                self.match(GrammarParser.ELSE_KW)
                self.state = 147
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
        self.enterRule(localctx, 28, self.RULE_switchConstr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(GrammarParser.SWITCH_KW)
            self.state = 151
            self.parenCond()
            self.state = 152
            self.match(GrammarParser.LEFT_C_BRACE)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.CASE_BRANCH:
                self.state = 153
                self.caseBranch()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.DEFAULT_BRANCH:
                self.state = 159
                self.defaultBranch()


            self.state = 162
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
        self.enterRule(localctx, 30, self.RULE_caseBranch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(GrammarParser.CASE_BRANCH)
            self.state = 165
            self.literal()
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
        self.enterRule(localctx, 32, self.RULE_defaultBranch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(GrammarParser.DEFAULT_BRANCH)
            self.state = 170
            self.match(GrammarParser.COLON)
            self.state = 171
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
        self.enterRule(localctx, 34, self.RULE_forConstr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(GrammarParser.FOR_KW)
            self.state = 174
            self.match(GrammarParser.LEFT_PAREN)
            self.state = 175
            self.general_expr()
            self.state = 176
            self.match(GrammarParser.SEMICOLON)
            self.state = 177
            self.general_expr()
            self.state = 178
            self.match(GrammarParser.SEMICOLON)
            self.state = 179
            self.general_expr()
            self.state = 180
            self.match(GrammarParser.RIGHT_PAREN)
            self.state = 181
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
        self.enterRule(localctx, 36, self.RULE_whileConstr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(GrammarParser.WHILE_KW)
            self.state = 184
            self.parenCond()
            self.state = 185
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
        self.enterRule(localctx, 38, self.RULE_general_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.RETURN_KW:
                self.state = 187
                self.match(GrammarParser.RETURN_KW)


            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 190
                self.decl()
                pass

            elif la_ == 2:
                self.state = 191
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 192
                self.printf()
                pass

            elif la_ == 4:
                self.state = 193
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
        self.enterRule(localctx, 40, self.RULE_decl)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.typeObj()
                self.state = 197
                self.identifier()
                self.state = 198
                self.match(GrammarParser.ASSIGN_OP)
                self.state = 199
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.typeObj()
                self.state = 202
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
        self.enterRule(localctx, 42, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 209
                self.match(GrammarParser.LEFT_PAREN)
                self.state = 210
                self.expr(0)
                self.state = 211
                self.match(GrammarParser.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.state = 213
                _la = self._input.LA(1)
                if not(_la==GrammarParser.INCR or _la==GrammarParser.DECR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 214
                self.expr(15)
                pass

            elif la_ == 3:
                self.state = 215
                _la = self._input.LA(1)
                if not(_la==GrammarParser.PLUS or _la==GrammarParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 216
                self.expr(14)
                pass

            elif la_ == 4:
                self.state = 217
                _la = self._input.LA(1)
                if not(_la==GrammarParser.AMP or _la==GrammarParser.STAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 218
                self.expr(13)
                pass

            elif la_ == 5:
                self.state = 219
                self.match(GrammarParser.NOT_OP)
                self.state = 220
                self.expr(12)
                pass

            elif la_ == 6:
                self.state = 221
                self.identifier()
                pass

            elif la_ == 7:
                self.state = 222
                self.literal()
                pass

            elif la_ == 8:
                self.state = 223
                self.functionCall()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 254
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 252
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 226
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 227
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.STAR) | (1 << GrammarParser.SLASH) | (1 << GrammarParser.PERCENT))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 228
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 229
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 230
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.PLUS or _la==GrammarParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 231
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 232
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 233
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.SMALLER_OP or _la==GrammarParser.SMALLER_E_OP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 234
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 235
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 236
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.GREATER_OP or _la==GrammarParser.GREATER_E_OP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 237
                        self.expr(9)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 238
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 239
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.EQUAL_OP or _la==GrammarParser.NOT_EQUAL_OP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 240
                        self.expr(8)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 241
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 242
                        self.match(GrammarParser.AND_OP)
                        self.state = 243
                        self.expr(7)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 244
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 245
                        self.match(GrammarParser.OR_OP)
                        self.state = 246
                        self.expr(6)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 247
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 248
                        self.match(GrammarParser.ASSIGN_OP)
                        self.state = 249
                        self.expr(4)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 250
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 251
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.INCR or _la==GrammarParser.DECR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 256
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
        self.enterRule(localctx, 46, self.RULE_printf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(GrammarParser.PRINT)
            self.state = 258
            self.match(GrammarParser.LEFT_PAREN)
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.CHAR, GrammarParser.INT, GrammarParser.FLOAT]:
                self.state = 259
                self.literal()
                pass
            elif token in [GrammarParser.ID]:
                self.state = 260
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 263
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
        self._predicates[22] = self.expr_sempred
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
         




