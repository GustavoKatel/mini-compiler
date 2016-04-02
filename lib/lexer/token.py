
from ..types import Types


class Token:

    def __init__(self, tok="", line=0, ttype=Types.KEYWORD, stype="", index=0):
        self.type = ttype
        self.str = tok
        self.line = line
        self.index = 0
        if stype=="":
            self.semantic_type = Types.MARKER
        else:
            self.semantic_type = stype

    def get_tuple(self):
        type_str = Types.typeToStr(self.type)
        return (self.str, type_str, self.line)

    def __str__(self):
        type_str = Types.typeToStr(self.type)

        template = "{0:10} {1:20} {2:5}"  # column widths: 10, 20, 5

        if len(type_str.split(' ')) > 1:
            return template.format(self.str, type_str, self.line)
        else:
            return template.format(self.str, type_str, self.line)
