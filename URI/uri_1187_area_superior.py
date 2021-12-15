#!/usr/bin/env python3

matriz = []
soma = contador = 0
operacao = input().lower()

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

inf = 1
sup = 11
for i in range(0,5):
    for j in range(inf,sup):
        soma += matriz[i][j]
        contador += 1
    inf += 1
    sup -= 1

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if (i == 0 and j in range(1,11)) or (i == 1 and j in range(2,10)) or (i == 2 and j in range(3,9)) or (i == 3 and j in range(4,8)) or (i == 4 and j in range(5,7)):
#             soma += matriz[i][j]
#             contador += 1

if operacao == 's':
    print(f"{soma:.1f}")
else:
    print(f"{soma/contador:.1f}")
