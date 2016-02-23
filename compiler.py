
from lib.lexer import Lexer

lexer = Lexer('sources/example1.pas')

table = lexer.parse()

# TODO serialize table to file
