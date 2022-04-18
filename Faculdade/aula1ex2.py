#Faça um algoritmo que leia a idade de uma pessoa e expressa em dias e mostre-a expressa em anos, meses e dias

dias = int(input("Digite uma quantidade de dias: "))

idade_em_anos = dias // 365
idade_em_meses = dias // 30

print(dias, idade_em_meses, idade_em_anos)