#!/usr/bin/env python3

# Valores teste: (10, 85) (2, 92) (22, 67)

rendimento_automovel = 12       # este valor e uma constante
tempo_gasto = int(input())
velocidade_media = int(input())
distancia_percorrida = tempo_gasto * velocidade_media
combustivel_necessario = distancia_percorrida / rendimento_automovel

# print("%.3f" % (combustivel_necessario)) # String.format()
print(f"{combustivel_necessario:.3f}")   # f-strings
