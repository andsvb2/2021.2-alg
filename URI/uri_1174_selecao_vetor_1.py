#!/usr/bin/env python3

lista = []
for i in range(100):
    lista.append(float(input()))


for i in range(len(lista)):
    x = lista[i]
    if x <= 10:
        print(f"A[{i}] = {lista[i]}")
