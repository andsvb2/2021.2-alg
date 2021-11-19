#!/usr/bin/env python3

import random # módulo para gerar números pseudoaleatórios
# Exemplo retirado do link: https://www.tutorialspoint.com/generating-random-number-list-in-python
# Documentação: https://docs.python.org/pt-br/3.9/library/random.html

# Gera duas listas com 10 números aleatórios entre -100 e 100
# lista_01 = random.sample(range(-100,100),10)
# lista_02 = random.sample(range(-100,100),10)

# Valores manualmente inseridos
lista_01 = [-71, -55, -28, 66, 72, 33, -90, 68, 5, 24]
lista_02 = [-100, -71, 72, -53, -49, -42, -27, -13, 2, 63]
lista_03 = lista_01.copy() # cria a lista_03 sem que alterações atinjam a lista_01

print(f"Lista 01: {lista_01}",f"Lista 02: {lista_02}", sep="\n")

if lista_01 == sorted(lista_01):
    if lista_02 == sorted(lista_02):
        print("As listas estão ordenadas.")
    else:
        print("A Lista 01 está ordenada.")
elif lista_02 == sorted(lista_02):
    print("A Lista 02 está ordenada.")
else:
    print("As listas estão desordenadas.")

for i in lista_02:
    if i not in lista_03:
        lista_03.append(i)

print(sorted(lista_01),sorted(lista_02),sorted(lista_03),sep="\n")
