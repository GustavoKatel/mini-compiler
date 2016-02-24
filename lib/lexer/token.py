
from ..types import Types


class Token:

    def __init__(self, tok="", line=0, ttype=Types.KEYWORD):
        self._type = ttype
        self._str = tok
        self._line = line

    def get_tuple(self):
        type_str = Types.typeToStr(self._type)
        return (self._str, type_str, self._line)

    def __str__(self):
        type_str = Types.typeToStr(self._type)

        template = "{0:10} {1:20} {2:5}"  # column widths: 10, 20, 5

        if len(type_str.split(' ')) > 1:
            return template.format(self._str, type_str, self._line)
        else:
            return template.format(self._str, type_str, self._line)
