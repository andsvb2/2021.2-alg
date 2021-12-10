#!/usr/bin/env python3

def checar_palindromo(palavra):
    # como reverter a string foi aprendido aqui: https://www.w3schools.com/python/python_howto_reverse_string.asp
    if palavra.strip().lower() == palavra[::-1].strip().lower():
        return True
    else:
        return False

entrada = input("Qual a palavra para checar? ")
# estado = checar_palindromo(entrada) # parece ser desnecessário
print(f"{entrada} é um palíndromo.") if checar_palindromo(entrada) else print(f"{entrada} não é um palíndromo.") # O is True após checar_palindromo(entrada) é opcional.
