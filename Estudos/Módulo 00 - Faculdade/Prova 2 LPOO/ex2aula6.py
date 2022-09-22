# 2- Preencha uma matriz por leitura

matriz = []

for i in range(3):
    linha = []
    for j in range(5):
        linha.append(int(input('Digite a nota[' + str(i) + ',' + str(j) + ']:')))
    matriz.append(linha) 