
from ..types import Types
from token import Token


class Lexer:

    def __init__(self, filename):
        self.filename = filename
        self.fd = open(self.filename, 'r')

        self.tokens = []

    def parse(self):
        try:
            self.parseLoop()
        except Exception as e:
            print e
            return None

        return self.tokens

    def parseLoop(self):
        fd_pos = 0
        char = None
        line = 0
        token_str = ""
        while True:
            char = self.fd.read(1)
            fd_pos += 1

            if char == ' ' or  # whitespace
            char == '\r' or  # ignore carrier
            char == '\t':  # ignore tabs
                continue

            elif char == '':  # EOF
                return

            elif char == '\n':  # new line
                line += 1
                continue

            # a,b) check IDENTIFIER/KEYWORD
            elif char.isalpha():  # is alpha
                token_str = char

                while True:  # tries to match a word
                    char = self.fd.read(1)
                    fd_pos += 1
                    if char.isalnum() or char == '_':  # letters, numbers and _
                        token_str += char
                        continue
                    elif char == '':  # EOF
                        break
                    else:  # not a word
                        fd_pos -= 1
                        self.fd.seek(fd_pos)  # go back one char
                        break

                # we have a token at token_str.
                if token_str in Types.KEYWORD_LIST:  # it is a keyword
                    token = Token(token_str, line, Types.KEYWORD)
                else:
                    token = Token(token_str, line, Types.IDENTIFIER)
                self.tokens.append(token)
                print "Found token: %s" % token

            # c,d) check NUMBER
            elif char.isdigit():
                token_str = char
                found_float = False

                while True:  # tries to match a number
                    char = self.fd.read(1)
                    fd_pos += 1
                    if char.isdigit():  # numbers
                        token_str += char
                        continue
                    elif char == '.':  # floating point
                        token_str += char
                        found_float = True
                        continue
                    else:  # something else
                        fd_pos -= 1
                        self.fd.seek(fd_pos)
                        break

                # we have a token at token_str
                if found_float:
                    token = Token(token_str, line, Types.NUMBER_REAL)
                else:
                    token = Token(token_str, line, Types.NUMBER_INT)
                self.tokens.append(token)
                print "Found token: %s" % token

            # e,f) delimiter. Also checks the CMD_ATTR
            elif char in Types.DELIMTER_LIST:

                token_str = char
                ttype = Types.DELIMTER

                # matches the first char of CMD_ATTR_STR
                if char == Types.CMD_ATTR_STR[0]:
                    next_char = self.fd.read(1)
                    if next_char == Types.CMD_ATTR_STR[1]:  # it is CMD_ATTR
                        fd_pos += 1
                        token_str += next_char
                        ttype = Types.CMD_ATTR
                    else:
                        self.fd.seek(fd_pos)  # go back

                token = Token(token_str, line, ttype)
                self.tokens.append(token)
                print "Found token: %s" % token

            # g) Relational operators
            elif char in Types.RELATIONAL_OPERATOR_LIST:
                token_str = ""
                while token_str+char in Types.RELATIONAL_OPERATOR_LIST:
                    token_str += char
                    char = self.fd.read(1)
                    fd_pos += 1
