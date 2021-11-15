#!/usr/bin/env python3

x = int(input())

contador = 0

while contador < 1000:
    for num in range(x):
        print(f"N[{contador}] = {num}")
        contador += 1
        if contador == 1000:
            break
