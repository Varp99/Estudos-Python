#Calcula o Perímetro e a Área de um quadrado

lado_do_quadrado = int(input("Digite o valor correspondente ao lado de um quadrado: "))

#O Perimetro de um quadrado é o Lado * 4
perimetro = lado_do_quadrado * 4
#Área de um quadrado é o Lado ao quadrado.
area = lado_do_quadrado ** 2

print("Perímetro:", perimetro, "Área:", area)