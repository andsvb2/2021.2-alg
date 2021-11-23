#!/usr/bin/env python3

import random # módulo para gerar números pseudoaleatórios
# Exemplo retirado do link: https://www.tutorialspoint.com/generating-random-number-list-in-python
# Documentação: https://docs.python.org/pt-br/3.9/library/random.html

# Gera duas listas com 10 números aleatórios entre -100 e 100
lista_01 = random.sample(range(-100,100),10)
lista_02 = random.sample(range(-100,100),10)

# Valores manualmente inseridos
# lista_01 = [-90, -71, -55, -28, 5, 24, 33, 66, 68, 72]
# lista_02 = [72, 63, 2, -13, -27, -42, -49, -53, -71, -100]

# lista_03 = lista_01.copy() # cria a lista_03 sem que alterações atinjam a lista_01

print(f"Lista 01: {lista_01}",f"Lista 02: {lista_02}", sep="\n")

# solução mais complicada, com mensagens específicas a cada caso
# if lista_01 == sorted(lista_01):
    # if lista_02 == sorted(lista_02):
        # print("As listas estão ordenadas.")
    # else:
        # print("A Lista 01 está ordenada.")
# elif lista_02 == sorted(lista_02):
    # print("A Lista 02 está ordenada.")
# else:
    # print("As listas estão desordenadas.")

# solução mais simples, que verifica e retorna informação de cada lista
if lista_01 == sorted(lista_01):
    print("A Lista 01 está em ordem crescente.")
elif lista_01 == sorted(lista_01,reverse=True):
    print("A Lista 01 está em ordem decrescente.")
else:
    print("A Lista 01 está desordenada.")

if lista_02 == sorted(lista_02):
    print("A Lista 02 está em ordem crescente.")
elif lista_02 == sorted(lista_02,reverse=True):
    print("A Lista 02 está em ordem decrescente.")
else:
    print("A Lista 02 está desordenada.")

for i in lista_02:
    if i not in lista_01:
        lista_01.append(i)

print("O resultado da combinação das duas listas é:",sorted(lista_01),sep="\n")
