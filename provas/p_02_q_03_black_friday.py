#!/usr/bin/env python3

tenis,blusa,viseira,total = 0,0,0,0

menu = f'''\nDigite uma das seguintes opções.
    M: exibe o menu de opções.
    T: adiciona um tênis ao carrinho.
    B: adiciona uma blusa ao carrinho.
    V: adiciona uma viseira ao carrinho.
    Z: finaliza o programa.
    '''
print(menu)

while True:

    comando = input("\nOpção: ")

    if comando.lower() == "m":
        print(menu)
    elif comando.lower() == "t":
        tenis += 1
        desc = 0.2
        preco = float(input("Preço do tênis: "))
        total += preco - (preco * desc)
    elif comando.lower() == "b":
        blusa += 1
        desc = 0.3
        preco = float(input("Preço da blusa: "))
        total += preco - (preco * desc)
    elif comando.lower() == "v":
        viseira += 1
        desc = 0.4
        preco = float(input("Preço da viseira: "))
        total += preco - (preco * desc)
    elif comando.lower() == "z":
        print()
        print(f"Total de produtos: {tenis + blusa + viseira}.",f"TOTAL A PAGAR: {total:.2f}",sep="\n")
        # print(f"Total de produtos: {tenis + blusa + viseira}.",f"Tênis: {tenis}.",f"Blusas: {blusa}.",f"Viseiras: {viseira}.",f"\nTOTAL A PAGAR: {total:.2f}",sep="\n")
        break
    else:
        print("Opção inválida.\nDigite 'M' para visualizar o menu.")
