# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
# velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de
# download do arquivo usando este link (em minutos)

tam_arquiv = float(input("Digite o tamanho do arquivo para download em MB: "))
velocidade = float(input("Digite a velocidade da sua internet em MBPS: "))

segundos = tam_arquiv/velocidade
minutos = int(segundos/60)
segundos = segundos%60

print("Tempo aproximado para download: " + str(minutos) + " minutos e " + str(segundos) + " segundos")