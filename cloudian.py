from parser import parse_tokens
from lexer import read_cloudian_source, lexer
import sys


def interpret(file):
    lines = read_cloudian_source(file)
    tokens = lexer(lines)
    graph = parse_tokens(tokens)
    graph.render('output.gv', view=True)


if __name__ == '__main__':
    interpret(sys.argv[1])
