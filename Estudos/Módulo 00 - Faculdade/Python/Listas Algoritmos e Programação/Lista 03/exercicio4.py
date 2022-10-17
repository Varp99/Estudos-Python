# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual
# de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do
# país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

anos = 0

paisA = 80000
crescA = 0.03
popA = paisA * crescA

print("Quantidade de habitantes por ano no país A: ", popA)

paisB = 200000
crescB = 0.015
popB = paisB * crescB

print("Quantidade de habitantes por ano no país B: ", popB)

while paisA <= paisB:
	paisA += paisA * 0.03
	paisB += paisB * 0.015
	anos += 1

print("O número de anos seria: ", anos)