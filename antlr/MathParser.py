# Generated from Math.g4 by ANTLR 4.8
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
        buf.write("G\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\5\2\r\n\2\3")
        buf.write("\2\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\7\3\36\n\3\f\3\16\3!\13\3\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\61\n\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\7\5B\n\5\f\5\16\5E\13\5\3\5\2\4\4\b\6\2\4\6\b\2\4")
        buf.write("\3\2\22\24\3\2\f\21\2M\2\22\3\2\2\2\4\27\3\2\2\2\6\"\3")
        buf.write("\2\2\2\b\60\3\2\2\2\n\r\5\4\3\2\13\r\5\b\5\2\f\n\3\2\2")
        buf.write("\2\f\13\3\2\2\2\r\16\3\2\2\2\16\17\7\n\2\2\17\21\3\2\2")
        buf.write("\2\20\f\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2")
        buf.write("\2\2\23\25\3\2\2\2\24\22\3\2\2\2\25\26\7\2\2\3\26\3\3")
        buf.write("\2\2\2\27\30\b\3\1\2\30\31\5\6\4\2\31\37\3\2\2\2\32\33")
        buf.write("\f\4\2\2\33\34\t\2\2\2\34\36\5\4\3\5\35\32\3\2\2\2\36")
        buf.write("!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \5\3\2\2\2!\37\3\2")
        buf.write("\2\2\"#\5\b\5\2#$\t\3\2\2$%\5\b\5\2%\7\3\2\2\2&\'\b\5")
        buf.write("\1\2\'(\7\b\2\2()\5\b\5\2)*\7\t\2\2*\61\3\2\2\2+,\7\5")
        buf.write("\2\2,\61\5\b\5\5-.\7\4\2\2.\61\5\b\5\4/\61\7\3\2\2\60")
        buf.write("&\3\2\2\2\60+\3\2\2\2\60-\3\2\2\2\60/\3\2\2\2\61C\3\2")
        buf.write("\2\2\62\63\f\n\2\2\63\64\7\6\2\2\64B\5\b\5\13\65\66\f")
        buf.write("\t\2\2\66\67\7\7\2\2\67B\5\b\5\n89\f\b\2\29:\7\13\2\2")
        buf.write(":B\5\b\5\t;<\f\7\2\2<=\7\4\2\2=B\5\b\5\b>?\f\6\2\2?@\7")
        buf.write("\5\2\2@B\5\b\5\7A\62\3\2\2\2A\65\3\2\2\2A8\3\2\2\2A;\3")
        buf.write("\2\2\2A>\3\2\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\t\3\2")
        buf.write("\2\2EC\3\2\2\2\b\f\22\37\60AC")
        return buf.getvalue()


