vetor = []
contador = 0

for i in range(10):
   pos = int(input("Digite uma posição: "))
   vetor.append(pos)
   i+=1   

for i in range(len(vetor)):
      for j in range(len(vetor)):
          if i != j:
              contador = contador + 1
              break
              
print("A quantidade de numeros diferentes é: ", contador)