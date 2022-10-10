#Imprime a quantidade de números pares de 100 até 200, incluindo-os.
num = 100
contador_pares = 0

while num <= 200:
    if num % 2 == 0:
        contador_pares = contador_pares + 1
    num = num + 1
print(contador_pares)
