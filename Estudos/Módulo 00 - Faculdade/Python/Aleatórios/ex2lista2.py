#Faça um programa que preencha por leitura um vetor de 10 posições, e conta quantos valores diferentes existem no vetor.

vetor = []

for i in range(10):
   pos = int(input("Digite o %d valor da posição: " % (int(len(vetor))+1)))
   vetor.append(pos)
print("Vetor: ", vetor)

valor_diferente = []
for i in vetor:
    if i not in valor_diferente:
        valor_diferente.append(i)
print("\nA qtd de valores diferentes é: ", (len(valor_diferente)))


class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calc_perimetro(self):
        valores = int(input("Digite um valor:"))
        perimetro 