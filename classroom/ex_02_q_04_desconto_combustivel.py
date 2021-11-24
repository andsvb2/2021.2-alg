#!/usr/bin/env python3

tipo_comb = input("Digite A para álcool e G para gasolina: ").lower()
litros = float(input("Litros: "))

if tipo_comb == 'a':
    pr_litro = 3.8
    if litros <= 20:
        desc = 0.03
    else:
        desc = 0.05
else:                   # else dá certo se contar apenas com entradas 'a' ou 'g'
    pr_litro = 4.4
    if litros <= 20:
        desc = 0.04
    else:
        desc = 0.06

pr_desc = pr_litro - (pr_litro * desc)
total = litros * pr_desc
print(f"O valor a ser pago é de R$ {total:.2f}.")
