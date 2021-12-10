#!/usr/bin/env python3

def potencia(prim,seg):
    return prim ** seg

x = int(input("Qual número inteiro será a base da potenciação? "))
y = int(input("Qual número inteiro será o expoente da potenciação? "))

print(f"O resultado da potenciação é {potencia(x,y)}.")
