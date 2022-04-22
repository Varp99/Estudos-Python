#Desenvolva um algoritmo que efetua a soma de todos os números ímpares que são multiplos de tres e que se encontram no conjunto dos números de 1 até 500 

soma = 0
contador = 0

for num in range(0,501):
    #Calcula os numeros impares usando o resto da divisão
    if(num%2 == 1):
        #Calcula quais numeros impares são multiplos de 3
        if(num%3 == 0):
            soma += num
            contador += 1
            print(num)
print("A soma de todos os {} valores é {}".format(contador,soma))