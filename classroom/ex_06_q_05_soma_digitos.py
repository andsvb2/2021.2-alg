#!/usr/bin/env python3

def soma_digitos(x):
    if len(x) == 1:
        return int(x)
    else:
        if not x[0].isdigit():
            return 0 + soma_digitos(x[1:])
        else:
            return int(x[0]) + soma_digitos(x[1:])

entrada = input("Digite um número: ")

resultado = soma_digitos(entrada)

print(f"A soma dos dígitos contidos em {entrada} é {resultado}.")
