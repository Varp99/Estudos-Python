# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande
# quantidade de organizações:

lista = [0, 0, 0, 0, 0, 0]
sos = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
while True:
    numero = int(input('Número do servidor (0=fim): '))
    if numero == 0:
        break
    lista[numero - 1] += 1
total = sum(lista)
print('Sistema Operacional\tVotos\t%')
print('-------------------\t-----\t---')
for voto, so in zip(lista, sos):
    if so == 'Windows Server':
        print(f'{so}\t\t{voto}\t{voto/total:.0%}')
    else:
        print(f'{so}\t\t\t{voto}\t{voto/total:.0%}')

melhor = max(lista)
i = lista.index(melhor)
porcentagem = melhor/total

print(f'O Sistema Operacional mais votado foi o {sos[i]}, com {melhor} votos, correspondendo a {porcentagem:.0%} dos votos.')