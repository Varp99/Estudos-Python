# Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []

for i in range(3):
    num = float(input("Digite um número: "))
    lista.append(num)

lista.sort(reverse=True)
print(lista)


