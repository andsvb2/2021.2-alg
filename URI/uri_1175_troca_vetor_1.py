#!/usr/bin/env python3

lista = []
for i in range(20):
    lista.insert(0,int(input()))

for num in range(20):
    print(f"N[{num}] = {lista[num]}")
