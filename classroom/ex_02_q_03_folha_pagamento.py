#!/usr/bin/env python3

INSS_ALIQ = 0.12
slr_bruto = float(input("Salário bruto: "))

if slr_bruto <= 1000:
    ir_aliq = 0.0
elif slr_bruto <= 1500:
    ir_aliq = 0.09
elif slr_bruto <= 2500:
    ir_aliq = 0.15
else:
    ir_aliq = 0.3

inss_desc = slr_bruto * INSS_ALIQ
ir_desc = slr_bruto * ir_aliq
descontos =  inss_desc + ir_desc
slr_liquido = slr_bruto - descontos

print(f"Salário bruto: R$ {slr_bruto:.2f}",
    f"IR: R$ {ir_desc:.2f}",
    f"INSS: R$ {inss_desc:.2f}",
    f"Soma dos descontos: R$ {descontos:.2f}",
    f"Salário líquido: R$ {slr_liquido:.2f}",
    sep="\n")
