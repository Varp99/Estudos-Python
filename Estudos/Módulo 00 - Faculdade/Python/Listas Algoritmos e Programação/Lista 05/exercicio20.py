# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de
# modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros,
# isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e
# mostre:

print('Comparativo de Consumo de Combustível')
veiculos = []
autonomias = []
for i in range(5):
    print('Veículo', i+1)
    veiculo = input('Nome: ')
    autonomia = float(input('Km por litro: '))
    veiculos.append(veiculo)
    autonomias.append(autonomia)
    
print('Relatório Final')
i = 1
for veiculo, autonomia in zip(veiculos, autonomias):
    print(f' {i} - {veiculo}\t\t-\t{autonomia:.1f} - {1000/autonomia:.1f} - R$ {1000/autonomia* 2.25:.2f}')
    
maior = max(autonomias)
i = autonomias.index(maior)
print('O menor consumo é do', veiculos[i])