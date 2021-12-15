#!/usr/bin/env python3

matriz = []
soma = contador = 0
operacao = input().lower()

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

col = 1
for i in range(1,11):
    for j in range(0,col):
        soma += matriz[i][j]
        contador += 1
    if i < 5:
        col += 1
    if i > 5:
        col -= 1

if operacao == 's':
    print(f"{soma:.1f}")
else:
    print(f"{soma/contador:.1f}")
