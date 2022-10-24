# Criar um algoritmo que leia um número que será o limite superior de um intervalo e imprimir todos os números ímpares menores do que esse número.
# Exemplo:
# Limite superior: 15
# Saída: 1 3 5 7 9 11 13

limite = int(input("Digite um número para ser o limite superior: "))

for i in range (limite -1, 0, -1):
    if i%2 != 0:
        print(i)