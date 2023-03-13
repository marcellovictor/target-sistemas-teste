import json

with open('dados.json', 'r') as arquivo_dados:
    lista_dados = json.load(arquivo_dados)


# encontrando menor valor de faturamento e dias com faturamento 0
menor_valor = None
dia_do_menor = None

dias_sem_faturamento = []

for d in lista_dados:
    if d['valor'] == 0.0:
        dias_sem_faturamento.append(d['dia'])
    else:
        if menor_valor is None:
            menor_valor = d['valor']
            dia_do_menor = d['dia']
        elif d['valor'] < menor_valor:
            menor_valor = d['valor']
            dia_do_menor = d['dia']

print("\nDias com faturamento 0:")
for dia in dias_sem_faturamento:
    print(dia, end=" ")
print("\n\nMenor valor de faturamento:")
print(f"Dia {dia_do_menor}, valor: {menor_valor}\n")


# encontrando maior valor de faturamento
maior_valor = None
dia_do_maior = None

for d in lista_dados:
    if maior_valor is None:
        maior_valor = d['valor']
        dia_do_maior = d['dia']
    elif d['valor'] > maior_valor:
        maior_valor = d['valor']
        dia_do_maior = d['dia']

print("Maior valor de faturamento:")
print(f"Dia {dia_do_maior}, valor: {maior_valor}\n")


# encontrando os dias com faturamento acima da média mensal

soma_faturamentos = 0
for d in lista_dados:
    soma_faturamentos += d['valor']

num_dias_uteis = len(lista_dados) - len(dias_sem_faturamento)
media_mensal = soma_faturamentos / num_dias_uteis

dias_acima_da_media = []
for d in lista_dados:
    if d['valor'] > media_mensal:
        dias_acima_da_media.append(d['dia'])

print(f"Total de dias com faturamento acima da média mensal: {len(dias_acima_da_media)}")
print("Sendo eles os dias: ", end="")
for dia in dias_acima_da_media:
    print(dia, end=" ")
print("\n")


"""
OBS 1: No enunciado da questão dizia para ignorar, no cálculo da média, os 
dias em que o faturamento foi 0. Como não fazia nenhuma observação para o cálculo
do menor valor de faturamento, decidi por mostrar o menor sem contar os dias de
faturamento 0, mas também retornar uma lista com os dias em que o faturamento foi 0.


OBS 2: O python tem funções prontas que diminuiriam o código. Porém, como acredito
que o objetivo seja de avaliação, fiz uma programação mais genérica.
"""
