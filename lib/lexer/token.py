
from ..types import Types

class Token:

    def __init__(self, tok="", line=0, ttype=Types.KEYWORD):
        self._type = ttype
        self._str = tok
        self._line = line

    def __str__(self):
        return "(%s)[%s] t=%s" % (self._str, self._line, self._type)
