
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
