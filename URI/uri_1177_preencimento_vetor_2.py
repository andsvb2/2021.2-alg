#!/usr/bin/env python3

# Solução que criei
x = int(input())
contador = 0
while contador < 1000:
    for num in range(x):
        print(f"N[{contador}] = {num}")
        contador += 1
        if contador == 1000:
            break


# # Solução do Augusto Almeida
# lista = []
# n = int(input())
# for a in range(1000):
#     for b in range(n):
#         lista.append(b)
#     print(f"N[{a}] = {lista[a]}")
