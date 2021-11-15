#!/usr/bin/env python3

x = None

while True:
    soma = []
    y = 0
    x = int(input())
    if x == 0:
        break
    elif x % 2 == 0:
        soma.append(x)
    else:
        soma.append(x+1)

    for i in range(1,5):
        y = soma[i-1]+2
        soma.append(y)
    print(sum(soma))
