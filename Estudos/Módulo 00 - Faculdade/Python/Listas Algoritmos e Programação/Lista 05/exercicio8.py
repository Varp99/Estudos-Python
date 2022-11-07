#  Faça um Programa que leia um lista A com 10 números inteiros, calcule e mostre a soma dos
# quadrados dos elementos do lista.

A = []

for i in range(10):
    numero = int(input(f'Informe o {i+1}º número: '))
    A.append(numero)

soma = 0

for numero in A:
    soma += numero * numero
    
print('Soma dos quadrados dos elementos:', soma)