# Faça um programa que leia e valide as seguintes informações:
# b. Idade: entre 0 e 150;
# c. Salário: maior que zero;
# d. Sexo: 1-feminino ou 2-masculino;
# e. Estado Civil: 1-solteiro, 2-casado, 3-viuvo, 4-divorciado;

idade = int(input("Digite uma idade entre 0 e 150: "))
while idade < 0 or idade > 150:
    print("Idade inválida")
    idade = int(input("Digite uma idade entre 0 e 150: "))

salario = float(input("Digite seu salario: "))
while salario < 0:
    print("Salário inválido")
    salario = float(input("Digite seu salario: "))

sexo = int(input("Digite seu sexo 1- Feminino ou 2- Masculino: "))
while sexo < 1 or sexo > 2:
    print("Sexo inválido")
    sexo = int(input("Digite seu sexo 1- Feminino ou 2- Masculino: "))
if sexo == 1:
    sexo = "feminino"
elif sexo == 2:
    sexo = "masculino"

estado = int(input("Digite seu estado civil 1- Solteiro, 2- Casado, 3- Viúvo, 4- Divorciado: "))
while estado < 1 or estado > 4:
    print("Estado Civil inválido")
    estado = int(input("Digite seu estado civil 1- Solteiro, 2- Casado, 3- Viúvo, 4- Divorciado: "))
if estado == 1:
    estado = "Solteiro"
elif estado == 2:
    estado = "Casado"
elif estado == 3:
    estado = "Viúvo"
elif estado == 4:
    estado = "Divorciado"

print("Sua idade é: ", idade)
print("Seu salário é: ", salario)
print("Seu sexo é: ", sexo)
print("Seu estado civil é: ", estado)


