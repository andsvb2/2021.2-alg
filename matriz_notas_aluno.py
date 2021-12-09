#!/usr/bin/env python3

# matriz nx3
# quantidade de alunos (n, informado pelo usuário) e cada linha com 3 notas

qtd_alunos = int(input("Quantos alunos? "))

matriz = []

for i in range(qtd_alunos):
    notas = []

    for i in range(3):
        nota = int(input("Digite a nota: "))
        notas.append(nota)
    matriz.append(notas)
print(matriz)

for i in range(len(matriz)):
    media = sum(matriz[i]) / len(matriz[i])
    print(f"{media:.2f}")
