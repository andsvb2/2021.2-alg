#!/usr/bin/env python3

# resultado = 0
# for i in range(1,6):
#     resultado += i
# print(f"Resultado da soma dos inteiros até 5: {resultado:d}")

maior = 0

for i in range(4):
    num = int(input("Digite um número inteiro positivo: "))
    if num > maior:
        maior = num

print('o maior número informado foi: ', maior)
