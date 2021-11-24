#!/usr/bin/env python3

def encontrar_coordenada(prim,seg):
    if prim > 0.0:
        if seg > 0.0:
            local = "Q1"
        else:
            local = "Q4"
    else:
        if seg > 0.0:
            local = "Q2"
        else:
            local = "Q3"
    print(f"\nA coordenada está no quadrante {local}.\n")

while True:
    x = float(input("Insira a coordenada X: "))
    y = float(input("Insira a coordenada Y: "))

    if x == 0 or y ==0:
        print("Uma das coordenadas é zero.\nPrograma finalizado.")
        break
    else:
        encontrar_coordenada(x,y)
