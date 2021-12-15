#!/usr/bin/env python3

import math

def verifica_primo(num):
    if num < 2:
        return False
    elif num == 2 or num == 3:
        return True
    else:
        for i in range(2,math.floor(math.sqrt(num)+1)):
            if (num % i) == 0:
                return False
        return True

entrada = int(input("Qual número gostaria de verificar? "))

print(f"{entrada} é um número primo.") if verifica_primo(entrada) is True else print(f"{entrada} não é um número primo.")
