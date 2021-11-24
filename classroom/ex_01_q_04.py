#!/usr/bin/env python3

# Faça um programa que peça a temperatura em graus Farenheit, transforme e
# mostre a temperatura em graus Celsius seguindo a fórmula C = (5 * (F-32) / 9).

temp_far = float(input("Digite a temperatura em Fahrenheit: "))
temp_celsius = 5 * (temp_far - 32) / 9

print(f"A temperatura em Celsius é de {temp_celsius:.2f} ℃.")
