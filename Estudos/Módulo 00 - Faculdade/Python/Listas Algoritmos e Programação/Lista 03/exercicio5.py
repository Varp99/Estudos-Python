# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

popA=float(input("informe a população da cidade A: "))
popB=float(input("informe a população da cidade B: "))

anos=0

crescA=float(input("informe a taxa de crescimento da população da cidade A: "))
crescB=float(input("informe a taxa de crescimento da população da cidade B: "))

while popA < popB:
	popA+=round((popA*crescA)/100)
	popB+=round((popB*crescB)/100)
	anos+=1

print("levará",anos,"anos para população de A ser maior que a de B")
print("população B -->",popB,"habitantes")
print("população A -->", popA,"habitantes")
