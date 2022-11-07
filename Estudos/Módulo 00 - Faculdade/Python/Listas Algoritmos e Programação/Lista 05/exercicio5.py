# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num lista a média
# de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias = []

for i in range(10):
    notas = []
    for j in range(4):
        nota = float(input(f'Informe a {j+1}ª nota do {i+1}º aluno: '))
        notas.append(nota)
    media = sum(notas)/len(notas)
    medias.append(media)

contador = 0
for media in medias:
    if media >= 7:
        contador += 1
        
print(f'{contador} alunos tiveram nota maior ou igual a 7')

