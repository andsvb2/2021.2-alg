#!/usr/bin/env python3

# Faça um programa em Python que leia dois números inteiros (A e B), realize os
# seguintes cálculos e exiba o resultado de cada cálculo.
#
# a) A parte inteira da divisão entre os valores de A e B
# b) O resto da divisão entre os valores de A e B
# c) O correspondente a 35 % do valor de B

num_a = int(input("Digite um número inteiro: "))
num_b = int(input("Digite outro número inteiro: "))

# a) A parte inteira da divisão entre os valores de A e B
div_int = num_a // num_b
print(f"a) O resultado da divisão inteira de {num_a} por {num_b} é {div_int}.")

# b) O resto da divisão entre os valores de A e B
resto_div = num_a % num_b
print(f"b) O resto da divisão de {num_a} por {num_b} é {div_int}.")

# c) O correspondente a 35 % do valor de B
porcentagem = 0.35 * num_b
print(f"c) {porcentagem:.2f} é equivalente a 35% de {num_b}.")


# Resposta fornecida no slide
#
# A = int(input("Digite o número:"))
# B = int(input("Digite o número:"))
#
# #a)
# parteInteira = A // B
# print("Resultado Parte Inteira: %d" %parteInteira)
#
# #b)
# resto = A % B
# print("Resultado Resto: %d" %resto)
#
# #xc)
# porcentagem = B * 0.35
# print("Resultado Porcentagem : %.2f" %porcentagem)
