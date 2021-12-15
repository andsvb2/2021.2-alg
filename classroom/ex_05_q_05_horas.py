#!/usr/bin/env python3

def converter_horas(num):
    if num in range(0,13):
        if num == 0:
            hora = 12
        turno = "A.M."
        return hora,turno
    elif num in range(13,24):
        hora = num - 12
        turno = "P.M."
        return hora,turno

def exibir_horas(prim,seg):
    hora,turno = converter_horas(prim)
    print(f"\n{hora}:{seg} {turno}\n")

print("Digite uma hora inválida para encerrar o programa.")

hora_entrada = 0

while hora_entrada in range(0,24):
    hora_entrada = int(input("Horas: "))
    if hora_entrada not in range(0,24):
        print(f"\nHora inválida.\nPrograma encerrado.")
        break
    minutos_entrada = int(input("Minutos: "))
    exibir_horas(hora_entrada,minutos_entrada)
