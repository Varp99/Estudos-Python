# Programa que cria uma matriz n x m preenchida com zeros

n = int(input("Digite a dimensao:"))
m = int(input("Digite a dimensao:"))
matriz = []

for i in range(n):
    linha = []
    for j in range(m):
        linha.append(0)
    matriz.append(linha)
print(matriz)