#!/usr/bin/env python3

preco_produto = float(input("Qual o preço do produto? "))
qtd_parcelas = 10
valor_parcela = preco_produto / qtd_parcelas
print(f"O valor {preco_produto}, divido em {qtd_parcelas} parcelas, fica por R$ {valor_parcela} cada parcela.")
