# Faça um programa que leia 5 números e informe o maior número.

numeros = []

for i in range(5):
    num = float(input('Digite um numero: '))
    numeros.append(num)

print('O maior valor é : ', max(numeros))
