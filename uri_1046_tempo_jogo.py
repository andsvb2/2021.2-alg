#!/usr/bin/env python3

# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do
# jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo
# uma duração mínima de 1 hora e máxima de 24 horas.

entrada = input()
horas = [int(i) for i in entrada.split()]

if horas[0] == horas [1]:
    duracao = 24
else:
    if horas[0] > 12:
        duracao = (24 - horas[0]) + horas[1]
    else:
        duracao = abs(horas[0] - horas[1])

print(f"O JOGO DUROU {duracao} HORA(S)")
