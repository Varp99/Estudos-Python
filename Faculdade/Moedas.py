#Indicar a menor quantidade de moedas que representa esse valor
valor = int(input("Digite um valor em centavos: "))

while valor > 0:
    if valor > 0:  
        Nmoedas = int(valor / 100) 
        if Nmoedas > 0:
            print(Nmoedas, "moedas de 1 real")
            valor = valor - (Nmoedas * 100)
        Nmoedas = int(valor / 50) 
        if Nmoedas > 0:
            print(Nmoedas, "moedas de 50 centavos")
            valor = valor - (Nmoedas * 50)
        Nmoedas = int(valor / 25) 
        if Nmoedas > 0:
            print(Nmoedas, "moedas de 25 centavos")
            valor = valor - (Nmoedas * 25)  
        Nmoedas = int(valor / 10)
        if Nmoedas > 0:
            print(Nmoedas, "moedas de 10 centavos")
            valor = valor - (Nmoedas * 10)
        Nmoedas = int(valor / 5)
        if Nmoedas > 0:
            print(Nmoedas, "moedas de 5 centavos")
            valor = valor - (Nmoedas * 5)
        if valor > 0:
            print(valor, "moedas de 1 centavo")
    else:
        print("Nenhuma moeda é necessária")


