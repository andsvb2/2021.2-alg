#!/usr/bin/env python3

processos = []

def listar_processos():
    print(f"\nPosição\t --\tProcesso")
    for i in processos:
        print(f"   {(processos.index(i))+1}\t --\t{i}")

menu = f'''\nDigite uma das seguintes opções.
    0: exibe o menu de opções.
    Adicionar: adiciona um processo à fila.
    Remover: remove um processo da fila.
    Fim: finaliza o programa.
    '''
print(menu)

while True:

    comando = input("\nOpção: ")

    if comando == "0":
        print(menu)
    elif comando.lower() == "adicionar":
        tmp_processo = input("Processo a ser adicionado: ")
        processos.append(tmp_processo)
        listar_processos()
    elif comando.lower() == "remover":
        processo_removido = processos.pop(0)
        print(f"\nProcesso removido: {processo_removido}.")
        listar_processos()
    elif comando.lower() == "fim":
        print("\nPrograma finalizado.")
        break
    else:
        print("\nOpção inválida.\nDigite 0 para visualizar o menu.")
