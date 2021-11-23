#!/usr/bin/env python3

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


print(f"A pilha tem {len(lista)} elementos.")
print(f"O último elemento é: {lista[-1]}.")

elementos_retirar = int(input("Quantos elementos devem ser desempilhados? "))

for i in range(elementos_retirar):
    lista.pop()

print(lista)


# for i in range(10):
    # lista.append(input("Digite um nome: "))

# print(lista[-1])




# #!/usr/bin/env python3

# def imprimir_resto(prim,seg):
#     for i in range(prim,seg):
#         if i % 5 == 2 or i % 5 == 3:
#             print(i)
#         else:
#             pass

# x = int(input())
# y = int(input())

# if x > y:
#     a = y+1
#     b = x
# else:
#     a = x+1
#     b = y

# imprimir_resto(a,b)
