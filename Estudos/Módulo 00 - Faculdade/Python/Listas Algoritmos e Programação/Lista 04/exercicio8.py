# Entrar com 20 números e imprimir a soma dos números cujos quadrados são menores do que 225.

soma = 0
lista = []

for i in range (5):
    num = int(input('Digite um valor: '))
    lista.append(num)

    if lista[i]**2 < 225:
        soma = soma + lista[i]

print(soma)

