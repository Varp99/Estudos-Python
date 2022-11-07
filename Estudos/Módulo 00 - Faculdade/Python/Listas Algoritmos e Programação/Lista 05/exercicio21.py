# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com
# a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é
# testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um
# deles, para verificar o que se pode aproveitar deles.

situacoes = [0, 0, 0, 0]

while True:
    identificacao = int(input('Identificação: '))
    if identificacao == 0:
        break
    situacao = int(input('Situação: '))
    situacoes[situacao - 1] += 1
total = sum(situacoes)
print('Quantidade de mouses:', total)
print('Situação\t\t\t\tQuantidade\t\t\tPercentual')

print(f'1- necessita da esfera\t\t\t\t{situacoes[0]}\t\t\t{situacoes[0]/total:.0%}')
print(f'2- necessita de limpeza\t\t\t\t{situacoes[1]}\t\t\t{situacoes[1]/total:.0%}')
print(f'3- necessita troca do cabo ou conector\t\t{situacoes[2]}\t\t\t{situacoes[2]/total:.0%}')
print(f'4- quebrado ou inutilizado\t\t\t{situacoes[3]}\t\t\t{situacoes[3]/total:.0%}')
# print('Foram processados', qtde, 'colaboradores')
# print(f'Total gasto com abonos: R$ {total:.2f}')
# print('Valor mínimo pago a', conta_minimo, 'colaboradores')
# print(f'Maior valor de abono pago: R$ {maximo:.2f}')