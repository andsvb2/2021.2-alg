#!/usr/bin/env python3

# cria lista com os 40 nomes mais comuns no Brasil
# fonte: https://pt.wikipedia.org/wiki/Lista_de_prenomes_mais_comuns_no_Brasil
# nomes = ['José', 'Maria', 'João', 'Ana', 'Antônio', 'Francisca', 'Francisco', 'Antônia', 'Carlos', 'Adriana', 'Paulo', 'Juliana', 'Pedro', 'Márcia', 'Lucas', 'Fernanda', 'Luiz', 'Patrícia', 'Marcos', 'Aline', 'Luís', 'Sandra', 'Gabriel', 'Camila', 'Rafael', 'Amanda', 'Daniel', 'Bruna', 'Marcelo', 'Jéssica', 'Bruno', 'Letícia', 'Eduardo', 'Júlia', 'Felipe', 'Luciana', 'Raimundo', 'Vanessa', 'Rodrigo', 'Mariana']

clientes = ['José', 'Maria', 'João', 'Ana', 'Antônio', 'Francisca', 'Francisco', 'Antônia', 'Carlos', 'Adriana', 'Paulo', 'Juliana', 'Pedro', 'Márcia', 'Lucas']

pedidos,pagamento,entrega = [],[],[]
# tmp_clientes_pedidos,tmp_pedidos_pagamento,tmp_pagamento_entrega = [],[],[]

def entrar_cliente():
    pedidos.append(clientes.pop(0))
    verificar_filas()
    # return pedidos

def mover_pagamento():
    pagamento.append(pedidos.pop(0))
    verificar_filas()
    # return pagamento

def mover_entrega():
    entrega.append(pagamento.pop(0))
    verificar_filas()
    # return entrega

def entregar():
    entrega.pop(0)
    verificar_filas()
    # return entrega

def verificar_filas():
    print(f'''\nClientes: {clientes}
Pedidos: {pedidos}
Pagamento: {pagamento}
Entrega: {entrega}\n''')

# for i in range(len(clientes)):
#     entrar_cliente()
#     if len(pedidos) == 5:
#         for i in range(len(pedidos)):
#             mover_pagamento()
#             if len(pagamento) == 5:
#                 for i in range(len(pagamento)):
#                     mover_entrega()
#                     if len(entrega) == 5:
#                         entregar()


while len(clientes) != 0:
    entrar_cliente()
    if len(pedidos) == 5:
        mover_pagamento()
        if len(pagamento) == 5:
            mover_entrega()
            if len(entrega) == 5:
                entregar()

while True:
    if len(clientes) == len(pedidos) == len(pagamento) == len(entrega) == 0:
        print("Filas esvaziadas.")
        break

    if len(pedidos) != 0:
        mover_pagamento()
    if len(pagamento) != 0:
        mover_entrega()
    if len(entrega) != 0:
        entregar()
