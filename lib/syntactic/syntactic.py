# -*- coding: utf-8 -*-
from ..types import Types

class Syntactic:

    def __init__(self, tokens):
        self.tokens = tokens
        self.index_atual = 0

    def parse(self):
        return self.programa()

    def programa(self):
        index = self.index_atual

        # self.index_atual é 0
        if self.tokens[self.index_atual].type != Types.KEYWORD or
            self.tokens[self.index_atual].str != "program":
            return False

        self.index_atual+=1
        if self.tokens[self.index_atual].type != Types.IDENTIFIER:
            return False

        self.index_atual+=1
        if self.tokens[self.index_atual].type != Types.DELIMTER or
            self.tokens[self.index_atual].str != ";":
            return False

        self.index_atual+=1
        if self.declaracoes_variaveis() == False:
            return False

        self.index_atual+=1
        if self.declaracoes_de_subprogramas() == False:
            return False

        self.index_atual+=1
        if self.comando_composto() == False:
            return False

        self.index_atual+=1
        if self.tokens[self.index_atual].type != Types.DELIMTER or
            self.tokens[self.index_atual].str != ".":
            return False

        return True


    def declaracoes_variaveis(self):
        index = self.index_atual

        if self.tokens[self.index_atual].type == Types.KEYWORD and
            self.tokens[self.index_atual].str == "var":

            self.index_atual+=1
            return self.lista_declaracoes_variaveis()

        else:
            self.index_atual = index
            return True

    def lista_declaracoes_variaveis(self):
        index = self.index_atual

        if self.lista_de_identificadores() == True:

            self.index_atual+=1
            if self.tokens[self.index_atual].type == Types.DELIMTER and
                self.tokens[self.index_atual].str == ":":

                self.index_atual+=1
                if self.tipo() == True:

                    self.index_atual+=1
                    if self.tokens[self.index_atual].type == Types.DELIMTER and
                        self.tokens[self.index_atual].str == ";":

                        self.index_atual+=1
                        return self.lista_declaracoes_variaveis_2()

                    else:
                        return False

                else:
                    return False

            else:
                return False

        else:
            return False


    def lista_declaracoes_variaveis_2(self):
        index = self.index_atual

        if self.lista_de_identificadores() == True:

            self.index_atual+=1
            if self.tokens[self.index_atual].type == Types.DELIMTER and
                self.tokens[self.index_atual].str == ":":

                self.index_atual+=1
                if self.tipo() == True:

                    self.index_atual+=1
                    if self.tokens[self.index_atual].type == Types.DELIMTER and
                        self.tokens[self.index_atual].str == ";":

                        self.index_atual+=1
                        return self.lista_declaracoes_variaveis_2()

                    else:
                        self.index_atual = index
                        return True

                else:
                    self.index_atual = index
                    return True

            else:
                self.index_atual = index
                return True

        else:
            self.index_atual = index
            return True

    def lista_de_identificadores(self):
        index = self.index_atual

        if self.tokens[self.index_atual].type == Types.IDENTIFIER:

            self.index_atual+=1
            return self.lista_de_identificadores_2()

        else:
            return False

    def lista_de_identificadores_2(self):
        index = self.index_atual

        if self.tokens[self.index_atual].type == Types.DELIMTER and
            self.tokens[self.index_atual].str == ",":

            self.index_atual+=1
            if self.tokens[self.index_atual].type == Types.IDENTIFIER:

                self.index_atual+=1
                return self.lista_de_identificadores_2()

            else:
                self.index_atual = index
                return True

        else:
            self.index_atual = index
            return True

    def tipo(self):
        index = self.index_atual

        if self.tokens[self.index_atual].type == Types.KEYWORD and
            self.tokens[self.index_atual].str == "integer":
            return True

        if self.tokens[self.index_atual].type == Types.KEYWORD and
            self.tokens[self.index_atual].str == "real":
            return True

        if self.tokens[self.index_atual].type == Types.KEYWORD and
            self.tokens[self.index_atual].str == "boolean":
            return True

        return False

    def declaracoes_de_subprogramas(self):
        index = self.index_atual

        return self.declaracoes_de_subprogramas_2()

    def declaracoes_de_subprogramas_2(self):
        index = self.index_atual

        if self.declaracao_de_subprograma() == True:

            self.index_atual+=1
            if self.tokens[self.index_atual].type == Type.DELIMTER and
                self.tokens[self.index_atual].str == ";":

                self.index_atual+=1
                return self.declaracoes_de_subprogramas_2()

            else:
                self.index_atual = index
                return True

        else:
            self.index_atual = index
            return True

    def declaracao_de_subprograma(self):
        index = self.index_atual

        if self.tokens[self.index_atual].type == Types.KEYWORD and
            self.tokens[self.index_atual].str == "procedure":

            self.index_atual+=1
            if self.tokens[self.index_atual].type == Types.IDENTIFIER:

                self.index_atual+=1
                if self.argumentos() == True:

                    self.index_atual+=1
                    if self.tokens[self.index_atual].type == Types.DELIMTER and
                        self.tokens[self.index_atual].str == ";":

                        self.index_atual+=1
                        if self.declaracoes_variaveis() == True:

                            self.index_atual+=1
                            if self.declaracoes_de_subprogramas() == True:

                                self.index_atual+=1
                                return self.comando_composto()

                            else:
                                return False

                        else:
                            return False

                    else:
                        return False

                else:
                    return False

            else:
                return False

        else:
            return False


    def argumentos(self):
        index = self.index_atual

        if self.tokens[self.index_atual].type == Type.DELIMTER and
            self.tokens[self.index_atual].str == "(":

            self.index_atual+=1
            if self.lista_de_parametros() == True:

                self.index_atual+=1
                if self.tokens[self.index_atual].type == Type.DELIMTER and
                    self.tokens[self.index_atual].str == ")":

                    return True

                else:
                    self.index_atual = index
                    return True

            else:
                self.index_atual = index
                return True

        else:
            self.index_atual = index
            return True

    def lista_de_parametros(self):
        index = self.index_atual

        if self.lista_de_identificadores() == True:

            self.index_atual+=1
            if self.tokens[self.index_atual].type == Types.DELIMTER and
                self.tokens[self.index_atual].str == ":":

                self.index_atual+=1
                if self.tipo() == True:

                    self.index_atual+=1
                    return self.lista_de_parametros_2()

                else:
                    return False

            else:
                return False

        else:
            return False

    def lista_de_parametros_2(self):
        index = self.index_atual

        if self.tokens[self.index_atual].type == Types.DELIMTER and
            self.tokens[self.index_atual].str == ";"

            self.index_atual+=1
            if self.lista_de_identificadores() == True:

                self.index_atual+=1
                if self.tokens[self.index_atual].type == Types.DELIMTER and
                    self.tokens[self.index_atual].str == ":":

                    self.index_atual+=1
                    if self.tipo() == True:

                        self.index_atual+=1
                        if self.lista_de_parametros_2() == False:
                            self.index_atual = index
                            return True

                    else:
                        self.index_atual = index
                        return True

                else:
                    self.index_atual = index
                    return True

            else:
                self.index_atual = index
                return True

        else:
            self.index_atual = index
            return True

    def comando_composto(self):
        index = self.index_atual

        if self.tokens[self.index_atual].type == Types.KEYWORD and
            self.tokens[self.index_atual].str == "begin":

            self.index_atual+=1
            if self.comandos_opcionais() == True:

                self.index_atual+=1
                if self.tokens[self.index_atual].type == Types.KEYWORD and
                    self.tokens[self.index_atual].str == "end":

                    return True

                else:
                    return False

            else:
                return False

        else:
            return False


    def comandos_opcionais(self):
        index = self.index_atual

        if self.lista_de_comandos() == True:

            return True

        else:
            self.index_atual = index
            return True

    def lista_de_comandos(self):
        index = self.index_atual

        if self.comando() == True:

            self.index_atual+=1
            return self.lista_de_comandos_2()

        else:
            return False

    def lista_de_comandos_2(self):
        index = self.index_atual

        if self.tokens[self.index_atual].type == Type.DELIMTER and
            self.tokens[self.index_atual].str == ";":

            self.index_atual+=1
            if self.comando() == True:

                self.index_atual+=1
                if self.lista_de_comandos_2() == True:

                    return True

                else:
                    self.index_atual = index
                    return True

            else:
                self.index_atual = index
                return True

        else:
            self.index_atual = index
            return True

    def comando(self):
        index = self.index_atual

        # primeiro caso
        if self.variavel() == True:

            self.index_atual+=1
            if self.tokens[self.index_atual].type == Types.CMD_ATTR and
                self.tokens[self.index_atual].str == Types.CMD_ATTR_STR:

                self.index_atual+=1
                if self.expressao() == True:

                    return True

        # backtrack e testa o segundo caso
        self.index_atual = index

        if self.ativacao_de_procedimento() == True:
            return True

        # backtrack e testa o terceiro caso
        self.index_atual = index

        if self.comando_composto() == True:
            return True

        # backtrack e testa o quarto caso
        self.index_atual = index

        if self.tokens[self.index_atual].type == Types.KEYWORD and
            self.tokens[self.index_atual].str == "if":

            self.index_atual+=1
            if self.expressao() == True:

                self.index_atual+=1
                if self.tokens[self.index_atual].type == Types.KEYWORD and
                    self.tokens[self.index_atual].str == "then":

                    self.index_atual+=1
                    if self.comando() == True:

                        self.index_atual+=1
                        if self.parte_else() == True:
                            return True

        # backtrack e testa o quinto caso
        self.index_atual = index

        if self.tokens[self.index_atual].type == Types.KEYWORD and
            self.tokens[self.index_atual].str == "while":

            self.index_atual+=1
            if self.expressao() == True:

                self.index_atual+=1
                if self.tokens[self.index_atual].type == Types.KEYWORD and
                    self.tokens[self.index_atual].str == "do":

                    self.index_atual+=1
                    if self.comando() == True:
                        return True

        return False

    def parte_else(self):
        index = self.index_atual

        if self.tokens[self.index_atual].type == Types.KEYWORD and
            self.tokens[self.index_atual].str == "else":

            self.index_atual+=1
            if self.comando() == True:

                return True

            else:
                self.index_atual = index
                return True

        else:
            self.index_atual = index
            return True

    def variavel(self):
        index = self.index_atual

        return self.tokens[self.index_atual].type == Types.IDENTIFIER

    def ativacao_de_procedimento(self):
        index = self.index_atual

        if self.tokens[self.index_atual].type == Types.IDENTIFIER

            self.index_atual+=1
            # Testar se é delimitador
            if self.tokens[self.index_atual].str == "(":

                self.index_atual+=1
                if self.lista_de_expressoes() == True:

                    self.index_atual+=1
                    # Testar se é delimitador
                    if self.tokens[self.index_atual].str == ")":
                        return True

                    else:
                        return False

                else:
                    return False

            else:
                return True

        else:
            return False

    def lista_de_expressoes(self):
        index = self.index_atual

        if self.expressao() == True:

            self.index_atual+=1 ## Checar incremento
            return self.lista_de_expressoes_2()

        else:
            return False

    def lista_de_expressoes_2(self):
        index = self.index_atual

        # Testar se é delimitador
        if self.tokens[self.index_atual].str == ","

            self.index_atual+=1 ## Checar incremento
            if self.expressao() == True:

                self.index_atual+=1 ## Checar incremento
                if self.lista_de_expressoes_2() == True:
                    return True

                else:
                    self.index_atual = index
                    return True

            else:
                self.index_atual = index
                return True ## Verificar com Gustavo, se temos uma ",", expressao é obrigatório

        else:
            self.index_atual = index
            return True

    def expressao(self):
        index = self.index_atual

        if self.expressao_simples() == True:

            self.index_atual+=1 ## Checar incremento
            if self.op_relacional() == True:

                self.index_atual+=1 ## Checar incremento
                return self.expressao_simples()

            else:
                return True

        else:
            return False

    def expressao_simples(self):
        index = self.index_atual

        if self.sinal() == True:

            self.index_atual+=1
            if self.termo() == True:

                self.index_atual+=1
                return self.expressao_simples_2()

            else:
                return False

        else:

            if self.termo() == True:

                self.index_atual+=1
                return self.expressao_simples_2()

            else:
                return False

    def expressao_simples_2(self):
        index = self.index_atual

        if self.op_aditivo() == True:

            self.index_atual+=1 ## Checar incremento
            if self.termo() == True:

                self.index_atual+=1 ## Checar incremento
                if self.expressao_simples_2() == True:
                    return True

                else:
                    self.index_atual = index
                    return True

            else:
                self.index_atual = index
                return True ## Verificar com Gustavo, se temos um op_aditivo, termo é obrigatório

        else:
            self.index_atual = index
            return True

    def termo(self):
        index = self.index_atual

        if self.fator() == True:

            self.index_atual+=1
            return self.termo_2()

        else:
            return False

    def termo_2(self):
        index = self.index_atual

        if self.op_multiplicativo() == True:

            self.index_atual+=1 ## Checar incremento
            if self.fator() == True:

                self.index_atual+=1 ## Checar incremento
                if self.termo_2() == True:
                    return True

                else:
                    self.index_atual = index
                    return True

            else:
                self.index_atual = index
                return True ## Verificar com Gustavo, se temos um op_mult, fator é obrigatório

        else:
            self.index_atual = index
            return True

    def fator(self):
        index = self.index_atual

        if self.tokens[self.index_atual].type == Types.IDENTIFIER

            self.index_atual+=1
            # Testar se é delimitador
            if self.tokens[self.index_atual].str == "(":

                self.index_atual+=1
                if self.lista_de_expressoes() == True:

                    self.index_atual+=1
                    # Testar se é delimitador
                    if self.tokens[self.index_atual].str == ")":
                        return True

                    else:
                        return False

                else:
                    return False

            else:
                return True

        else:
            if self.tokens[self.index_atual].type == Types.NUMBER_INT or

                self.tokens[self.index_atual].type == Types.NUMBER_REAL or

                self.tokens[self.index_atual].str == "true" or

                self.tokens[self.index_atual].str == "false":

                    return True

            else:
                # Testar se é delimitador
                if self.tokens[self.index_atual].str == "(":

                    self.index_atual+=1
                    if self.expressao() == True:

                        self.index_atual+=1
                        # Testar se é delimitador
                        if self.tokens[self.index_atual].str == ")":
                            return True

                        else:
                            return False

                    else:
                        return False

                else:
                    if self.tokens[self.index_atual].type == Types.KEYWORD and
                        self.tokens[self.index_atual].str == "not":

                        self.index_atual+=1
                        if self.fator() == True:
                            return True

                        else:
                            return False

                    else:
                        return False

    def sinal(self):
        index = self.index_atual

        if self.tokens[self.index_atual].str == "+" or

            self.tokens[self.index_atual].str == "-":

            return True

        else:
            return False

    def op_relacional(self):
        index = self.index_atual

        if self.tokens[self.index_atual].str == "=" or

            self.tokens[self.index_atual].str == "<" or

            self.tokens[self.index_atual].str == ">" or

            self.tokens[self.index_atual].str == "<=" or

            self.tokens[self.index_atual].str == ">=" or

            self.tokens[self.index_atual].str == "<>":

            return True

        else:
            return False

    def op_aditivo(self):
        index = self.index_atual

        if self.tokens[self.index_atual].str == "+" or

            self.tokens[self.index_atual].str == "-" or

            self.tokens[self.index_atual].str == "or":

            return True

        else:
            return False

    def op_multiplicativo(self):
        index = self.index_atual

        if self.tokens[self.index_atual].str == "*" or

            self.tokens[self.index_atual].str == "/" or

            self.tokens[self.index_atual].str == "and":

            return True

        else:
            return False
