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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("F\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\5\2\r\n\2\3")
        buf.write("\2\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3 \n\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\7\3(\n\3\f\3\16\3+\13\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\59\n\5\3\5\3\5\3\5\3\5\3\5\3\5\7")
        buf.write("\5A\n\5\f\5\16\5D\13\5\3\5\2\4\4\b\6\2\4\6\b\2\5\3\2\f")
        buf.write("\21\3\2\4\5\3\2\6\b\2K\2\22\3\2\2\2\4\37\3\2\2\2\6,\3")
        buf.write("\2\2\2\b8\3\2\2\2\n\r\5\4\3\2\13\r\5\b\5\2\f\n\3\2\2\2")
        buf.write("\f\13\3\2\2\2\r\16\3\2\2\2\16\17\7\13\2\2\17\21\3\2\2")
        buf.write("\2\20\f\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2")
        buf.write("\2\2\23\25\3\2\2\2\24\22\3\2\2\2\25\26\7\2\2\3\26\3\3")
        buf.write("\2\2\2\27\30\b\3\1\2\30\31\7\t\2\2\31\32\5\4\3\2\32\33")
        buf.write("\7\n\2\2\33 \3\2\2\2\34\35\7\24\2\2\35 \5\4\3\6\36 \5")
        buf.write("\6\4\2\37\27\3\2\2\2\37\34\3\2\2\2\37\36\3\2\2\2 )\3\2")
        buf.write("\2\2!\"\f\5\2\2\"#\7\22\2\2#(\5\4\3\6$%\f\4\2\2%&\7\23")
        buf.write("\2\2&(\5\4\3\5\'!\3\2\2\2\'$\3\2\2\2(+\3\2\2\2)\'\3\2")
        buf.write("\2\2)*\3\2\2\2*\5\3\2\2\2+)\3\2\2\2,-\5\b\5\2-.\t\2\2")
        buf.write("\2./\5\b\5\2/\7\3\2\2\2\60\61\b\5\1\2\61\62\7\t\2\2\62")
        buf.write("\63\5\b\5\2\63\64\7\n\2\2\649\3\2\2\2\65\66\t\3\2\2\66")
        buf.write("9\5\b\5\6\679\7\3\2\28\60\3\2\2\28\65\3\2\2\28\67\3\2")
        buf.write("\2\29B\3\2\2\2:;\f\5\2\2;<\t\4\2\2<A\5\b\5\6=>\f\4\2\2")
        buf.write(">?\t\3\2\2?A\5\b\5\5@:\3\2\2\2@=\3\2\2\2AD\3\2\2\2B@\3")
        buf.write("\2\2\2BC\3\2\2\2C\t\3\2\2\2DB\3\2\2\2\n\f\22\37\')8@B")
        return buf.getvalue()


