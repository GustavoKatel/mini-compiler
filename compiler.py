# -*- coding: utf-8 -*-

import sys
from lib.lexer import Lexer

fname = 'sources/example1.pas'

if len(sys.argv) > 1:
    fname = sys.argv[1]

lexer = Lexer(fname)

tokens = lexer.parse()

template = "{0:10} {1:20} {2:5}"  # column widths: 10, 20, 5

print template.format('Token', 'Classificacao', 'Linha')

for tok in tokens:
    print template.format(*tok.get_tuple())

# TODO serialize table to file
