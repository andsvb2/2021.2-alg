#!/usr/bin/env python3

qtd_num = int(input())
dentro = 0
fora = 0
contador = 0

while contador < qtd_num:
    num_comparado = int(input())
    contador += 1
    if num_comparado in range(10,21):
        dentro += 1
    else:
        fora += 1
print(f"{dentro} in",f"{fora} out",sep="\n")
