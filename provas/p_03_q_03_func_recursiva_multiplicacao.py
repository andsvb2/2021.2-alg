#!/usr/bin/env python3

# uso para gerar uma lista inicial
# import random
# lista_aleatoria = random.sample(range(1,100),5)

lista_teste = [15, 10, 14, 66, 29]

def multiplicacao(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] * multiplicacao(lista[1:])

resultado = multiplicacao(lista_teste)

print(f"A multiplicação dos elementos da lista resulta em {resultado}.")
