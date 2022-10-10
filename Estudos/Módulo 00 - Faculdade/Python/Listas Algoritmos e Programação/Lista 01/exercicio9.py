#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.C = (5 * (F-32) / 9).

faren = float(input("Digite uma temperatura em Farenheit: "))
c = (5*(faren-32)/9)
print("Essa temperatura em Celsius é: ",c)