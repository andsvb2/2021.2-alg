#!/usr/bin/env python3

codigo = int(input("Digite o código do item: "))

if codigo not in range(100,106): # usado
# if not 100 <= codigo <= 105:    # criado para ajudar a resolver questões de turma
    print("Digite um código válido.")
else:
    quantidade = int(input("Digite a quantidade: "))
    if codigo == 100:
        item = "Cachorro quente"
        preco = 3.10
    elif codigo == 101:
        item = "Bauru simples"
        preco = 5
    elif codigo == 102:
        item = "Bauru c/ ovo"
        preco = 6.3
    elif codigo == 103:
        item = "Hambúrguer"
        preco = 8
    elif codigo == 104:
        item = "Cheeseburguer"
        preco = 8.5
    elif codigo == 105:
        item = "Refrigerante"
        preco = 2.55
    total = quantidade * preco
    if quantidade == 1:
        print(f"{item}: {quantidade} unidade custa R$ {preco:.2f}.")
    else:
        print(f"{item}: {quantidade} unidade(s) por R$ {preco:.2f} cada.\nTOTAL: R$ {total:.2f}.")
