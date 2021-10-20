#!/usr/bin/env python3

idade = int(input("Idade: "))

if idade < 16:
    print("Não eleitor.")
elif 18 > idade >= 16 or idade >= 65:
    print("Eleitor facultativo.")
else:
    print("Eleitor obrigatório.")
    if idade == 18:
        sexo = input("Informe seu sexo, digitando M ou F: ")
        if sexo.lower() == "m":
            print("Lembre do seu Alistamento Militar.")
