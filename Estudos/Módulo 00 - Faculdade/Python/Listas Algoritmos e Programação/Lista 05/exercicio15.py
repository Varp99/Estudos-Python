# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com
# base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas
# daquela semana.
# Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9
# por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de
# contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de
# valores:
# a. $200 - $299
# b. $300 - $399
# c. $400 - $499
# d. $500 - $599
# e. $600 - $699
# f. $700 - $799
# g. $800 - $899
# h. $900 - $999
# i. $1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs
# aninhados.

valores = []

for i in range(200, 1000, 100):
    valores.append([i, i+99, 0])

# print(valores) 

salarios = []
while True:
    venda = float(input('Informe o valor da venda, infome -1 pra sair: '))
    if venda == -1:
        break
    salarios.append(200 + 0.09*venda)

maior_1000 = 0
for salario in salarios:
    for i, item in enumerate(valores):
        minimo, maximo, total = item
        if minimo <= salario < maximo:
            valores[i][2] += 1
            break
        if salario > 1000:
            maior_1000 += 1
            break
for minimo, maximo, total in valores:
    print(f'Entre {minimo} e {maximo}:', total)
print('Mais que mil:', maior_1000)