# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores...

votos = []
print('Enquete: Quem foi o melhor jogador?')
for _ in range(23):
    votos.append(0)

while True:
    numero = int(input('Número do jogador (0=fim): '))
    if numero == 0:
        break
    elif not 1 <= numero <= 23:
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
        continue
    votos[numero - 1] += 1

total = sum(votos)
print('Foram computados', total, 'votos.')
print('Jogador\tVotos\t%')
for i, voto in enumerate(votos):
    if voto > 0:
        print(f'{i+1}\t{voto}\t{voto/total:.1%}')

melhor = max(votos)
i = votos.index(melhor)
porcentagem = melhor/total
print(f'O melhor jogador foi o número {i+1}, com {melhor} votos, correspondendo a {porcentagem:.0%} do total de votos.')