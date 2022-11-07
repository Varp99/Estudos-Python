# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
# perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
# participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
# classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário,
# ele será classificado como "Inocente".

perguntas = [
    "Telefonou para a vítima? (S/N) ",
    "Esteve no local do crime? (S/N) ",
    "Mora perto da vítima? (S/N) ",
    "Devia para a vítima? (S/N) ",
    "Já trabalhou com a vítima? (S/N) "
]

contador = 0
for pergunta in perguntas:
    resposta = input(pergunta)
    if resposta == 'S':
        contador += 1
        
if contador == 5:
    print("Assassino")
elif contador == 3 or contador == 4:
    print("Cúmplice")
elif contador == 2:
    print( "Suspeita")
else:
    print("Inocente")
