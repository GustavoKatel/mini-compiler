
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

                        return self.lista_declaracoes_variaveis_2()

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

                        return self.lista_declaracoes_variaveis_2()

        else:
            self.index_atual = index
            return True
