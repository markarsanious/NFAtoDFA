import argparse
from antlr4 import *
from task_2_1Lexer import task_2_1Lexer
from task_2_1Listener import task_2_1Listener
from task_2_1Parser import task_2_1Parser
from antlr4.tree.Trees import Trees

def get_token_type(token):
    if token.type == task_2_1Lexer.NEWLINE:
        return ""
    elif token.type == task_2_1Lexer.COMMAND:
        return "COMMAND"
    elif token.type == task_2_1Lexer.REG:
        return "REG"
    elif token.type == task_2_1Lexer.MEMORY:
        return "MEMORY"
    elif token.type == task_2_1Lexer.IMMEDIATE:
        return "IMMEDIATE"
    else:
        return "ERROR UNKNOWN TOKEN"

def main():

    with open(args.file, "r") as file:
        lines = file.read()
        lines = lines.replace(",","")
        lines = lines.replace(" ", "")
    input_stream = InputStream(lines)
    lexer = task_2_1Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = task_2_1Parser(token_stream)

 #   tree = parser.start()
 #   print(Trees.toStringTree(tree,None, parser))

    token = lexer.nextToken()

    while not token.type == Token.EOF:
        if not (get_token_type(token) == ""):
            output_file.write(get_token_type(token) + " " + token.text + "\n")
            print(get_token_type(token), token.text)
        token = lexer.nextToken()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?", metavar="file")

    args = parser.parse_args()

    output_file = open("task_2_1_result.txt", "w+")

    main()	