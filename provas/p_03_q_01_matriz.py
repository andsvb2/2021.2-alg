#!/usr/bin/env python3

matriz = []

tam_matriz = int(input("Qual o tamanho da matriz? "))

for i in range(tam_matriz):
    linha = []
    for j in range(tam_matriz):
        linha.append(int(input("Valor a preencher a matriz: ")))
    matriz.append(linha)

num_busca = int(input("Qual o valor a ser encontrado? "))

estado = False

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if num_busca == matriz[linha][coluna]:
            estado = True
            print(f"\nValor encontrado na linha {linha}, coluna {coluna}.")

if estado == False:
    print("\nValor não encontrado.")
