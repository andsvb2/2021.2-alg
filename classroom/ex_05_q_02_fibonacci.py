#!/usr/bin/env python3

def fibonacci(limite):
    seq = [0, 1]          # É preciso inicializar a sequência com os dois primeiros números
    if limite > 2:              # Cria a lista de números
        for i in range(2,limite):
            novo_valor = seq[i-1] + seq[i-2]
            seq.append(novo_valor)
    elif limite == 1:       # Mantem uma lista sendo retornada, mas apenas com um número
        seq.pop()
    print(f"Sequência Fibonacci com {limite} número: {seq}") if len(seq) == 1 else print(f"Sequência Fibonacci com os {limite} primeiros números: {seq}")


fibonacci(int(input("Digite um limite para a sequência de Fibonacci: ")))
