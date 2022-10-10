# Faça um programa que peça um valor e mostre na tela se o valor é positivo, negativo ou nulo.

valor = float(input("Digite um valor: "))

if valor > 0:
    print("Valor positivo")
elif valor == 0:
    print("Valor nulo")
else:
    print("Valor Negativo")
