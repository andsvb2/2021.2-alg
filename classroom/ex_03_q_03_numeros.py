#!/usr/bin/env python3

while True:
    num_a = int(input("Digite um número inteiro: "))
    num_b = int(input("Digite outro número inteiro: "))
    if num_a == num_b:
        print("Números iguais.\nTchau.")
        break
    elif num_a < num_b:
        print(f"Os números {num_a} e {num_b} estão na ordem crescente.")
    else:
        print(f"Os números {num_a} e {num_b} estão na ordem decrescente.")
