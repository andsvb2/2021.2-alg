#!/usr/bin/env python3

# cria lista com os 40 nomes mais comuns no Brasil
# fonte: https://pt.wikipedia.org/wiki/Lista_de_prenomes_mais_comuns_no_Brasil
nomes = ['José', 'Maria', 'João', 'Ana', 'Antônio', 'Francisca', 'Francisco', 'Antônia', 'Carlos', 'Adriana', 'Paulo', 'Juliana', 'Pedro', 'Márcia', 'Lucas', 'Fernanda', 'Luiz', 'Patrícia', 'Marcos', 'Aline', 'Luís', 'Sandra', 'Gabriel', 'Camila', 'Rafael', 'Amanda', 'Daniel', 'Bruna', 'Marcelo', 'Jéssica', 'Bruno', 'Letícia', 'Eduardo', 'Júlia', 'Felipe', 'Luciana', 'Raimundo', 'Vanessa', 'Rodrigo', 'Mariana']

estacionamento = []
patio_manobra = []

# Cria lista estacionamento com 30 elementos da lista nomes
for i in range(30):
    estacionamento.append(nomes[i])

# Cria loop que dura enquanto houver elementos na lista estacionamento
while not (len(estacionamento) == 0):
    cliente = input("Dono(a) do carro a retirar: ")
    if cliente not in estacionamento: # Testa se o nome do dono está na lista estacionamento
        print("Cliente não encontrado.")
    else:
        posicao = estacionamento.index(cliente)
        for i in range((len(estacionamento)-1) - posicao):
            tmp = estacionamento.pop()
            patio_manobra.append(tmp)
        estacionamento.pop()
        while not (len(patio_manobra) == 0):
            patio_p_estacionamento = patio_manobra.pop()
            estacionamento.append(patio_p_estacionamento)
        print(f"Estacionamento: {estacionamento}")
