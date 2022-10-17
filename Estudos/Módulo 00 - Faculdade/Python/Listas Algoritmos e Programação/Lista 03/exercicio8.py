# Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []

for i in range(5):
    num = float(input('Digite um numero: '))
    numeros.append(num)

soma = sum(numeros)
print("A Soma é: ", soma)
print("A média é: ", soma/5)