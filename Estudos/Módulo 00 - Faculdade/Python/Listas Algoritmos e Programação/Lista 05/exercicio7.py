# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu
# respectivo lista. Imprima a idade e a altura na ordem inversa a ordem lida.

lista = []
produto = 1

for i in range(5):
    idade = int(input(f'Informe a {i+1}ª idade: '))
    altura = float(input(f'Informe a {i+1}ª altura: '))
    lista.append([idade, altura])

lista.reverse()

for idade, altura in lista:
    print(f'Idade:', idade, 'Altura:', altura)