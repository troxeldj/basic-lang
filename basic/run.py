from .Lexer import Lexer
from .Parser import Parser
def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    
    parser = Parser(tokens)
    ast = parser.parse()

    return ast.node, ast.error
