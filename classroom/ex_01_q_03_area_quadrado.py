#!/usr/bin/env python3

# Faça um programa que calcule a área de um quadrado recebendo do usuário o
# tamanho do lado em centímetros, em seguida mostre o dobro desta área para o
# usuário.

lado = float(input("Qual o tamanho, em cm, do lado?\t"))
area = lado ** 2
dobro_area = area * 2
print(f"O dobro da área é {dobro_area:.2f} cm².")
