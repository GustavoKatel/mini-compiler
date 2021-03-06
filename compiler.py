# -*- coding: utf-8 -*-

import sys, traceback
from lib.lexer import Lexer
from lib.syntactic import Syntactic

fname = 'sources/example1.pas'

if len(sys.argv) > 1:
    fname = sys.argv[1]

lexer = Lexer(fname)

try:
    tokens = lexer.parse()
except Exception as e:
    print e
    sys.exit(1)

template = "{0:10} {1:25} {2:5}"  # column widths: 10, 20, 5

# print template.format('Token', 'Classificacao', 'Linha')

# for tok in tokens:
#     print template.format(*tok.get_tuple())

syntactic = Syntactic(tokens)
try:
    if syntactic.parse() == False:
        print "Erro sintático"
except Exception as e:
    # traceback.print_exc()
    print str(e)

# TODO serialize table to file
