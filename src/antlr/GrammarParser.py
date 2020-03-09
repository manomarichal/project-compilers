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
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\7\2\20\n\2\f\2\16\2\23\13\2\3\2\3\2\3\3\5\3\30\n\3\3")
        buf.write("\3\3\3\5\3\34\n\3\3\3\7\3\37\n\3\f\3\16\3\"\13\3\3\3\5")
        buf.write("\3%\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\5\6\67\n\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\7\6M\n\6\f\6\16\6P\13\6\3\6\2\3\n\7\2\4\6\b\n\2\n\3")
        buf.write("\2\6\b\3\2\3\5\5\2\13\13\r\r\34\36\3\2\16\20\4\2\13\13")
        buf.write("\r\r\4\2\24\25\27\30\4\2\26\26\31\31\3\2\34\35\2[\2\21")
        buf.write("\3\2\2\2\4\27\3\2\2\2\6&\3\2\2\2\b+\3\2\2\2\n\66\3\2\2")
        buf.write("\2\f\r\5\6\4\2\r\16\7\23\2\2\16\20\3\2\2\2\17\f\3\2\2")
        buf.write("\2\20\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\24\3\2")
        buf.write("\2\2\23\21\3\2\2\2\24\25\7\2\2\3\25\3\3\2\2\2\26\30\7")
        buf.write("\t\2\2\27\26\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2\2\31 \t")
        buf.write("\2\2\2\32\34\7\t\2\2\33\32\3\2\2\2\33\34\3\2\2\2\34\35")
        buf.write("\3\2\2\2\35\37\7\16\2\2\36\33\3\2\2\2\37\"\3\2\2\2 \36")
        buf.write("\3\2\2\2 !\3\2\2\2!$\3\2\2\2\" \3\2\2\2#%\7\t\2\2$#\3")
        buf.write("\2\2\2$%\3\2\2\2%\5\3\2\2\2&\'\5\4\3\2\'(\7\37\2\2()\7")
        buf.write("\n\2\2)*\5\n\6\2*\7\3\2\2\2+,\t\3\2\2,\t\3\2\2\2-.\b\6")
        buf.write("\1\2./\7\21\2\2/\60\5\n\6\2\60\61\7\22\2\2\61\67\3\2\2")
        buf.write("\2\62\63\t\4\2\2\63\67\5\n\6\13\64\67\7\37\2\2\65\67\5")
        buf.write("\b\5\2\66-\3\2\2\2\66\62\3\2\2\2\66\64\3\2\2\2\66\65\3")
        buf.write("\2\2\2\67N\3\2\2\289\f\n\2\29:\t\5\2\2:M\5\n\6\13;<\f")
        buf.write("\t\2\2<=\t\6\2\2=M\5\n\6\n>?\f\b\2\2?@\t\7\2\2@M\5\n\6")
        buf.write("\tAB\f\7\2\2BC\t\b\2\2CM\5\n\6\bDE\f\6\2\2EF\7\32\2\2")
        buf.write("FM\5\n\6\7GH\f\5\2\2HI\7\33\2\2IM\5\n\6\6JK\f\f\2\2KM")
        buf.write("\t\t\2\2L8\3\2\2\2L;\3\2\2\2L>\3\2\2\2LA\3\2\2\2LD\3\2")
        buf.write("\2\2LG\3\2\2\2LJ\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2")
        buf.write("O\13\3\2\2\2PN\3\2\2\2\n\21\27\33 $\66LN")
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
    RULE_decl = 2
    RULE_literal = 3
    RULE_expr = 4

    ruleNames =  [ "doc", "typeObj", "decl", "literal", "expr" ]

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
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.INT_TYPE) | (1 << GrammarParser.FLOAT_TYPE) | (1 << GrammarParser.CHAR_TYPE) | (1 << GrammarParser.CONST))) != 0):
                self.state = 10
                self.decl()
                self.state = 11
                self.match(GrammarParser.SEMICOLON)
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
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
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.CONST:
                self.state = 20
                self.match(GrammarParser.CONST)


            self.state = 23
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.INT_TYPE) | (1 << GrammarParser.FLOAT_TYPE) | (1 << GrammarParser.CHAR_TYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 25
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==GrammarParser.CONST:
                        self.state = 24
                        self.match(GrammarParser.CONST)


                    self.state = 27
                    self.match(GrammarParser.STAR) 
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.CONST:
                self.state = 33
                self.match(GrammarParser.CONST)


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


        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

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
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.typeObj()
            self.state = 37
            self.match(GrammarParser.ID)
            self.state = 38
            self.match(GrammarParser.ASSIGN_OP)
            self.state = 39
            self.expr(0)
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
        self.enterRule(localctx, 6, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
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

        def MINUS(self):
            return self.getToken(GrammarParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(GrammarParser.PLUS, 0)

        def NOT_OP(self):
            return self.getToken(GrammarParser.NOT_OP, 0)

        def DECR(self):
            return self.getToken(GrammarParser.DECR, 0)

        def INCR(self):
            return self.getToken(GrammarParser.INCR, 0)

        def ID(self):
            return self.getToken(GrammarParser.ID, 0)

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

        def GREATER_OP(self):
            return self.getToken(GrammarParser.GREATER_OP, 0)

        def SMALLER_E_OP(self):
            return self.getToken(GrammarParser.SMALLER_E_OP, 0)

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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.LEFT_PAREN]:
                self.state = 44
                self.match(GrammarParser.LEFT_PAREN)
                self.state = 45
                self.expr(0)
                self.state = 46
                self.match(GrammarParser.RIGHT_PAREN)
                pass
            elif token in [GrammarParser.PLUS, GrammarParser.MINUS, GrammarParser.INCR, GrammarParser.DECR, GrammarParser.NOT_OP]:
                self.state = 48
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.PLUS) | (1 << GrammarParser.MINUS) | (1 << GrammarParser.INCR) | (1 << GrammarParser.DECR) | (1 << GrammarParser.NOT_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 49
                self.expr(9)
                pass
            elif token in [GrammarParser.ID]:
                self.state = 50
                self.match(GrammarParser.ID)
                pass
            elif token in [GrammarParser.CHAR, GrammarParser.INT, GrammarParser.FLOAT]:
                self.state = 51
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 76
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 74
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 55
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.STAR) | (1 << GrammarParser.SLASH) | (1 << GrammarParser.PERCENT))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 56
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 57
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 58
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.PLUS or _la==GrammarParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 59
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 60
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 61
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.SMALLER_OP) | (1 << GrammarParser.GREATER_OP) | (1 << GrammarParser.SMALLER_E_OP) | (1 << GrammarParser.GREATER_E_OP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 62
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 63
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 64
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.EQUAL_OP or _la==GrammarParser.NOT_EQUAL_OP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 65
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 67
                        self.match(GrammarParser.AND_OP)
                        self.state = 68
                        self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 70
                        self.match(GrammarParser.OR_OP)
                        self.state = 71
                        self.expr(4)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 73
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.INCR or _la==GrammarParser.DECR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 78
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 10)
         




