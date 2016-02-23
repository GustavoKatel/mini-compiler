
class Types:

    KEYWORD = 1
    IDENTIFIER = 2
    NUMBER_INT = 3
    NUMBER_REAL = 4
    DELIMTER = 5
    CMD_ATTR = 6
    RELATIONAL_OPERATOR = 7
    OPERATOR_ADD = 8
    OPERATOR_MUL = 9

    KEYWORD_LIST = ["program", "var", "integer", "real", "boolean",
                    "procedure", "begin", "end", "if", "then", "else", "while",
                    "do", "not"]

    DELIMTER_LIST = [";", ".", ":", "(", ")", ","]

    CMD_ATTR_STR = ":="

    RELATIONAL_OPERATOR_LIST = ["=", "<", ">", "<=", ">=", "<>"]
