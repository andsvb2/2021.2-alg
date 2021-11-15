#!/usr/bin/env python3

qtd_alunos,num_sorteado = [int(i) for i in input().split()]
alunos = []

for i in range(qtd_alunos):
    alunos.append(input())

alunos.sort(key=str.lower)
print(alunos[num_sorteado-1])
