#!/usr/bin/env python3

# import math

def verifica_num_primo(num):
    if x in [2,3,5,7,11]:
        return True
    elif x % 2 == 0:
        return False
    # A construção de sum abaixo é uma ideia retirada do link
    # https://www.kite.com/python/answers/how-to-sum-the-digits-of-a-number-in-python
    # elif sum(int(i) for i in str(x)) % 3 == 0:
    elif x % 3 == 0:
        return False
    elif x % 5 == 0:
        return False
    elif x % 7 == 0:
        return False
    else:
        return True

    if num > 1:
        # fórmula adaptada de https://www.programiz.com/python-programming/examples/prime-number
        for i in range(2,num):#math.floor(math.sqrt(num)+1)):
            if (num % i) == 0:
                return False
                break
            else:
                return True
    else:
        return False


num = int(input("Qual número gostaria de verificar? "))
print(f"{num} é um número primo.") if verifica_num_primo(num) is True else print(f"{num} não é um número primo.")
