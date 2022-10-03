# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, utilizando as seguintes fórmulas:
# a. Para homens: (72.7*h) - 58
# b. Para mulheres: (62.1*h) - 44.7 (h = altura)

altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo (m) ou (f): ")

if sexo == "m":
    peso = (72.7*altura)-58
    print("Seu peso ideal seria: ",peso)
elif sexo == "f":
    peso = (62.1*altura)-44.7
    print("Seu peso ideal seria: ",peso)
else:
    print("Parar")