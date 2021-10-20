#!/usr/bin/env python3

# Valores teste: (JOAO, 500.00, 1230.30) (PEDRO, 700.00, 0.00) (MANGOJATA, 1700.00, 1230.50)

nome_vendedor = input()
salario_fixo = float(input())
total_vendas = float(input())
comissao_devida = 0.15 * total_vendas
total_receber = comissao_devida + salario_fixo

print(f"TOTAL = R$ {total_receber:.2f}")
