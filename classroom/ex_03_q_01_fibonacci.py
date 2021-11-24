#!/usr/bin/env python3

limite = int(input("Digite um limite para a sequência de Fibonacci: "))

# seq = [0, 1] # cria uma lista com os primeiros números da sequência
# if limite > 2:                  #
#     for i in range(2,limite):
#         novo_valor = seq[i-1] + seq[i-2]
#         seq.append(novo_valor)
#     print(seq)
# elif limite == 2:
#     print(seq)
# else:
#     print(seq[0])

prim = 0
seg = 1


for i in range(limite):
    if i <= 1:
        prox = i
    else:
        prox = prim + seg
        prim = seg
        seg = prox
    print(prox)
