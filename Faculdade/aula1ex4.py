#Escreva um algoritmo que receba 10 valores e imprima-os em ordem crescente, decrescente e na ordem inversa a de entrada.
 
lista = []
#Faz o código se repetir 10x
for n in range(10):
    #O n+1 serve para ir incrementando o valor no input
    num = int(input(f'Digite um valor {n+1}:' ))
    #Adiciona os valores digitados dentro da lista
    lista.append(num)
#Coloca a lista na ordem inversa a de entrada
lista.reverse()
print(lista)
#Ordena a lista em ordem crescente
lista.sort()
print(lista)
#Ordena a lista em ordem decrescente
lista.sort(reverse=True)
print(lista)
