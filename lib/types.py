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
    NUMBER_COMPLEX = 10
    LOGICAL_OPERATOR = 11
    MARKER = 12

    KEYWORD_LIST = ["program", "var", "integer", "real", "boolean",
                    "procedure", "begin", "end", "if", "then", "else", "while",
                    "do", "not", "true", "false"]

    DELIMTER_LIST = [";", ".", ":", "(", ")", ","]

    CMD_ATTR_STR = ":="

    RELATIONAL_OPERATOR_LIST = ["=", "<", ">", "<=", ">=", "<>"]

    ADD_OPERATOR_LIST = ["+", "-", "or"]

    MUL_OPERATOR_LIST = ["*", "/", "and"]

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
            return 'Comando atribuicao'
        elif t == Types.RELATIONAL_OPERATOR:
            return 'Operador relacional'
        elif t == Types.ADD_OPERATOR:
            return 'Operador aditivo'
        elif t == Types.MUL_OPERATOR:
            return 'Operador multiplicativo'
        elif t == Types.NUMBER_COMPLEX:
            return 'Número complexo'
        elif t == Types.LOGICAL_OPERATOR:
            return 'Operador lógico'
        else:
            return 'Não identificado'
