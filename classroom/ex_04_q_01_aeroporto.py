#!/usr/bin/env python3

voos = ['AD2819', 'G32168', 'LA4521', 'AD4424', 'AD4902', 'AD4068', 'LA3280']

menu = f'''\nDigite uma das seguintes opções.
    0: Exibir menu de opções.
    1: Listar o número de aviões aguardando na fila de decolagem.
    2: Autorizar a decolagem do próximo avião.
    3: Adicionar um avião à fila de espera.
    4: Listar todos os aviões na fila de espera.
    5 (ou 'Fim'): Finalizar o programa.
    '''
print(menu)

while True:

    comando = input("\nOpção: ")

    if comando.isdigit():
        comando_int = int(comando)
        if comando_int == 0:
            print(menu)
        elif comando_int == 1:
            print(f"Aviões na fila de decolagem: {len(voos)}.")
        elif comando_int == 2:
            voo_autorizado = voos.pop(0)
            print(f"Voo autorizado para decolagem: {voo_autorizado}.")
        elif comando_int == 3:
            voos.append(input("Código do voo a ser adicionado: "))
        elif comando_int == 4:
            print(f"Posição\t --\tCódigo")
            for i in voos:
                print(f"   {(voos.index(i))+1}\t --\t{i}")
        elif comando_int == 5:
            print("Programa finalizado.")
            break
        else:
            print("Digite uma opção válida ou 0 para visualizar o menu.")
    elif comando == "Fim":
        print("Programa finalizado.")
        break
    else:
        print("Digite uma opção válida ou 0 para visualizar o menu.")
