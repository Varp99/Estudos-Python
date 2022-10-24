# Entrar com um código (numero), idade e sexo de 20 pessoas. Imprimir o código se a pessoa for do sexo masculino e tiver mais de 21 anos

lista = []

for i in range (2):
    codigo = int(input("Digite um Código: "))
    lista.append(codigo)
    idade = int(input("Digite uma idade: "))
    lista.append(idade)
    sexo = input("Digite o sexo: ")
    lista.append(sexo)
    if sexo == "masculino" and idade > 21:
        print("O código dessa pessoa é: ", codigo)



