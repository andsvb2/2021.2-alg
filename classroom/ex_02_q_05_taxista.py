#!/usr/bin/env python3

dist_km = float(input("Quilômetros: "))

if dist_km <= 500:
    tarifa = 0.75
else:
    tarifa = 0.65

total = 20 + (dist_km * tarifa)
print(f"Total a pagar: R$ {total:.2f}.")
