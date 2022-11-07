# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos
# alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = []
alturas = []

for i in range(5):
    idade = int(input(f'Informe a {i+1}ª idade: '))
    altura = float(input(f'Informe a {i+1}ª altura: '))
    idades.append(idade)
    alturas.append(altura)

contador = 0
media = sum(alturas)/len(alturas)

for i in range(5):
    if idades[i] > 13 and alturas[i] < media:
        contador += 1

print(contador, 'alunos possuem mais de 13 anos e altura inferior à média.')
