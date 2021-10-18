#!/usr/bin/env python3

# Leia 2 valores com uma casa decimal (x e y), que devem representar as
# coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao
# qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem
# (x = y = 0).

entrada = input()
x,y = entrada.split()
x = float(x)
y = float(y)
# coord = [float(i) for i in entrada.split()]
local = None

if x == 0.0:
    if y == 0.0:
        local = "Origem"
    else:
        local = "Eixo X"
elif y == 0.0:
    local = "Eixo Y"
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


# if coord[0] == 0.0 and coord[1] == 0.0:
#     local = "Origem"
# else:
#     if coord[0] > 0:
#         if coord[1] > 0:
#             local = "Q1"
#         else:
#             local = "Q4"
#     else:
#         if coord[1] > 0:
#             local = "Q2"
#         else:
#             local = "Q3"

print(local)
