# -*- coding: utf-8 -*-
import sys, copy
from ..types import Types
from ..lexer import Token

class Syntactic:

    def __init__(self, tokens):
        self.scope_stack = []
        self.pct_stack = []
        self.variable_count = 0
        self.declaration = False
        self.tokens = tokens
        self.index_atual = -1

    def parse(self):
        return self.programa()

    def programa(self):
        index = self.index_atual
        self.index_atual+=1

        self.do_stack_marker()

        # self.index_atual é 0
        if self.tokens[self.index_atual].str != "program":
            return False

        self.index_atual+=1
        if self.tokens[self.index_atual].type != Types.IDENTIFIER:
            return False

        # add program identifier to the stack
        # print self.tokens[self.index_atual+1]
        self.tokens[self.index_atual].semantic_type = "program"
        self.do_stack_add(self.tokens[self.index_atual])

        self.index_atual+=1
        if self.tokens[self.index_atual].str != ";":
            return False

        self.declaration = True
        if self.declaracoes_variaveis() == False:
            return False

        if self.declaracoes_de_subprogramas() == False:
            return False

        if self.comando_composto() == False:
            return False

        self.index_atual+=1
        if self.tokens[self.index_atual].str != ".":
            return False

        # self.do_stack_clean()

        print
        print "----- Scope Stack -----"
        for t in self.scope_stack:
            print "%s = %s (%s)" % (t.str, t.semantic_type, t.index)

        print
        print "----- PCT Stack -----"
        for t in self.pct_stack:
            print "%s = %s (%s)" % (t.str, t.semantic_type, t.index)

        return True


    def declaracoes_variaveis(self):
        index = self.index_atual
        self.index_atual+=1

        if self.tokens[self.index_atual].str == "var":

            return self.lista_declaracoes_variaveis()

        else:
            self.index_atual = index
            return True

    def lista_declaracoes_variaveis(self):
        index = self.index_atual

        if self.lista_de_identificadores() == True:

            self.index_atual+=1
            if self.tokens[self.index_atual].str == ":":

                if self.tipo() == True:

                    self.index_atual+=1
                    if self.tokens[self.index_atual].str == ";":

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
            if self.tokens[self.index_atual].str == ":":

                if self.tipo() == True:

                    self.index_atual+=1
                    if self.tokens[self.index_atual].str == ";":

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
        self.index_atual+=1

        if self.tokens[self.index_atual].type == Types.IDENTIFIER:

            if self.do_stack_add(self.tokens[self.index_atual]) == False:
                print "Símbolo já definido: " + self.tokens[self.index_atual].str + " Linha: " + str(self.tokens[self.index_atual].line)
                raise Exception("")
            self.variable_count+=1

            return self.lista_de_identificadores_2()

        else:
            return False

    def lista_de_identificadores_2(self):
        index = self.index_atual
        self.index_atual+=1

        if self.tokens[self.index_atual].str == ",":

            self.index_atual+=1
            if self.tokens[self.index_atual].type == Types.IDENTIFIER:

                if self.do_stack_add(self.tokens[self.index_atual]) == False:
                    print "Símbolo já definido: " + self.tokens[self.index_atual].str + " Linha: " + str(self.tokens[self.index_atual].line)
                    raise Exception("")
                self.variable_count+=1

                return self.lista_de_identificadores_2()

            else:
                self.index_atual = index
                return True

        else:
            self.index_atual = index
            return True

    def tipo(self):
        index = self.index_atual
        self.index_atual+=1

        if self.tokens[self.index_atual].str == "integer":
            self.do_stack_types("integer")
            return True

        if self.tokens[self.index_atual].str == "real":
            self.do_stack_types("real")
            return True

        if self.tokens[self.index_atual].str == "boolean":
            self.do_stack_types("boolean")
            return True

        return False

    def declaracoes_de_subprogramas(self):
        self.declaration = False

        index = self.index_atual

        return self.declaracoes_de_subprogramas_2()

    def declaracoes_de_subprogramas_2(self):
        index = self.index_atual

        if self.declaracao_de_subprograma() == True:

            self.index_atual+=1
            if self.tokens[self.index_atual].str == ";":

                return self.declaracoes_de_subprogramas_2()

            else:
                self.index_atual = index
                return True

        else:
            self.index_atual = index
            return True

    def declaracao_de_subprograma(self):
        index = self.index_atual

        self.index_atual+=1
        if self.tokens[self.index_atual].str == "procedure":

            self.index_atual+=1
            if self.tokens[self.index_atual].type == Types.IDENTIFIER:

                # add procedure identifier to the stack
                self.tokens[self.index_atual].semantic_type = "procedure"
                if self.do_stack_add(self.tokens[self.index_atual]) == False:
                    print "Símbolo já definido: " + self.tokens[self.index_atual].str + " Linha: " + str(self.tokens[self.index_atual].line)
                    raise Exception("")

                self.do_stack_marker()

                if self.argumentos() == True:

                    self.index_atual+=1
                    if self.tokens[self.index_atual].str == ";":

                        self.declaration = True
                        if self.declaracoes_variaveis() == True:

                            if self.declaracoes_de_subprogramas() == True:

                                res = self.comando_composto()
                                # self.do_stack_clean()
                                return res

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
        self.index_atual+=1

        if self.tokens[self.index_atual].str == "(":

            if self.lista_de_parametros() == True:

                self.index_atual+=1
                if self.tokens[self.index_atual].str == ")":

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
            if self.tokens[self.index_atual].str == ":":

                if self.tipo() == True:

                    return self.lista_de_parametros_2()

                else:
                    return False

            else:
                return False

        else:
            return False

    def lista_de_parametros_2(self):
        index = self.index_atual
        self.index_atual+=1

        if self.tokens[self.index_atual].str == ";":

            if self.lista_de_identificadores() == True:

                self.index_atual+=1
                if self.tokens[self.index_atual].str == ":":

                    if self.tipo() == True:

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
        self.index_atual+=1

        if self.tokens[self.index_atual].str == "begin":

            if self.comandos_opcionais() == True:

                self.index_atual+=1
                if self.tokens[self.index_atual].str == "end":

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

            return self.lista_de_comandos_2()

        else:
            return False

    def lista_de_comandos_2(self):
        index = self.index_atual
        self.index_atual+=1

        if self.tokens[self.index_atual].str == ";":

            if self.comando() == True:

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
            if self.tokens[self.index_atual].str == Types.CMD_ATTR_STR:

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

        self.index_atual+=1
        if self.tokens[self.index_atual].str == "if":

            if self.expressao() == True:

                self.index_atual+=1
                if self.tokens[self.index_atual].str == "then":

                    if self.comando() == True:

                        index = self.index_atual
                        if self.parte_else() == True:
                            return True
                        else:
                            self.index_atual = index
                            return True

        # backtrack e testa o quinto caso
        self.index_atual = index

        self.index_atual+=1
        if self.tokens[self.index_atual].str == "while":

            if self.expressao() == True:

                self.index_atual+=1
                if self.tokens[self.index_atual].str == "do":

                    if self.comando() == True:
                        return True

        return False

    def parte_else(self):
        index = self.index_atual

        self.index_atual+=1
        if self.tokens[self.index_atual].str == "else":

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

        self.index_atual+=1

        token = self.tokens[self.index_atual]

        if token.type == Types.IDENTIFIER:
            if self.check_isdeclared(token) == False:
                print "Símbolo não declarado: " + token.str + " Linha: " + str(token.line)
                raise Exception("Símbolo não declarado: " + token.str + " Linha: " + str(token.line))

            t = self.get_stack_token(token.str)
            t = copy.copy(t)
            t.index = token.index
            self.do_pct_add(t)

            return True

        return False

    def ativacao_de_procedimento(self):
        index = self.index_atual

        self.index_atual+=1
        if self.tokens[self.index_atual].type == Types.IDENTIFIER:

            token = self.tokens[self.index_atual]
            if self.check_isdeclared(token) == False:
                print "Símbolo não declarado: " + token.str + " Linha: " + str(token.line)
                raise Exception("Símbolo não declarado: " + token.str + " Linha: " + str(token.line))

            self.index_atual+=1
            if self.tokens[self.index_atual].str == "(":

                if self.lista_de_expressoes() == True:

                    self.index_atual+=1
                    if self.tokens[self.index_atual].str == ")":
                        return True

                    else:
                        return False

                else:
                    return False

            else:
                self.index_atual-=1
                return True

        else:
            return False

    def lista_de_expressoes(self):
        index = self.index_atual

        if self.expressao() == True:

            return self.lista_de_expressoes_2()

        else:
            return False

    def lista_de_expressoes_2(self):
        index = self.index_atual

        self.index_atual+=1
        if self.tokens[self.index_atual].str == ",":

            if self.expressao() == True:

                if self.lista_de_expressoes_2() == True:
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

    def expressao(self):
        index = self.index_atual

        if self.expressao_simples() == True:

            if self.op_relacional() == True:

                if self.expressao_simples() == True:
                    return True

        # backtrack e testa caso de ser só expressao_simples
        self.index_atual = index
        return self.expressao_simples()


    def expressao_simples(self):
        index = self.index_atual

        if self.sinal() == True:

            if self.termo() == True:

                return self.expressao_simples_2()

            else:
                return False

        else:

            self.index_atual = index
            if self.termo() == True:

                return self.expressao_simples_2()

            else:
                return False

    def expressao_simples_2(self):
        index = self.index_atual

        if self.op_aditivo() == True:

            if self.termo() == True:

                if self.expressao_simples_2() == True:
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

    def termo(self):
        index = self.index_atual

        if self.fator() == True:

            return self.termo_2()

        else:
            return False

    def termo_2(self):
        index = self.index_atual

        if self.op_multiplicativo() == True:

            if self.fator() == True:

                if self.termo_2() == True:
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

    def fator(self):
        index = self.index_atual
        self.index_atual+=1

        if self.tokens[self.index_atual].type == Types.IDENTIFIER:

            token = self.tokens[self.index_atual]
            if self.check_isdeclared(token) == False:
                print "Símbolo não declarado: " + token.str + " Linha: " + str(token.line)
                raise Exception("Símbolo não declarado: " + token.str + " Linha: " + str(token.line))

            t = self.get_stack_token(token.str)
            t = copy.copy(t)
            t.index = token.index
            self.do_pct_add(t)

            self.index_atual+=1
            if self.tokens[self.index_atual].str == "(":

                if self.lista_de_expressoes() == True:

                    self.index_atual+=1
                    if self.tokens[self.index_atual].str == ")":
                        return True

                    else:
                        return False

                else:
                    return False

            else:
                self.index_atual-=1
                return True

        else:
            if self.tokens[self.index_atual].type == Types.NUMBER_INT:
                self.tokens[self.index_atual].semantic_type = "integer"
                self.do_pct_add(self.tokens[self.index_atual])
                return True

            elif self.tokens[self.index_atual].type == Types.NUMBER_REAL:
                self.tokens[self.index_atual].semantic_type = "real"
                self.do_pct_add(self.tokens[self.index_atual])
                return True

            elif self.tokens[self.index_atual].str == "true":
                self.tokens[self.index_atual].semantic_type = "boolean"
                self.do_pct_add(self.tokens[self.index_atual])
                return True

            elif self.tokens[self.index_atual].str == "false":
                self.tokens[self.index_atual].semantic_type = "boolean"
                self.do_pct_add(self.tokens[self.index_atual])
                return True

            else:
                if self.tokens[self.index_atual].str == "(":

                    if self.expressao() == True:

                        self.index_atual+=1
                        if self.tokens[self.index_atual].str == ")":
                            return True

                        else:
                            return False

                    else:
                        return False

                else:
                    if self.tokens[self.index_atual].type == Types.KEYWORD and \
                        self.tokens[self.index_atual].str == "not":

                        if self.fator() == True:
                            return True

                        else:
                            return False

                    else:
                        return False

    def sinal(self):
        index = self.index_atual

        self.index_atual+=1
        if self.tokens[self.index_atual].str == "+" or \
            self.tokens[self.index_atual].str == "-":

            return True

        else:
            return False

    def op_relacional(self):
        index = self.index_atual

        self.index_atual+=1
        if self.tokens[self.index_atual].str == "=" or \
            self.tokens[self.index_atual].str == "<" or \
            self.tokens[self.index_atual].str == ">" or \
            self.tokens[self.index_atual].str == "<=" or \
            self.tokens[self.index_atual].str == ">=" or \
            self.tokens[self.index_atual].str == "<>":

            return True

        else:
            return False

    def op_aditivo(self):
        index = self.index_atual

        self.index_atual+=1
        if self.tokens[self.index_atual].str == "+" or \
            self.tokens[self.index_atual].str == "-" or \
            self.tokens[self.index_atual].str == "or":

            return True

        else:
            return False

    def op_multiplicativo(self):
        index = self.index_atual

        self.index_atual+=1
        if self.tokens[self.index_atual].str == "*" or \
            self.tokens[self.index_atual].str == "/" or \
            self.tokens[self.index_atual].str == "and":

            return True

        else:
            return False

    def get_stack_token(self, symbol):
        for t in self.scope_stack[::-1]:
            if t.str == symbol:
                return t
        return False

    def check_isdeclared(self, token):
        for t in self.scope_stack[::-1]:
            if t.str == token.str:
                return True
        return False

    def do_stack_add(self, token):
        for t in self.scope_stack[::-1]:
            if t.str == "$":
                break
            if t.str == token.str:
                return False

        self.scope_stack.append(token)
        return True

    def do_stack_types(self, stype):
        for i in range(self.variable_count):
            self.scope_stack[-(i+1)].semantic_type = stype

        self.variable_count = 0

    def do_stack_marker(self):
        self.scope_stack.append(Token(tok="$", ttype=Types.MARKER, stype=Types.MARKER))

    def do_stack_clean(self):
        t = self.scope_stack.pop()

        while t.str != "$":
            t = self.scope_stack.pop()

    def do_backtrack_pct(self, index):
        i = 0
        while i < len(self.pct_stack):
            if self.pct_stack[i].index >= index:
                del self.pct_stack[i]
            else:
                i+=1

    def do_pct_add(self, token):
        self.do_backtrack_pct(token.index)

        self.pct_stack.append(token)
