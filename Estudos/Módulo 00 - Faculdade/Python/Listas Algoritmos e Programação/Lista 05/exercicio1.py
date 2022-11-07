#Faça um Programa que leia um lista de 5 números inteiros e mostre-os.

lista = []

for i in range (5):
    num = int(input("Digite um número inteiro: "))
    lista.append(num)
print(lista)