#!/usr/bin/env python3

teste_soma=teste_tamanho=0
matriz = []
tmp_matriz = []
resultado = float()

operacao = input().lower()

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
        matriz.append(linha)
inf = 5
sup = 7

for i in range(7,12):
    for j in range(inf,sup):
       tmp_matriz.append(matriz[i][j])
    inf -= 1
    sup += 1


# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if i > 7 and i + j >= 12 and j < i:
#             teste_soma+=matriz[i][j]
#             teste_tamanho+=1
#             tmp_matriz.append(matriz[i][j])

if operacao == 's':
    resultado = sum(tmp_matriz)
else:
    resultado = sum(tmp_matriz)/len(tmp_matriz)

print(f"{resultado:.1f}")
