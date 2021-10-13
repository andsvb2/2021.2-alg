#!/usr/bin/env python3

import time
start_time = time.time()

# 1018

quantias = [576, 11257, 503]
cedulas = [100, 50, 20, 10, 5, 2, 1]

ced_100 = 0
ced_50 = 0
ced_20 = 0
ced_10 = 0
ced_5 = 0
ced_2 = 0
ced_1 = 0
resto = 0

def conta_cedulas():
    while quantia != 0:
        if quantia > 100:
            ced_100 = quantia // 100
            resto %= 100
            if resto > 50:
                ced_50 = resto // 50
                resto %= 50


# quantia = int(input())
# nota_100 = quantia // 100
# sobra_100 = quantia % 100
# nota_50 = sobra_100 // 50
# sobra_50 = sobra_100 % 50
# nota_20 = sobra_50 // 20
# sobra_20 = sobra_50 % 20
# nota_10 = sobra_20 // 10
# sobra_10 = sobra_20 % 10
# nota_05 = sobra_10 // 5
# sobra_05 = sobra_10 % 5
# nota_02 = sobra_05 // 2
# sobra_02 = sobra_05 % 2
# nota_01 = sobra_02 // 1

# print(quantia, f"{nota_100} nota(s) de R$ 100,00",
#       f"{nota_50} nota(s) de R$ 50,00", f"{nota_20} nota(s) de R$ 20,00",
#       f"{nota_10} nota(s) de R$ 10,00", f"{nota_05} nota(s) de R$ 5,00",
#       f"{nota_02} nota(s) de R$ 2,00", f"{nota_01} nota(s) de R$ 1,00",
#       sep='\n')

print("--- %s seconds ---" % (time.time() - start_time))
