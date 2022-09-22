letra = str("AATCTGCAC")
#Caso fosse pedir pro usuário digitar o código está abaixo comentado.
#letra = str(input('Digite uma fita de DNA:'))
res = str("")

for x in letra:

  if(x == "A"):
      res = res + "T"
  if(x == "T"):
      res = res + "A"
  if(x == "C"):
      res = res + "G"
  if(x == "G"):
      res = res + "C"

print("A cadeia de dna é: {} e a sua cadeia complementar é: {}".format(letra, res))

