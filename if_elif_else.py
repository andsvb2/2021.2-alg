#!/usr/bin/env python3

num = int(input("Digite um número: "))

# if num % 2 == 0:
#     if num % 3 == 0:
#         print("O número é divisível por 2 e por 3.")
#     else:
#         print("O número é divisível por 2.")
# elif num % 3 == 0:
#     print("O número é divisível por 3.")
# else:
#     print("Não é divisível nem por 2, nem por 3.")

if num >= 0 or num <= 100:
    if num < 70:
        print("Não passou.")
    else:
        print("Passou.")
else:
    print("Nota inválida.")


if num < 0 or num > 100:
    print("Nota inválida.")
else:
    if num < 70:
        print("Não passou.")
    else:
        print("Passou.")
