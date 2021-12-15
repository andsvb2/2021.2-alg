#!/usr/bin/env python3

def calcula_conta(prim,seg):
    total = prim + (prim * seg)
    return total

valor_refeicao = float(input("Valor da refeição: "))
taxa_servico = float(input("Valor da taxa de serviço: "))

total_conta = calcula_conta(valor_refeicao,taxa_servico)

print(f"Total a pagar: R$ {total_conta:.2f}")
