#!/usr/bin/env python3

def potencia(prim,seg):
    return prim ** seg

x = int(input("Digite um número inteiro, que será a base da potenciação: "))
y = int(input("Digite outro número inteiro, que será o expoente da potenciação: "))

print(f"O resultado da potenciação é: {potencia(x,y)}.")
