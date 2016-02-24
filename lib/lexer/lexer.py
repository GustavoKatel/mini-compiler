
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
            raise e

        return self.tokens

    def parseLoop(self):
        fd_pos = 0
        char = None
        line = 1
        token_str = ""
        comment_count = 0
        while True:
            char = self.fd.read(1)
            fd_pos += 1

            # whitespace, carrier, tabs
            if char == ' ' or char == '\r' or char == '\t':
                continue

            elif char == '':  # EOF
                if comment_count > 0:
                    raise Exception('Invalid syntax. Comment section not closed')
                return

            elif char == '\n':  # new line
                line += 1
                continue

            elif char == Types.COMMENT_OPEN:  # open comment section
                comment_count += 1
                continue

            elif char == Types.COMMENT_CLOSE:  # close comment section
                comment_count -= 1
                if comment_count < 0:
                    raise Exception('Invalid syntax in line %s. Invalid comment operator' % line)
                continue

            elif comment_count:  # ignore comments
                continue

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
                # print "Found token: %s" % token

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
                # print "Found token: %s" % token

            # g) Relational operators
            # elif char in Types.RELATIONAL_OPERATOR_LIST:
            elif self._in_list_first_char(char, Types.RELATIONAL_OPERATOR_LIST):
                token_str = ""
                while True:
                    if not self._in_list_starts_with(token_str+char, Types.RELATIONAL_OPERATOR_LIST):
                        fd_pos -= 1
                        self.fd.seek(fd_pos)
                        break
                    token_str += char
                    char = self.fd.read(1)
                    fd_pos += 1
                    if char == '':
                        break

                # we have a token
                token = Token(token_str, line, Types.RELATIONAL_OPERATOR)
                self.tokens.append(token)

            # h) additive operators
            elif self._in_list_starts_with(char, Types.ADD_OPERATOR_LIST):

                token_str = ""
                while True:
                    if not self._in_list_starts_with(token_str+char, Types.ADD_OPERATOR_LIST):
                        fd_pos -= 1
                        self.fd.seek(fd_pos)
                        break
                    token_str += char
                    char = self.fd.read(1)
                    fd_pos += 1
                    if char == '':
                        break

                token = Token(token_str, line, Types.ADD_OPERATOR)
                self.tokens.append(token)

            #  i) multiplicative operators
            elif self._in_list_starts_with(char, Types.MUL_OPERATOR_LIST):

                token_str = ""
                while True:
                    if not self._in_list_starts_with(token_str+char, Types.MUL_OPERATOR_LIST):
                        fd_pos -= 1
                        self.fd.seek(fd_pos)
                        break
                    token_str += char
                    char = self.fd.read(1)
                    fd_pos += 1
                    if char == '':
                        break

                token = Token(token_str, line, Types.MUL_OPERATOR)
                self.tokens.append(token)

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
                # print "Found token: %s" % token

            else:
                raise Exception('Invalid symbol in line: %s col: %s symbol: %s'
                                % (line, fd_pos, char))

    def _in_list_first_char(self, char, mlist):
        for item in mlist:
            if char == item[0]:
                return True
        return False

    def _in_list_starts_with(self, str, mlist):
        for item in mlist:
            if item.startswith(str):
                return True
        return False
