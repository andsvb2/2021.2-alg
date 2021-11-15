#!/usr/bin/env python3

# Solução criada por mim
while True:
    y,z = str(),str()
    x = int(input())
    if x == 0:
        break
    else:
        for i in range(1,x+1):
            z = str(i)
            y += z + " "
    print(y.rstrip())

# # Solução criada pelo Augusto
# x = int(input())
# lista = []
# while(x != 0):
#     x = x + 1
#     for a in range(1,x):
#         a = str(a)
#         lista.append(a)
#     numeros = " ".join(lista)
#     print(numeros)
#     lista = []
#     x = int(input())
