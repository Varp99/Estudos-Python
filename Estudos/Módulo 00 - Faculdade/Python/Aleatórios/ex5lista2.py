#Faça um programa que leia um vetor vet de 20 números inteiros. O programa deve gerar, a partir do vetor lido, um outro vetor pos que
#contenha apenas os valores inteiros positivos de vet. A partir do vetor pos, deve ser gerado um outro vetor semdup que contenha apenas
#uma ocorrência de cada valor de pos.

vetor = []

for i in range(20):
    pos = int(input("Digite o %d valor: " %(i+1)))
    vetor.append(pos)   
print("Valores positivos: ")

if len(vetor) > 0:
    pos = []
    for i in vetor:
        if i > 0:
            pos.append(i)
    print(pos)

semduplicidade = []
for i in pos:
    if i not in semduplicidade:
        semduplicidade.append(i)
print("Valores sem duplicidade: ")
print(semduplicidade)
