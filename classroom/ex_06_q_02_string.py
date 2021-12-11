#!/usr/bin/env python3

# Créditos
# Ideia de fatiar string: https://stackoverflow.com/questions/19036084/count-occurrences-of-a-given-character-in-a-string-using-recursion
# Augusto Almeida me alertou para o pedido de "letras" e mostrou o método .isalpha().
# Iriedson Vilar me sugeriu simplificar a função com o teste dentro dela.

# Implemente uma função recursiva que receba um string e diga quantas letras ele tem.
# Crie um programa que use essa função.
#
# String usada para teste: 'radar radar    radar     radar 123q123 radar  '
# Resultado esperado: 26 letras e 44 caracteres

def conta_letras(x):
    if not x:
        return 0
    else:
        if not x[0].isalpha():
            return 0 + conta_letras(x[1:])
        else:
            return 1 + conta_letras(x[1:])

def conta_caracteres(x):
    if not x:
        return 0
    else:
        return 1 + conta_caracteres(x[1:])

entrada = input("Qual a string? ")
qtd_letras = conta_letras(entrada)
qtd_total = conta_caracteres(entrada)


print(f"A entrada digitada, '{entrada}', contem {qtd_letras} letra(s) e {qtd_total} caracteres.")
