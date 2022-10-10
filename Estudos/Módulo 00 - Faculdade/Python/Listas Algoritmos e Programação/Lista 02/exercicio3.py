#Faça um Programa que verifique se o numero digitado é "1" ou "2". Conforme o numero escrever: 1- Feminino, 2-Masculino ou Sexo Inválido.

num = float(input("Digite 1 ou 2: "))

if num == 1:
    print("1- Feminino")
elif num == 2:
    print("2- Masculino")
else:
    print("Sexo inválido")