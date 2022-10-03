#Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. Faça um programa que determine o percentual de ocorrências
#de face 6 do dado dentre esses 50 lançamentos

import random
vetor = []
face_dado = 6

#Lançamento do dado
for i in range(50):
   vetor.append(random.randint(1,6))
print("O resultado dos 50 lançamentos foram: \n{}" .format(vetor))
ocorrencias = vetor.count(face_dado)

#parte de calcular percentual
porcentagem = (ocorrencias/50)*100
print("\nO percentual de ocorrencias é %.2f" %(porcentagem),"%")







