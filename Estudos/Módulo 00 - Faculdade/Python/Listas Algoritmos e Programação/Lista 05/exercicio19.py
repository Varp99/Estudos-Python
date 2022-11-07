# As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento
# ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a
# aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
# Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do
# sindicato laboral, chegou-se a seguinte forma de cálculo:

lista = []
abonos = []
while True:
    salario = int(input('Salário: '))
    if salario == 0:
        break
    if salario < 500:
        lista.append(salario)
        abonos.append(100)
    else:
        lista.append(salario)
        abonos.append(salario*0.2)
        
qtde = len(lista)
total = sum(abonos)
conta_minimo = 0
maximo = max(abonos)
print('Salario\t\tAbono')

for salario, abono in zip(lista, abonos):
    print(f'R$ {salario:.2f}\tR$ {abono:.2f}')
for item in abonos:
    if item == 100:
        conta_minimo += 1

print('Foram processados', qtde, 'colaboradores')
print(f'Total gasto com abonos: R$ {total:.2f}')
print('Valor mínimo pago a', conta_minimo, 'colaboradores')
print(f'Maior valor de abono pago: R$ {maximo:.2f}')