#Programa que lê uma matriz 3 x 3 digitada pelo usuário e conta quantos números pares existem na matriz, imprimindo na tela o resultado e a matriz

matriz = []

for i in range (3):
    linha = []
    for j in range (3):
        linha.append (int(input('Digite o valor de ['+ str (i) + ',' + str (j) + ']:')))
    matriz.append (linha)

par = 0
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            par = par + 1

for i in range(3):
    print(matriz[i])

print("A matriz possui", par, "números pares")
