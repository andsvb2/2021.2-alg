#!/usr/bin/env python3

# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os
# valores em ordem crescente, uma linha em branco e em seguida, os valores na
# sequência como foram lidos.
#
entrada = input()
numeros = [int(i) for i in entrada.split()]

for i in sorted(numeros):
    print(i,sep="\n")

print()

for i in numeros:
    print(i,sep="\n")
