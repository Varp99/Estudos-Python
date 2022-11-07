# Faça um Programa que leia um lista de 5 números inteiros, mostre a soma, a multiplicação e os
# números.

lista = []
produto = 1

for i in range(5):
    numero = int(input(f'Informe o {i+1}º número: '))
    lista.append(numero)
    produto *= numero

soma = sum(lista)
    
print('Soma:', soma)
print('Produto:', produto)
print('Números:', lista)