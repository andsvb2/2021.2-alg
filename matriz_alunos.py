#!/usr/bin/env python3

# crie uma matriz 5x2 com curso e aluno nas colunas
# linhas = 5
# colunas = 2 [curso,nomealuno]

lin = 5
col = 2

matriz = []

for i in range(lin):
    linha = []
    curso = input("curso: ")
    aluno = input("nome discente: ")
    linha.append(curso)
    linha.append(aluno)

    matriz.append(linha)
    print(matriz)

print("Terminou:",matriz)
