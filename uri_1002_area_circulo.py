#!/usr/bin/env python3

## 1002

# Valores teste: 2.00, 100.64, 150.00

n = 3.14159
raio = input()
area = n * (float(raio) ** 2)

# print("A=%.4f" % (area))        # String.format()
print(f"A={area:.4f}")          # f-strings
