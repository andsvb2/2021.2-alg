#!/usr/bin/env python3

# cria lista com os 40 nomes mais comuns no Brasil
# fonte: https://pt.wikipedia.org/wiki/Lista_de_prenomes_mais_comuns_no_Brasil
# nomes = ['José', 'Maria', 'João', 'Ana', 'Antônio', 'Francisca', 'Francisco', 'Antônia', 'Carlos', 'Adriana', 'Paulo', 'Juliana', 'Pedro', 'Márcia', 'Lucas', 'Fernanda', 'Luiz', 'Patrícia', 'Marcos', 'Aline', 'Luís', 'Sandra', 'Gabriel', 'Camila', 'Rafael', 'Amanda', 'Daniel', 'Bruna', 'Marcelo', 'Jéssica', 'Bruno', 'Letícia', 'Eduardo', 'Júlia', 'Felipe', 'Luciana', 'Raimundo', 'Vanessa', 'Rodrigo', 'Mariana']

clientes = ['José', 'Maria', 'João', 'Ana', 'Antônio', 'Francisca', 'Francisco', 'Antônia', 'Carlos', 'Adriana', 'Paulo', 'Juliana', 'Pedro', 'Márcia', 'Lucas']

pedidos,pagamento,entrega = [],[],[]
# tmp_clientes_pedidos,tmp_pedidos_pagamento,tmp_pagamento_entrega = [],[],[]

estado_das_filas = f'''\nClientes: {clientes}
Pedidos: {pedidos}
Pagamento: {pagamento}
Entrega: {entrega}\n'''

for i in range(len(clientes)):
    tmp_clientes_pedidos = clientes.pop(0)
    pedidos.append(tmp_clientes_pedidos)
    print(estado_das_filas)
    if len(pedidos) == 5:
        tmp_pedidos_pagamento = pedidos.pop(0)
        pagamento.append(tmp_pedidos_pagamento)
        print(estado_das_filas)
        if len(pagamento) == 5:
            tmp_pagamento_entrega = pagamento.pop(0)
            entrega.append(tmp_pagamento_entrega)
            print(estado_das_filas)


# while True:

#     cliente_p_pedido = clientes.pop(0)
#     pedidos.append(cliente_p_pedido)
#     print(estado_das_filas)

    # for i in clientes:
    #     cliente_p_pedido = clientes.pop(0)
    #     pedidos.append(cliente_p_pedido)
    #     print(estado_das_filas)
    #     if len(pedidos) == 5:
    #         cliente_p_pagamento = pedidos.pop(0)
    #         pagamento.append(cliente_p_pagamento)
    #         print(estado_das_filas)
    #         if len(pagamento) == 5:
    #             cliente_p_entrega = pagamento.pop(0)
    #             entrega.append(cliente_p_entrega)
    #             print(estado_das_filas)


    # if len(clientes) == len(pedidos) == len(pagamento) == len(entrega) == 0:
    #     print("Filas esvaziadas.")
    #     break
