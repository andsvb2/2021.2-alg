#!/usr/bin/env python3

login = input("Login: ")

while True:
    senha = input("Senha: ")
    confirmacao = input("Confirmação de senha: ")
    if len(senha) < 8 or senha.isdigit():
        print("Digite uma senha com no mínimo 8 caracteres formada por números e letras.")
    elif senha != confirmacao:
        print("Senha e confirmação de senha são diferentes.")
    else:
        print("Senha e confirmação de senha OK.")
        break
