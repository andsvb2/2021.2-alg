#!/usr/bin/env python3

qtd_func = int(input("Quantos funcionários trabalham no setor? "))

nao_vacinados, astrazeneca, pfizer, coronavac, jansen = 0,0,0,0,0

for i in range(qtd_func):
    nome_func = input("Nome: ")
    estado_vacinal = input("Tomou alguma vacina?\nResponder com Sim ou Não. ")
    if estado_vacinal.lower().startswith('n'):
        nao_vacinados += 1
        situacao_vacina = "Não vacinado(a)"
    else:
        qual_vacina = input("Qual vacina?\nResponder com 'Astrazeneca', 'Coronavac', 'Jansen' ou 'Pfizer'.\n").lower()
        if qual_vacina.startswith('a'):
            astrazeneca +=1
            situacao_vacina = "Astrazeneca"
        elif qual_vacina.startswith('c'):
            coronavac += 1
            situacao_vacina = "Coronavac"
        elif qual_vacina.startswith('j'):
            jansen += 1
            situacao_vacina = "Jansen"
        elif qual_vacina.startswith('p'):
            pfizer += 1
            situacao_vacina = "Pfizer"
    mensagem = f"Funcionário(a): {nome_func}.\nVacina: {situacao_vacina}."
    print(mensagem)
    print()

print(f"Funcionários(as): {qtd_func}.",\
      f"Não foram vacinados(as): {nao_vacinados}.",\
      # f"Total de vacinados(as): {qtd_func - nao_vacinados}, distribuídos(as) entre as seguintes vacinas:",\
      f"Astrazeneca: {astrazeneca}.",\
      f"Coronavac: {coronavac}.",\
      f"Jansen: {jansen}.",\
      f"Pfizer: {pfizer}.",sep="\n")
