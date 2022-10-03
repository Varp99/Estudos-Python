# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendose que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato
# faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
# IR (11%) : R$
# INSS (8%) : R$
# indicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

sl_hora = float(input("Digite quanto vc ganha por hora: "))
horas = float(input("Digite quantas horas vc trabalha no mês: "))

salario_bruto = sl_hora * horas
b = salario_bruto * 0.11
c = salario_bruto * 0.08
d = salario_bruto * 0.05
e = salario_bruto - b - c - d

print("Seu salário bruto é de : ", salario_bruto)
print("Valor pago ao IR : ", b)
print("Valor pago ao INSS : ", c)
print("Valor pago ao Sindicato : ", d)
print("Seu salário líquido é de : ", e)