# Criar um algoritmo que imprima a soma dos números pares entre 25 e 200.

soma = 0

for i in range (25, 201):
    if i % 2 == 0:
        soma = soma + i
print(soma)
