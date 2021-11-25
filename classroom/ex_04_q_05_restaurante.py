#!/usr/bin/env python3

# cria lista com os 15 nomes mais comuns no Brasil
# fonte: https://pt.wikipedia.org/wiki/Lista_de_prenomes_mais_comuns_no_Brasil
# clientes = ['José', 'Maria', 'João', 'Ana', 'Antônio', 'Francisca', 'Francisco', 'Antônia', 'Carlos', 'Adriana', 'Paulo', 'Juliana', 'Pedro', 'Márcia', 'Lucas']

# esse bloco cria uma lista de 15 clientes a partir da entrada do usuário
clientes =[]
for i in range(15):
    clientes.append(input("Digite o nome do cliente a ser atendido: "))

pedidos,pagamento,entrega = [],[],[]

def entrar_cliente():
    pedidos.append(clientes.pop(0))
    verificar_filas()

def mover_pagamento():
    pagamento.append(pedidos.pop(0))
    verificar_filas()

def mover_entrega():
    entrega.append(pagamento.pop(0))
    verificar_filas()

def entregar():
    entrega.pop(0)
    verificar_filas()
    # if len(entrega) == 0:
        # print("As filas estão vazias.")
    # else:
        # verificar_filas()

def verificar_filas():
    print(f'''\nClientes ({len(clientes)}): {clientes}
Pedidos ({len(pedidos)}): {pedidos}
Pagamento ({len(pagamento)}): {pagamento}
Entrega ({len(entrega)}): {entrega}\n''')

verificar_filas()

for i in range(5):
    entrar_cliente()

for i in range(5):
    mover_pagamento()
    entrar_cliente()

for i in range(5):
    mover_entrega()
    mover_pagamento()
    entrar_cliente()

for i in range(5):
    entregar()
    mover_entrega()
    mover_pagamento()

for i in range(5):
    entregar()
    mover_entrega()

for i in range(5):
    entregar()

print("As filas estão vazias.")

# É possível evitar o print das filas vazias e deixar apenas a mensagem de aviso.
# Para isso é necessário excluir/comentar as linhas 23 e 62, além de descomentar as linhas 24-27.