class GrammarParser(Parser):
    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'",
                    "'%'", "'('", "')'", "';'", "'<'", "'>'", "'=='", "'<='",
                    "'>='", "'!='", "'&&'", "'||'", "'!'"]

    symbolicNames = ["<INVALID>", "INT", "PLUS", "MINUS", "STAR", "SLASH",
                     "PERCENT", "LEFT_PAREN", "RIGHT_PAREN", "SEMICOLON",
                     "SMALLER_OP", "GREATER_OP", "EQUAL_OP", "SMALLER_E_OP",
                     "GREATER_E_OP", "NOT_EQUAL_OP", "AND_OP", "OR_OP",
                     "NOT_OP", "WS"]

    RULE_doc = 0
    RULE_bool_expr = 1
    RULE_comp_expr = 2
    RULE_math_expr = 3

    ruleNames = ["doc", "bool_expr", "comp_expr", "math_expr"]

    EOF = Token.EOF
    INT = 1
    PLUS = 2
    MINUS = 3
    STAR = 4
    SLASH = 5
    PERCENT = 6
    LEFT_PAREN = 7
    RIGHT_PAREN = 8
    SEMICOLON = 9
    SMALLER_OP = 10
    GREATER_OP = 11
    EQUAL_OP = 12
    SMALLER_E_OP = 13
    GREATER_E_OP = 14
    NOT_EQUAL_OP = 15
    AND_OP = 16
    OR_OP = 17
    NOT_OP = 18
    WS = 19

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class DocContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def SEMICOLON(self, i: int = None):
            if i is None:
                return self.getTokens(GrammarParser.SEMICOLON)
            else:
                return self.getToken(GrammarParser.SEMICOLON, i)

        def bool_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Bool_exprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Bool_exprContext, i)

        def math_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Math_exprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Math_exprContext, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_doc

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitDoc"):
                return visitor.visitDoc(self)
            else:
                return visitor.visitChildren(self)

    def doc(self):

        localctx = GrammarParser.DocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_doc)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << GrammarParser.INT) | (1 << GrammarParser.PLUS) | (1 << GrammarParser.MINUS) | (
                    1 << GrammarParser.LEFT_PAREN) | (1 << GrammarParser.NOT_OP))) != 0):
                self.state = 10
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 0, self._ctx)
                if la_ == 1:
                    self.state = 8
                    self.bool_expr(0)
                    pass

                elif la_ == 2:
                    self.state = 9
                    self.math_expr(0)
                    pass

                self.state = 12
                self.match(GrammarParser.SEMICOLON)
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self.match(GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Bool_exprContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(GrammarParser.LEFT_PAREN, 0)

        def bool_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Bool_exprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Bool_exprContext, i)

        def RIGHT_PAREN(self):
            return self.getToken(GrammarParser.RIGHT_PAREN, 0)

        def NOT_OP(self):
            return self.getToken(GrammarParser.NOT_OP, 0)

        def comp_expr(self):
            return self.getTypedRuleContext(GrammarParser.Comp_exprContext, 0)

        def AND_OP(self):
            return self.getToken(GrammarParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(GrammarParser.OR_OP, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_bool_expr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBool_expr"):
                return visitor.visitBool_expr(self)
            else:
                return visitor.visitChildren(self)

    def bool_expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.Bool_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_bool_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 2, self._ctx)
            if la_ == 1:
                self.state = 22
                self.match(GrammarParser.LEFT_PAREN)
                self.state = 23
                self.bool_expr(0)
                self.state = 24
                self.match(GrammarParser.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.state = 26
                self.match(GrammarParser.NOT_OP)
                self.state = 27
                self.bool_expr(4)
                pass

            elif la_ == 3:
                self.state = 28
                self.comp_expr()
                pass

            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 3, self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.Bool_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bool_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 32
                        self.match(GrammarParser.AND_OP)
                        self.state = 33
                        self.bool_expr(4)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.Bool_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bool_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 35
                        self.match(GrammarParser.OR_OP)
                        self.state = 36
                        self.bool_expr(3)
                        pass

                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Comp_exprContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def math_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Math_exprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Math_exprContext, i)

        def SMALLER_OP(self):
            return self.getToken(GrammarParser.SMALLER_OP, 0)

        def GREATER_OP(self):
            return self.getToken(GrammarParser.GREATER_OP, 0)

        def EQUAL_OP(self):
            return self.getToken(GrammarParser.EQUAL_OP, 0)

        def SMALLER_E_OP(self):
            return self.getToken(GrammarParser.SMALLER_E_OP, 0)

        def GREATER_E_OP(self):
            return self.getToken(GrammarParser.GREATER_E_OP, 0)

        def NOT_EQUAL_OP(self):
            return self.getToken(GrammarParser.NOT_EQUAL_OP, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_comp_expr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitComp_expr"):
                return visitor.visitComp_expr(self)
            else:
                return visitor.visitChildren(self)

    def comp_expr(self):

        localctx = GrammarParser.Comp_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comp_expr)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.math_expr(0)
            self.state = 43
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << GrammarParser.SMALLER_OP) | (1 << GrammarParser.GREATER_OP) | (
                    1 << GrammarParser.EQUAL_OP) | (1 << GrammarParser.SMALLER_E_OP) | (
                            1 << GrammarParser.GREATER_E_OP) | (1 << GrammarParser.NOT_EQUAL_OP))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 44
            self.math_expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Math_exprContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(GrammarParser.LEFT_PAREN, 0)

        def math_expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Math_exprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.Math_exprContext, i)

        def RIGHT_PAREN(self):
            return self.getToken(GrammarParser.RIGHT_PAREN, 0)

        def MINUS(self):
            return self.getToken(GrammarParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(GrammarParser.PLUS, 0)

        def INT(self):
            return self.getToken(GrammarParser.INT, 0)

        def STAR(self):
            return self.getToken(GrammarParser.STAR, 0)

        def SLASH(self):
            return self.getToken(GrammarParser.SLASH, 0)

        def PERCENT(self):
            return self.getToken(GrammarParser.PERCENT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_math_expr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMath_expr"):
                return visitor.visitMath_expr(self)
            else:
                return visitor.visitChildren(self)

    def math_expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.Math_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_math_expr, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.LEFT_PAREN]:
                self.state = 47
                self.match(GrammarParser.LEFT_PAREN)
                self.state = 48
                self.math_expr(0)
                self.state = 49
                self.match(GrammarParser.RIGHT_PAREN)
                pass
            elif token in [GrammarParser.PLUS, GrammarParser.MINUS]:
                self.state = 51
                _la = self._input.LA(1)
                if not (_la == GrammarParser.PLUS or _la == GrammarParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 52
                self.math_expr(4)
                pass
            elif token in [GrammarParser.INT]:
                self.state = 53
                self.match(GrammarParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 7, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 62
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 6, self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 57
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                                (1 << GrammarParser.STAR) | (1 << GrammarParser.SLASH) | (
                                1 << GrammarParser.PERCENT))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 58
                        self.math_expr(4)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 60
                        _la = self._input.LA(1)
                        if not (_la == GrammarParser.PLUS or _la == GrammarParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 61
                        self.math_expr(3)
                        pass

                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 7, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.bool_expr_sempred
        self._predicates[3] = self.math_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def bool_expr_sempred(self, localctx: Bool_exprContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 3)

        if predIndex == 1:
            return self.precpred(self._ctx, 2)

    def math_expr_sempred(self, localctx: Math_exprContext, predIndex: int):
        if predIndex == 2:
            return self.precpred(self._ctx, 3)

        if predIndex == 3:
            return self.precpred(self._ctx, 2)
