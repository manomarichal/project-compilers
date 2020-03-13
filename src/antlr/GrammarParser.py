# Generated from src/Grammar.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("h\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\5\2\21\n\2\3\2\3\2\7\2\25\n\2\f\2\16\2\30\13\2\3")
        buf.write("\2\3\2\3\3\5\3\35\n\3\3\3\3\3\5\3!\n\3\3\3\7\3$\n\3\f")
        buf.write("\3\16\3\'\13\3\3\3\5\3*\n\3\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\5\5\66\n\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7G\n\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7c\n\7\f\7\16")
        buf.write("\7f\13\7\3\7\2\3\f\b\2\4\6\b\n\f\2\n\3\2\6\b\3\2\3\5\3")
        buf.write("\2\34\35\4\2\13\13\r\r\3\2\16\20\4\2\24\24\27\27\4\2\25")
        buf.write("\25\30\30\4\2\26\26\31\31\2v\2\26\3\2\2\2\4\34\3\2\2\2")
        buf.write("\6+\3\2\2\2\b\65\3\2\2\2\n\67\3\2\2\2\fF\3\2\2\2\16\21")
        buf.write("\5\b\5\2\17\21\5\f\7\2\20\16\3\2\2\2\20\17\3\2\2\2\21")
        buf.write("\22\3\2\2\2\22\23\7\23\2\2\23\25\3\2\2\2\24\20\3\2\2\2")
        buf.write("\25\30\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\31\3\2\2")
        buf.write("\2\30\26\3\2\2\2\31\32\7\2\2\3\32\3\3\2\2\2\33\35\7\t")
        buf.write("\2\2\34\33\3\2\2\2\34\35\3\2\2\2\35\36\3\2\2\2\36%\t\2")
        buf.write("\2\2\37!\7\t\2\2 \37\3\2\2\2 !\3\2\2\2!\"\3\2\2\2\"$\7")
        buf.write("\16\2\2# \3\2\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&)\3\2")
        buf.write("\2\2\'%\3\2\2\2(*\7\t\2\2)(\3\2\2\2)*\3\2\2\2*\5\3\2\2")
        buf.write("\2+,\7\37\2\2,\7\3\2\2\2-.\5\4\3\2./\5\6\4\2/\60\7\n\2")
        buf.write("\2\60\61\5\f\7\2\61\66\3\2\2\2\62\63\5\4\3\2\63\64\5\6")
        buf.write("\4\2\64\66\3\2\2\2\65-\3\2\2\2\65\62\3\2\2\2\66\t\3\2")
        buf.write("\2\2\678\t\3\2\28\13\3\2\2\29:\b\7\1\2:;\7\21\2\2;<\5")
        buf.write("\f\7\2<=\7\22\2\2=G\3\2\2\2>?\t\4\2\2?G\5\f\7\17@A\t\5")
        buf.write("\2\2AG\5\f\7\16BC\7\36\2\2CG\5\f\7\rDG\5\6\4\2EG\5\n\6")
        buf.write("\2F9\3\2\2\2F>\3\2\2\2F@\3\2\2\2FB\3\2\2\2FD\3\2\2\2F")
        buf.write("E\3\2\2\2Gd\3\2\2\2HI\f\f\2\2IJ\t\6\2\2Jc\5\f\7\rKL\f")
        buf.write("\13\2\2LM\t\5\2\2Mc\5\f\7\fNO\f\n\2\2OP\t\7\2\2Pc\5\f")
        buf.write("\7\13QR\f\t\2\2RS\t\b\2\2Sc\5\f\7\nTU\f\b\2\2UV\t\t\2")
        buf.write("\2Vc\5\f\7\tWX\f\7\2\2XY\7\32\2\2Yc\5\f\7\bZ[\f\6\2\2")
        buf.write("[\\\7\33\2\2\\c\5\f\7\7]^\f\5\2\2^_\7\n\2\2_c\5\f\7\5")
        buf.write("`a\f\20\2\2ac\t\4\2\2bH\3\2\2\2bK\3\2\2\2bN\3\2\2\2bQ")
        buf.write("\3\2\2\2bT\3\2\2\2bW\3\2\2\2bZ\3\2\2\2b]\3\2\2\2b`\3\2")
        buf.write("\2\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2e\r\3\2\2\2fd\3\2\2")
        buf.write("\2\f\20\26\34 %)\65Fbd")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'int'", "'float'", "'char'", "'const'", "'='", "'+'", 
                     "'&'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", "';'", 
                     "'<'", "'>'", "'=='", "'<='", "'>='", "'!='", "'&&'", 
                     "'||'", "'++'", "'--'", "'!'" ]

    symbolicNames = [ "<INVALID>", "CHAR", "INT", "FLOAT", "INT_TYPE", "FLOAT_TYPE", 
                      "CHAR_TYPE", "CONST", "ASSIGN_OP", "PLUS", "AMP", 
                      "MINUS", "STAR", "SLASH", "PERCENT", "LEFT_PAREN", 
                      "RIGHT_PAREN", "SEMICOLON", "SMALLER_OP", "GREATER_OP", 
                      "EQUAL_OP", "SMALLER_E_OP", "GREATER_E_OP", "NOT_EQUAL_OP", 
                      "AND_OP", "OR_OP", "INCR", "DECR", "NOT_OP", "ID", 
                      "WS" ]

    RULE_doc = 0
    RULE_typeObj = 1
    RULE_identifier = 2
    RULE_decl = 3
    RULE_literal = 4
    RULE_expr = 5

    ruleNames =  [ "doc", "typeObj", "identifier", "decl", "literal", "expr" ]

    EOF = Token.EOF
    CHAR=1
    INT=2
    FLOAT=3
    INT_TYPE=4
    FLOAT_TYPE=5
    CHAR_TYPE=6
    CONST=7
    ASSIGN_OP=8
    PLUS=9
    AMP=10
    MINUS=11
    STAR=12
    SLASH=13
    PERCENT=14
    LEFT_PAREN=15
    RIGHT_PAREN=16
    SEMICOLON=17
    SMALLER_OP=18
    GREATER_OP=19
    EQUAL_OP=20
    SMALLER_E_OP=21
    GREATER_E_OP=22
    NOT_EQUAL_OP=23
    AND_OP=24
    OR_OP=25
    INCR=26
    DECR=27
    NOT_OP=28
    ID=29
    WS=30

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

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SEMICOLON)
            else:
                return self.getToken(GrammarParser.SEMICOLON, i)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.DeclContext)
            else:
                return self.getTypedRuleContext(GrammarParser.DeclContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


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
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.CHAR) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT) | (1 << GrammarParser.INT_TYPE) | (1 << GrammarParser.FLOAT_TYPE) | (1 << GrammarParser.CHAR_TYPE) | (1 << GrammarParser.CONST) | (1 << GrammarParser.PLUS) | (1 << GrammarParser.MINUS) | (1 << GrammarParser.LEFT_PAREN) | (1 << GrammarParser.INCR) | (1 << GrammarParser.DECR) | (1 << GrammarParser.NOT_OP) | (1 << GrammarParser.ID))) != 0):
                self.state = 14
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [GrammarParser.INT_TYPE, GrammarParser.FLOAT_TYPE, GrammarParser.CHAR_TYPE, GrammarParser.CONST]:
                    self.state = 12
                    self.decl()
                    pass
                elif token in [GrammarParser.CHAR, GrammarParser.INT, GrammarParser.FLOAT, GrammarParser.PLUS, GrammarParser.MINUS, GrammarParser.LEFT_PAREN, GrammarParser.INCR, GrammarParser.DECR, GrammarParser.NOT_OP, GrammarParser.ID]:
                    self.state = 13
                    self.expr(0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 16
                self.match(GrammarParser.SEMICOLON)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 23
            self.match(GrammarParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_typeObj)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.CONST:
                self.state = 25
                self.match(GrammarParser.CONST)


            self.state = 28
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.INT_TYPE) | (1 << GrammarParser.FLOAT_TYPE) | (1 << GrammarParser.CHAR_TYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 30
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==GrammarParser.CONST:
                        self.state = 29
                        self.match(GrammarParser.CONST)


                    self.state = 32
                    self.match(GrammarParser.STAR) 
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.CONST:
                self.state = 38
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
        self.enterRule(localctx, 4, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(GrammarParser.ID)
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
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.typeObj()
                self.state = 44
                self.identifier()
                self.state = 45
                self.match(GrammarParser.ASSIGN_OP)
                self.state = 46
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.typeObj()
                self.state = 49
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
        self.enterRule(localctx, 8, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
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

        def NOT_OP(self):
            return self.getToken(GrammarParser.NOT_OP, 0)

        def identifier(self):
            return self.getTypedRuleContext(GrammarParser.IdentifierContext,0)


        def literal(self):
            return self.getTypedRuleContext(GrammarParser.LiteralContext,0)


        def STAR(self):
            return self.getToken(GrammarParser.STAR, 0)

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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.LEFT_PAREN]:
                self.state = 56
                self.match(GrammarParser.LEFT_PAREN)
                self.state = 57
                self.expr(0)
                self.state = 58
                self.match(GrammarParser.RIGHT_PAREN)
                pass
            elif token in [GrammarParser.INCR, GrammarParser.DECR]:
                self.state = 60
                _la = self._input.LA(1)
                if not(_la==GrammarParser.INCR or _la==GrammarParser.DECR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 61
                self.expr(13)
                pass
            elif token in [GrammarParser.PLUS, GrammarParser.MINUS]:
                self.state = 62
                _la = self._input.LA(1)
                if not(_la==GrammarParser.PLUS or _la==GrammarParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 63
                self.expr(12)
                pass
            elif token in [GrammarParser.NOT_OP]:
                self.state = 64
                self.match(GrammarParser.NOT_OP)
                self.state = 65
                self.expr(11)
                pass
            elif token in [GrammarParser.ID]:
                self.state = 66
                self.identifier()
                pass
            elif token in [GrammarParser.CHAR, GrammarParser.INT, GrammarParser.FLOAT]:
                self.state = 67
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 98
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 96
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 70
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 71
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.STAR) | (1 << GrammarParser.SLASH) | (1 << GrammarParser.PERCENT))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 72
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 73
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 74
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.PLUS or _la==GrammarParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 75
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 76
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 77
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.SMALLER_OP or _la==GrammarParser.SMALLER_E_OP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 78
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 79
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 80
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.GREATER_OP or _la==GrammarParser.GREATER_E_OP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 81
                        self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 82
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 83
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.EQUAL_OP or _la==GrammarParser.NOT_EQUAL_OP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 84
                        self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 86
                        self.match(GrammarParser.AND_OP)
                        self.state = 87
                        self.expr(6)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 88
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 89
                        self.match(GrammarParser.OR_OP)
                        self.state = 90
                        self.expr(5)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 91
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 92
                        self.match(GrammarParser.ASSIGN_OP)
                        self.state = 93
                        self.expr(3)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 94
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 95
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.INCR or _la==GrammarParser.DECR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 100
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 14)
         




