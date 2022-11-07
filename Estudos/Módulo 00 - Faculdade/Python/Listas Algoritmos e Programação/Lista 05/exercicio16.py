# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do
# atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que
# receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome,
# os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do
# atleta. A saída do programa deve ser conforme o exemplo abaixo:

atletas = []
saltos = []
medias = []

while True:
    atleta = input('Atleta: ')
    if atleta == '':
        break
    salto1 = float(input('Primeiro Salto: '))
    salto2 = float(input('Segundo Salto: '))
    salto3 = float(input('Terceiro Salto: '))
    salto4 = float(input('Quarto Salto: '))
    salto5 = float(input('Quinto Salto: '))
    
    atletas.append(atleta)
    saltos_atleta = [salto1, salto2, salto3, salto4, salto5]
    saltos.append(saltos_atleta)
    medias.append(sum(saltos_atleta)/len(saltos_atleta))
    
print('Resultado final:')
for i, atleta in enumerate(atletas):
    print('Atleta:', atleta)
    print('Saltos:', end=' ')
    for j, salto in enumerate(saltos[i]):
        if j != 4:
            print(salto, '- ', end='')
        else:
            print(salto,)
    print('Média dos saltos:', medias[i])