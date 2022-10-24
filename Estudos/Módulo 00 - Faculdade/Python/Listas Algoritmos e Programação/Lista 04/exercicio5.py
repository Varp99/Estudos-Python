# Criar um algoritmo que leia um número que servirá para controlar os números pares que serão impressos a partir de 2.
# Exemplo:
# Quantos: 4
# Saída: 2 4 6 8

num = int(input("Digite a quantidade de valores: "))

for i in range(num):
    print(i*2+2)