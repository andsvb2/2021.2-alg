#!/usr/bin/env python3

def conta_a(x):
    if not x:
        return 0
    else:
        if not x[0].isalpha():
            return 0 + conta_a(x[1:])
        else:
            if x[0] == 'a':
                return 1 + conta_a(x[1:])
            else:
                return 0 + conta_a(x[1:])

# def conta_caracteres(x):
#     if not x:
#         return 0
#     else:
#         return 1 + conta_caracteres(x[1:])

entrada = input("Qual a string? ").lower()
qtd_a = conta_a(entrada)
# qtd_total = conta_caracteres(entrada)


print(f"A entrada digitada, '{entrada}', contem {qtd_a} 'A'.")
