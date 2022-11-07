# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma
# lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da
# média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . .
# . ).

meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]

temperaturas = []

for mes in meses:
    temperatura = float(input(f'Informe a temperatura no mês de {mes}: '))
    temperaturas.append(temperatura)
    
media = sum(temperaturas)/len(temperaturas)
print('A média foi:', media)
for i, temperatura in enumerate(temperaturas):
    if temperatura > media:
        print('A temperatura do mês de', meses[i], 'foi maior que a média:', temperatura)
