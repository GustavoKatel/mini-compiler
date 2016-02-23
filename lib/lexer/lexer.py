
from ..types import Types

class Lexer:

    def __init__(self, filename):
        self.filename = filename
        self.fd = open(self.filename, 'r')

        self.table = dict()

    def parse(self):
        self.fd.open()

        try:
            self.parseLoop()
        except Exception as e:
            print e
            return None

        return self.table

    def parseLoop(self):
        fd_pos = 0
        char = self.fd.read(1)
        while True:
            if char == ' ': # whitespace
                fd_pos++
                continue
            if char == '': # EOF
                return

            char = self.fd.read(1)

            # a,b) check IDENTIFIER/KEYWORD
            if char.isalpha(): # is alpha
                fd_pos++
                # TODO continue
