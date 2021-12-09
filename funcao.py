#!/usr/bin/env python3

# def adicionar(prim,seg):
#     soma = prim + seg
#     return soma

# num1 = 10
# num2 = 18

# resultado = adicionar(num1,num2)

# print(resultado)

def nome_completo(nome):
    if(" " in nome):
        return nome.title()

def nome_lista(nome_aluno):
    nome_aluno = nome_completo(nome_aluno)
    lista = nome_aluno.split(" ")
    return lista

aluno = "hélio moura"
print(nome_lista(aluno))
