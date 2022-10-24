# Criar um algoritmo que imprima os 10 primeiros termos da série de Fibonacci.
# Observação: os dois primeiros termos desta série são 1 e 1 e os demais são gerados a partir da soma dos anteriores.
# Exemplos:
# 1 + 1 -> 2 terceiro termo;
# m 1 + 2-> 3 quarto termo etc.

termoAnterior = 0
termo = 1

for i in range (1, 10):
    print(termo)
    temp = termo
    termo = termoAnterior + termo
    termoAnterior = temp