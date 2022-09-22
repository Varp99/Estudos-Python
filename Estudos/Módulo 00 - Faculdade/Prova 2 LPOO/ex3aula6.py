#Programa que lê uma matriz 3x3 digitada pelo usuário e conta quantos números pares existem na matriz, imprimindo na tela o resultado e a matriz.

matriz =[]

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("Digite o valor [" + str(i) + "," + str(j) + "]: ")))
    matriz.append(linha)

#contar pares
pares = 0
for i in range(3):
    for j in range(3):
        if matriz [i][j] % 2 == 0:
            pares = pares + 1

#imprimir a matriz
for i in range(3):
    print(matriz [i])

#imprimir a quantidade de numeros pares
print("A quantidade de numeros pares é:", pares)