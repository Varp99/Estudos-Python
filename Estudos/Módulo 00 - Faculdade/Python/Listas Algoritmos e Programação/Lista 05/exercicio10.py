# Altere o programa anterior, intercalando 3 listaes de 10 elementos cada.

lista1 = []
lista2 = []
lista3 = []
lista4 = []

for i in range(10):
    numero = input(f'Informe o {i+1}º elemento da lista 1: ')
    lista1.append(numero)
    
for i in range(10):
    numero = input(f'Informe o {i+1}º elemento da lista 2: ')
    lista2.append(numero)
    
for i in range(10):
    numero = input(f'Informe o {i+1}º elemento da lista 3: ')
    lista3.append(numero)
    
for i in range(10):
    lista4.append(lista1[i])
    lista4.append(lista2[i])
    lista4.append(lista3[i])

print('Lista 4:', lista4)