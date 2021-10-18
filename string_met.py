#!/usr/bin/env python3

nome = input("Digite um nome: ")
print(nome)
# nome_alterado = nome.upper()
# print(nome_alterado)

# if nome_alterado == "RENATA":
#     print("Sou eu.")

# nome_alterado = nome.startswith("R")

for i in nome.split():
    print(i)

nome1,nome2 = nome.split()
print(nome1,nome2, sep="\n")
