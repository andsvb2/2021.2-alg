#!/usr/bin/env python3

import re

while True:
    entrada = input("Insira as coordenadas do ponto.\nQuando quiser parar o programa, digite 0 (zero) em uma das coordenadas.\n\t")
    if re.search(',',entrada):
        x,y = [float(i) for i in entrada.split(',')]
    elif re.search(' ', entrada):
        x,y = [float(i) for i in entrada.split()]

    if x == 0 or y == 0:
        print("Uma das coordenadas é zero.")
        break
    elif x > 0.0:
        if y > 0.0:
            local = "Q1"
        else:
            local = "Q4"
    else:
        if y > 0.0:
            local = "Q2"
        else:
            local = "Q3"
    print(local)
