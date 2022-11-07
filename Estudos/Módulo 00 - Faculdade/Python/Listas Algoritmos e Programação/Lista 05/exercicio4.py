# Faça um Programa que leia 20 números inteiros e armazene-os num lista. Armazene os números
# pares no lista PAR e os números IMPARES no lista impar. Imprima os três listaes

lista = []
par = []
impar = []

for i in range (20):
    num = int(input("Digite um número: "))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print("Todos os números: ", lista)
print("Números pares: ", par)
print("Números impares: ", impar)