# Generated from task_2_1.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3")
        buf.write("\2\7\2\20\n\2\f\2\16\2\23\13\2\3\3\3\3\3\3\5\3\30\n\3")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\5\5+\n\5\3\6\3\6\3\6\3\6\5\6\61\n\6\3\6")
        buf.write("\2\2\7\2\4\6\b\n\2\2\2\65\2\21\3\2\2\2\4\27\3\2\2\2\6")
        buf.write("\31\3\2\2\2\b*\3\2\2\2\n\60\3\2\2\2\f\r\5\4\3\2\r\16\7")
        buf.write("\3\2\2\16\20\3\2\2\2\17\f\3\2\2\2\20\23\3\2\2\2\21\17")
        buf.write("\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23\21\3\2\2\2\24\30")
        buf.write("\5\6\4\2\25\30\5\b\5\2\26\30\5\n\6\2\27\24\3\2\2\2\27")
        buf.write("\25\3\2\2\2\27\26\3\2\2\2\30\5\3\2\2\2\31\32\7\4\2\2\32")
        buf.write("\7\3\2\2\2\33\34\7\4\2\2\34\35\7\5\2\2\35+\7\6\2\2\36")
        buf.write("\37\7\4\2\2\37 \7\6\2\2 +\7\5\2\2!\"\7\4\2\2\"#\7\5\2")
        buf.write("\2#+\7\5\2\2$%\7\4\2\2%&\7\6\2\2&+\7\7\2\2\'(\7\4\2\2")
        buf.write("()\7\5\2\2)+\7\7\2\2*\33\3\2\2\2*\36\3\2\2\2*!\3\2\2\2")
        buf.write("*$\3\2\2\2*\'\3\2\2\2+\t\3\2\2\2,-\7\4\2\2-\61\7\5\2\2")
        buf.write("./\7\4\2\2/\61\7\6\2\2\60,\3\2\2\2\60.\3\2\2\2\61\13\3")
        buf.write("\2\2\2\6\21\27*\60")
        return buf.getvalue()


class task_2_1Parser ( Parser ):

    grammarFileName = "task_2_1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "NEWLINE", "COMMAND", "REG", "MEMORY", 
                      "IMMEDIATE" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_aaa = 2
    RULE_add = 3
    RULE_inc = 4

    ruleNames =  [ "start", "expr", "aaa", "add", "inc" ]

    EOF = Token.EOF
    NEWLINE=1
    COMMAND=2
    REG=3
    MEMORY=4
    IMMEDIATE=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(task_2_1Parser.ExprContext)
            else:
                return self.getTypedRuleContext(task_2_1Parser.ExprContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(task_2_1Parser.NEWLINE)
            else:
                return self.getToken(task_2_1Parser.NEWLINE, i)

        def getRuleIndex(self):
            return task_2_1Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = task_2_1Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==task_2_1Parser.COMMAND:
                self.state = 10
                self.expr()
                self.state = 11
                self.match(task_2_1Parser.NEWLINE)
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def aaa(self):
            return self.getTypedRuleContext(task_2_1Parser.AaaContext,0)


        def add(self):
            return self.getTypedRuleContext(task_2_1Parser.AddContext,0)


        def inc(self):
            return self.getTypedRuleContext(task_2_1Parser.IncContext,0)


        def getRuleIndex(self):
            return task_2_1Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = task_2_1Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.aaa()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.add()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.inc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AaaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMAND(self):
            return self.getToken(task_2_1Parser.COMMAND, 0)

        def getRuleIndex(self):
            return task_2_1Parser.RULE_aaa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAaa" ):
                listener.enterAaa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAaa" ):
                listener.exitAaa(self)




    def aaa(self):

        localctx = task_2_1Parser.AaaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_aaa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(task_2_1Parser.COMMAND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMAND(self):
            return self.getToken(task_2_1Parser.COMMAND, 0)

        def REG(self, i:int=None):
            if i is None:
                return self.getTokens(task_2_1Parser.REG)
            else:
                return self.getToken(task_2_1Parser.REG, i)

        def MEMORY(self):
            return self.getToken(task_2_1Parser.MEMORY, 0)

        def IMMEDIATE(self):
            return self.getToken(task_2_1Parser.IMMEDIATE, 0)

        def getRuleIndex(self):
            return task_2_1Parser.RULE_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)




    def add(self):

        localctx = task_2_1Parser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_add)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(task_2_1Parser.COMMAND)
                self.state = 26
                self.match(task_2_1Parser.REG)
                self.state = 27
                self.match(task_2_1Parser.MEMORY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(task_2_1Parser.COMMAND)
                self.state = 29
                self.match(task_2_1Parser.MEMORY)
                self.state = 30
                self.match(task_2_1Parser.REG)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(task_2_1Parser.COMMAND)
                self.state = 32
                self.match(task_2_1Parser.REG)
                self.state = 33
                self.match(task_2_1Parser.REG)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.match(task_2_1Parser.COMMAND)
                self.state = 35
                self.match(task_2_1Parser.MEMORY)
                self.state = 36
                self.match(task_2_1Parser.IMMEDIATE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 37
                self.match(task_2_1Parser.COMMAND)
                self.state = 38
                self.match(task_2_1Parser.REG)
                self.state = 39
                self.match(task_2_1Parser.IMMEDIATE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMAND(self):
            return self.getToken(task_2_1Parser.COMMAND, 0)

        def REG(self):
            return self.getToken(task_2_1Parser.REG, 0)

        def MEMORY(self):
            return self.getToken(task_2_1Parser.MEMORY, 0)

        def getRuleIndex(self):
            return task_2_1Parser.RULE_inc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInc" ):
                listener.enterInc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInc" ):
                listener.exitInc(self)




    def inc(self):

        localctx = task_2_1Parser.IncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_inc)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(task_2_1Parser.COMMAND)
                self.state = 43
                self.match(task_2_1Parser.REG)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(task_2_1Parser.COMMAND)
                self.state = 45
                self.match(task_2_1Parser.MEMORY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





