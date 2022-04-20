#Faça um algoritmo que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias

dias = int(input("Digite uma quantidade de dias: "))

idade_em_anos = int(dias / 365)
dias = dias - idade_em_anos * 365
idade_em_meses = int(dias / 30)
dias = dias - idade_em_meses * 30

print("Sua idade em anos, meses e dias é respectivamente: ",idade_em_anos,idade_em_meses,dias )