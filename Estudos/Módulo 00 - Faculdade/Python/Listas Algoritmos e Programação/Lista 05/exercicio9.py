# Faça um Programa que leia dois listaes com 10 elementos cada. Gere um terceiro lista de 20
# elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros
# listaes

lista1 = []
lista2 = []
lista3 = []

for i in range(10):
    numero = input(f'Informe o {i+1}º elemento da lista 1: ')
    lista1.append(numero)
    
for i in range(10):
    numero = input(f'Informe o {i+1}º elemento da lista 2: ')
    lista2.append(numero)
    
for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print('Lista 3:', lista3)