#!/usr/bin/env python3

# Faça um programa que peça dois números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo;
# b) a soma do triplo do primeiro com o terceiro;
# c) o terceiro elevado ao cubo.

int_01 = int(input("Por favor, digite um número inteiro: "))
int_02 = int(input("Agora digite outro número inteiro: "))
num_real = float(
    input(
        "Por último, digite um número real usando ponto ( . ) como separador de decimais: "
    )
)

letra_a = (int_01 * 2) * (int_02 / 2)
letra_b = (int_01 * 3) + num_real
letra_c = num_real ** 3

print(f"a) Resposta: {letra_a}", f"b) Resposta: {letra_b}", f"c) Resposta: {letra_c}", sep="\n")
