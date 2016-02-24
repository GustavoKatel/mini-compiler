# -*- coding: utf-8


class Types:

    KEYWORD = 1
    IDENTIFIER = 2
    NUMBER_INT = 3
    NUMBER_REAL = 4
    DELIMTER = 5
    CMD_ATTR = 6
    RELATIONAL_OPERATOR = 7
    ADD_OPERATOR = 8
    MUL_OPERATOR = 9

    KEYWORD_LIST = ["program", "var", "integer", "real", "boolean",
                    "procedure", "begin", "end", "if", "then", "else", "while",
                    "do", "not"]

    DELIMTER_LIST = [";", ".", ":", "(", ")", ","]

    CMD_ATTR_STR = ":="

    RELATIONAL_OPERATOR_LIST = ["=", "<", ">", "<=", ">=", "<>"]

    ADD_OPERATOR_LIST = ["+", "-"]

    MUL_OPERATOR_LIST = ["*", "/"]

    COMMENT_OPEN = '{'

    COMMENT_CLOSE = '}'

    @staticmethod
    def typeToStr(t):
        if t == Types.KEYWORD:
            return 'Palavra reservada'
        elif t == Types.IDENTIFIER:
            return 'Identificador'
        elif t == Types.NUMBER_INT:
            return 'Numero inteiro'
        elif t == Types.NUMBER_REAL:
            return 'Numero real'
        elif t == Types.DELIMTER:
            return 'Delimitador'
        elif t == Types.CMD_ATTR:
            return 'Delimitador'
        elif t == Types.RELATIONAL_OPERATOR:
            return 'Operador relacional'
        elif t == Types.ADD_OPERATOR:
            return 'Operador aditivo'
        elif t == Types.MUL_OPERATOR:
            return 'Operador multiplicativo'
        else:
            return 'Não identificado'
