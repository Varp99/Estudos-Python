#Programa para fazer a conversão de Fahreinheit para Celsius

fahreinheit = int(input("Digite a temperatura em Fahreinheit: "))

celsius = (fahreinheit - 32) * 5 / 9
print("A temperatura em Celsius seria: {} Celsius ".format(celsius))