class MathParser ( Parser ):

    grammarFileName = "Math.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'('", "')'", "';'", "'%'", "'<'", "'>'", "'=='", "'<='", 
                     "'>='", "'!='", "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "INT", "PLUS", "MINUS", "STAR", "SLASH", 
                      "LEFT_PAREN", "RIGHT_PAREN", "SEMICOLON", "PERCENT", 
                      "SMALLER_OP", "GREATER_OP", "EQUAL_OP", "SMALLER_E_OP", 
                      "GREATER_E_OP", "NOT_EQUAL_OP", "AND_OP", "OR_OP", 
                      "NOT_OP_OP", "WS" ]

    RULE_doc = 0
    RULE_bool_expr = 1
    RULE_comp_expr = 2
    RULE_math_expr = 3

    ruleNames =  [ "doc", "bool_expr", "comp_expr", "math_expr" ]

    EOF = Token.EOF
    INT=1
    PLUS=2
    MINUS=3
    STAR=4
    SLASH=5
    LEFT_PAREN=6
    RIGHT_PAREN=7
    SEMICOLON=8
    PERCENT=9
    SMALLER_OP=10
    GREATER_OP=11
    EQUAL_OP=12
    SMALLER_E_OP=13
    GREATER_E_OP=14
    NOT_EQUAL_OP=15
    AND_OP=16
    OR_OP=17
    NOT_OP_OP=18
    WS=19

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
            return self.getToken(MathParser.EOF, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MathParser.SEMICOLON)
            else:
                return self.getToken(MathParser.SEMICOLON, i)

        def bool_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Bool_exprContext)
            else:
                return self.getTypedRuleContext(MathParser.Bool_exprContext,i)


        def math_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Math_exprContext)
            else:
                return self.getTypedRuleContext(MathParser.Math_exprContext,i)


        def getRuleIndex(self):
            return MathParser.RULE_doc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoc" ):
                listener.enterDoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoc" ):
                listener.exitDoc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoc" ):
                return visitor.visitDoc(self)
            else:
                return visitor.visitChildren(self)




    def doc(self):

        localctx = MathParser.DocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_doc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MathParser.INT) | (1 << MathParser.PLUS) | (1 << MathParser.MINUS) | (1 << MathParser.LEFT_PAREN))) != 0):
                self.state = 10
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 8
                    self.bool_expr(0)
                    pass

                elif la_ == 2:
                    self.state = 9
                    self.math_expr(0)
                    pass


                self.state = 12
                self.match(MathParser.SEMICOLON)
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self.match(MathParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comp_expr(self):
            return self.getTypedRuleContext(MathParser.Comp_exprContext,0)


        def bool_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Bool_exprContext)
            else:
                return self.getTypedRuleContext(MathParser.Bool_exprContext,i)


        def AND_OP(self):
            return self.getToken(MathParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(MathParser.OR_OP, 0)

        def NOT_OP_OP(self):
            return self.getToken(MathParser.NOT_OP_OP, 0)

        def getRuleIndex(self):
            return MathParser.RULE_bool_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_expr" ):
                listener.enterBool_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_expr" ):
                listener.exitBool_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_expr" ):
                return visitor.visitBool_expr(self)
            else:
                return visitor.visitChildren(self)



    def bool_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathParser.Bool_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_bool_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.comp_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 29
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MathParser.Bool_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bool_expr)
                    self.state = 24
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 25
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MathParser.AND_OP) | (1 << MathParser.OR_OP) | (1 << MathParser.NOT_OP_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 26
                    self.bool_expr(3) 
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Comp_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def math_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Math_exprContext)
            else:
                return self.getTypedRuleContext(MathParser.Math_exprContext,i)


        def SMALLER_OP(self):
            return self.getToken(MathParser.SMALLER_OP, 0)

        def GREATER_OP(self):
            return self.getToken(MathParser.GREATER_OP, 0)

        def EQUAL_OP(self):
            return self.getToken(MathParser.EQUAL_OP, 0)

        def SMALLER_E_OP(self):
            return self.getToken(MathParser.SMALLER_E_OP, 0)

        def GREATER_E_OP(self):
            return self.getToken(MathParser.GREATER_E_OP, 0)

        def NOT_EQUAL_OP(self):
            return self.getToken(MathParser.NOT_EQUAL_OP, 0)

        def getRuleIndex(self):
            return MathParser.RULE_comp_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_expr" ):
                listener.enterComp_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_expr" ):
                listener.exitComp_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_expr" ):
                return visitor.visitComp_expr(self)
            else:
                return visitor.visitChildren(self)




    def comp_expr(self):

        localctx = MathParser.Comp_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comp_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.math_expr(0)
            self.state = 33
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MathParser.SMALLER_OP) | (1 << MathParser.GREATER_OP) | (1 << MathParser.EQUAL_OP) | (1 << MathParser.SMALLER_E_OP) | (1 << MathParser.GREATER_E_OP) | (1 << MathParser.NOT_EQUAL_OP))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 34
            self.math_expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Math_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(MathParser.LEFT_PAREN, 0)

        def math_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.Math_exprContext)
            else:
                return self.getTypedRuleContext(MathParser.Math_exprContext,i)


        def RIGHT_PAREN(self):
            return self.getToken(MathParser.RIGHT_PAREN, 0)

        def MINUS(self):
            return self.getToken(MathParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(MathParser.PLUS, 0)

        def INT(self):
            return self.getToken(MathParser.INT, 0)

        def STAR(self):
            return self.getToken(MathParser.STAR, 0)

        def SLASH(self):
            return self.getToken(MathParser.SLASH, 0)

        def PERCENT(self):
            return self.getToken(MathParser.PERCENT, 0)

        def getRuleIndex(self):
            return MathParser.RULE_math_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_expr" ):
                listener.enterMath_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_expr" ):
                listener.exitMath_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath_expr" ):
                return visitor.visitMath_expr(self)
            else:
                return visitor.visitChildren(self)



    def math_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathParser.Math_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_math_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MathParser.LEFT_PAREN]:
                self.state = 37
                self.match(MathParser.LEFT_PAREN)
                self.state = 38
                self.math_expr(0)
                self.state = 39
                self.match(MathParser.RIGHT_PAREN)
                pass
            elif token in [MathParser.MINUS]:
                self.state = 41
                self.match(MathParser.MINUS)
                self.state = 42
                self.math_expr(3)
                pass
            elif token in [MathParser.PLUS]:
                self.state = 43
                self.match(MathParser.PLUS)
                self.state = 44
                self.math_expr(2)
                pass
            elif token in [MathParser.INT]:
                self.state = 45
                self.match(MathParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 63
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MathParser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 49
                        self.match(MathParser.STAR)
                        self.state = 50
                        self.math_expr(9)
                        pass

                    elif la_ == 2:
                        localctx = MathParser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 52
                        self.match(MathParser.SLASH)
                        self.state = 53
                        self.math_expr(8)
                        pass

                    elif la_ == 3:
                        localctx = MathParser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 55
                        self.match(MathParser.PERCENT)
                        self.state = 56
                        self.math_expr(7)
                        pass

                    elif la_ == 4:
                        localctx = MathParser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 57
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 58
                        self.match(MathParser.PLUS)
                        self.state = 59
                        self.math_expr(6)
                        pass

                    elif la_ == 5:
                        localctx = MathParser.Math_exprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_math_expr)
                        self.state = 60
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 61
                        self.match(MathParser.MINUS)
                        self.state = 62
                        self.math_expr(5)
                        pass

             
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self._predicates[1] = self.bool_expr_sempred
        self._predicates[3] = self.math_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def bool_expr_sempred(self, localctx:Bool_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def math_expr_sempred(self, localctx:Math_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         




