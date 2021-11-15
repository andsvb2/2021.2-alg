#!/usr/bin/env python3

# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números
# impares entre eles.
#
# Valores de entrada e resultados
# (6, -5) 5
# (15, 12) 13
# (12, 12) 0

x = int(input())
y = int(input())
numeros = []

if x < y:
    for i in range(x,y):
        if i % 2 != 0:
            numeros.append(i)
else:
    for i in range(y+1,x):
        if i % 2 != 0:
            numeros.append(i)

print(sum(numeros))
