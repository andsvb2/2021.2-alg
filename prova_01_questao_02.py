#!/usr/bin/env python3

letra = input("Por favor, digite uma letra: ").lower()
vogais = ['a', 'á', 'â', 'ã', 'à', 'e', 'é', 'ê', 'i', 'o', 'u', 'á'] # já havia colocado variações de 'a' e 'e' antes de perguntar

if letra in vogais:
    print("A letra digitada é uma vogal.")
else:
    print("A letra digitada é uma consoante.")
