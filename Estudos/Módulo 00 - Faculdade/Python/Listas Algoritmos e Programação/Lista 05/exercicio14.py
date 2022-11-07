# Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser
# armazenado). Após esta entrada de dados, faça:
# a. Mostre a quantidade de valores que foram lidos;
# b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# d. Calcule e mostre a soma dos valores;
# e. Calcule e mostre a média dos valores;
# f. Calcule e mostre a quantidade de valores acima da média calculada;
# g. Calcule e mostre a quantidade de valores abaixo de sete;
# h. Encerre o programa com uma mensagem;

notas = []
nota = 0
while nota != -1:
    nota = float(input(f'Informe a nota: '))
    if nota != -1:
        notas.append(nota)

print('Foram lidos', len(notas), 'valores')

for nota in notas:
    print(nota, '', end='')

notas.reverse()
for nota in notas:
    print(nota)

print('A soma foi', sum(notas))
media = sum(notas)/len(notas)
print('A média foi', media)

acima_media = 0
abaixo_sete = 0
for nota in notas:
    if nota > media:
        acima_media += 1
    if nota < 7:
        abaixo_sete += 1

print('A quantidade de valores acima da média foi', acima_media)
print('A quantidade de valores abaixo de sete foi', abaixo_sete)
print('Fim do programa')