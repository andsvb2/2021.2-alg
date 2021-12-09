#!/usr/bin/env python3

def busca_pares(x):
    if x == 0:
        print(0)
    elif x % 2 == 0:
        print(x)
        # busca_pares(x-1)        #  com x-1 dá erro de recursividade para x >= 995
        busca_pares(x-2)        #  com x-2 dá erro de recursividade para x >= 1989
    else:
        busca_pares(x-1)

# busca_pares(int(input("Digite um número inteiro positivo: ")))

busca_pares(1_988)

#
