#Faça um algoritmo que receba um valor que é um valor pago, um segundo valor que é o preço do produto e retorne o troco a seu dado

#Entradas
valor_pago = float(input("Digite o valor pago: "))
preco_produto = float(input("Digite o preço do produto: "))
#Conta para saber o troco
troco = valor_pago - preco_produto
if (troco > 0):
    print("O seu troco é: %.2f"% troco)
else:
    print("Não há troco")