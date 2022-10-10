# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar 0-matutino ou 1-Vespertino ou 2-Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = int (input("Em que turno vc estuda? 0 - matutino / 1 - vespertino / 2- noturno: "))

if turno == 0:
    print("Bom dia!")
elif turno == 1:
    print("Boa tarde!")
elif turno == 2:
    print("Boa noite!")
else:
    print("Valor inválido")
