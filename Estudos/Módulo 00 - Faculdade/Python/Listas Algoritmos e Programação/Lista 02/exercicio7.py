# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

prec1 = float(input("Digite o primeiro preço: "))
prec2 = float(input("Digite o segundo preço: "))
prec3 = float(input("Digite o terceiro preço: "))

if prec1 < prec2 and prec1 < prec3:
    print("Este é o produto que vc deve comprar: ", prec1)
elif prec2 < prec1 and prec2 < prec3:
    print("Este é o produto que vc deve comprar: ", prec2)
else:
    print("Este é o produto que vc deve comprar: ", prec3)