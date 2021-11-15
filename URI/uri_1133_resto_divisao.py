#!/usr/bin/env python3

def imprimir_resto(prim,seg):
    for i in range(prim,seg):
        if i % 5 == 2 or i % 5 == 3:
            print(i)
        else:
            pass

x = int(input())
y = int(input())

if x > y:
    a = y+1
    b = x
else:
    a = x+1
    b = y

imprimir_resto(a,b)
