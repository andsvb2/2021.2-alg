#!/usr/bin/env python3

# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do
# jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo
# uma duração mínima de 1 hora e máxima de 24 horas.

# inicio,final = [int(i) for i in input().split()]

# if inicio < final:
#     duracao = final - inicio
# else:
#     duracao = (24 - inicio) + final
# print(f"O JOGO DUROU {duracao} HORA(S)")

# Criado para ajudar a pensar outro código.
#
inc,fim = (input(" ").split())
inc = int(inc)
fim = int(fim)
if inc < fim:
    duracao = fim - inc
else:
    duracao = (24 - inc) + fim
print(f"O JOGO DUROU {duracao} HORA(S)")

# if inc < fim:
#     inc,fim = fim - inc
#     print('%d'% inc,fim)
# else:
#     inc,fim = (24-inc)+fim
#     print('%d'% inc, fim)
# print("O JOGO DUROU %d HORA(S)"%duracao)
