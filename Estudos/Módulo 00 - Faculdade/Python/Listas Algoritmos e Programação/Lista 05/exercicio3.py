# Faça um Programa que leia 4 notas, mostre as notas e a média na tela

lista = []

for i in range (4):
    num = float(input("Digite uma nota: "))
    lista.append(num)

print("Essas foram as notas: ", lista)
media = sum(lista)/4
print("A média das notas são: ", media)