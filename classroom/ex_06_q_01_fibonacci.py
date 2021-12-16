#!/usr/bin/env python3

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

limite = int(input("Qual o limite desejado? "))

resultado = fibonacci(limite)

print(resultado)
