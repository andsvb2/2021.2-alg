#!/usr/bin/env python3


pares = []
impares = []

# # bloco para gerar números aleatórios de teste
# import random
# lista_02 = random.sample(range(-100,100),20)
# for i in lista_02:
#     if i % 2 == 0:
#         pares.append(i)
#         print(pares,impares,sep="\n")
#     else:
#         impares.append(i)
#         print(pares,impares,sep="\n")

for i in range(20):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print()

while True:
    if len(pares) != 0:
        tmp_pares = pares.pop()
        print(f"Número par removido: {tmp_pares}.")
    if len(impares) != 0:
        tmp_impares = impares.pop()
        print(f"Número ímpar removido: {tmp_impares}.")
    if len(pares) == len(impares) == 0:
        print(f"\nPilhas esvaziadas.")
        break
