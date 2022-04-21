#Indicar a menor quantidade de moedas que representa esse valor
valor = int(input("Digite um valor em centavos: "))

while valor > 0:
    if valor > 0:  
        moedas = int(valor / 100) 
        if moedas > 0:
            print(moedas, "moedas de 1 real")
            valor = valor - (moedas * 100)
        moedas = int(valor / 50) 
        if moedas > 0:
            print(moedas, "moedas de 50 centavos")
            valor = valor - (moedas * 50)
        moedas = int(valor / 25) 
        if moedas > 0:
            print(moedas, "moedas de 25 centavos")
            valor = valor - (moedas * 25)  
        moedas = int(valor / 10)
        if moedas > 0:
            print(moedas, "moedas de 10 centavos")
            valor = valor - (moedas * 10)
        moedas = int(valor / 5)
        if moedas > 0:
            print(moedas, "moedas de 5 centavos")
            valor = valor - (moedas * 5)
        if valor > 0:
            print(valor, "moedas de 1 centavo")
    else:
        print("Nenhuma moeda é necessária")


