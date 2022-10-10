# Peça para o usuário ir digitando números, quando ele digitar -99 o programa para e mostra a soma dos valores digitados anteriormente.

lista = []
num = 0

while num != -99:
    num = int(input("Digite um número: "))
    if num != -99:
        lista.append(num)
        soma = sum(lista)
    
print(lista)
print(soma)
print("A média dos valores anteriores é: ", soma/2)