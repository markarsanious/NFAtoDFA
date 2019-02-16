# Generated from task_2_1.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2")
        buf.write("\17\n\2\r\2\16\2\20\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3\34\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4&\n\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\6\6.\n\6\r\6\16\6/\3\6\6\6\63")
        buf.write("\n\6\r\6\16\6\64\3\6\5\68\n\6\2\2\7\3\3\5\4\7\5\t\6\13")
        buf.write("\7\3\2\4\4\2\f\f\17\17\3\2\62;\2A\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3\16\3\2\2\2")
        buf.write("\5\33\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13\67\3\2\2\2\r\17")
        buf.write("\t\2\2\2\16\r\3\2\2\2\17\20\3\2\2\2\20\16\3\2\2\2\20\21")
        buf.write("\3\2\2\2\21\4\3\2\2\2\22\23\7C\2\2\23\24\7C\2\2\24\34")
        buf.write("\7C\2\2\25\26\7C\2\2\26\27\7F\2\2\27\34\7F\2\2\30\31\7")
        buf.write("K\2\2\31\32\7P\2\2\32\34\7E\2\2\33\22\3\2\2\2\33\25\3")
        buf.write("\2\2\2\33\30\3\2\2\2\34\6\3\2\2\2\35\36\7C\2\2\36&\7Z")
        buf.write("\2\2\37 \7D\2\2 &\7Z\2\2!\"\7E\2\2\"&\7Z\2\2#$\7F\2\2")
        buf.write("$&\7Z\2\2%\35\3\2\2\2%\37\3\2\2\2%!\3\2\2\2%#\3\2\2\2")
        buf.write("&\b\3\2\2\2\'(\7]\2\2()\7C\2\2)*\7Z\2\2*+\7_\2\2+\n\3")
        buf.write("\2\2\2,.\t\3\2\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2")
        buf.write("\2\2\608\3\2\2\2\61\63\4\62\63\2\62\61\3\2\2\2\63\64\3")
        buf.write("\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\66\3\2\2\2\668\7")
        buf.write("d\2\2\67-\3\2\2\2\67\62\3\2\2\28\f\3\2\2\2\t\2\20\33%")
        buf.write("/\64\67\2")
        return buf.getvalue()


class task_2_1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NEWLINE = 1
    COMMAND = 2
    REG = 3
    MEMORY = 4
    IMMEDIATE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "COMMAND", "REG", "MEMORY", "IMMEDIATE" ]

    ruleNames = [ "NEWLINE", "COMMAND", "REG", "MEMORY", "IMMEDIATE" ]

    grammarFileName = "task_2_1.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


