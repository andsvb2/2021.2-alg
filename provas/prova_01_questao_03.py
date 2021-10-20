#!/usr/bin/env python3

emprestimo = float(input("Digite o valor desejado: "))
qtd_parcelas = int(input("Em quantas parcelas deseja pagar? "))
salario = float(input("Qual o valor de seu salário? "))

# em vez de criar variaveis, coloco a operação no if
# valor_parcela = emprestimo / qtd_parcelas
# limite = salario * 0.3

if (emprestimo / qtd_parcelas) <= (salario * 0.3): # com operacao
# if valor_parcela <= limite:                        # usando variaveis
    print("Empréstimo aprovado.")
else:
    print("Empréstimo negado.")
