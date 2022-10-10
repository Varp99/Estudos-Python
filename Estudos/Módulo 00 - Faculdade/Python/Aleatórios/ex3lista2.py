#Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição a posição em que o valor x
#lido do teclado está no vetor. Caso o valor x não seja encontrado, o programa deve imprimir -1

vetor = []
i = 0

while i < 5:
   pos = int(input("Digite uma posição: "))
   vetor.append(pos)
   i+=1

i = 0

encontrarValor = int(input("Encontre a posição de um valor dentro do vetor: "))
valorEncontrado = False

while i < 5:
   if encontrarValor == vetor[i]:
       print("O valor ", encontrarValor, " está na posição: ", i, " do vetor")
       valorEncontrado = True
   i+=1    

if valorEncontrado == False:
   print("-1")