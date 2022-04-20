print("*******************")
print("Jogo de adivinhação")
print("*******************")

#Definição do número a ser adivinhado
numero_secreto = 42
#Definição da quantidade de tentativas
tentativas = 3
#Controle de rodada
rodada = 1

#Enquanto rodada for menor ou igual a tentativas executa o código
while (rodada <= tentativas):
    #Acompanhar em qual tentativa está / print("Tentativa",rodada,"de",tentativas)
    #Melhor maneira
    print("Tentativa {} de {}".format(rodada, tentativas))
    #Pedir para a pessoa digitar um número
    chute_str = input("Digite o seu número:")
    print("Você digitou", chute_str)

    #Transformar a string em int
    chute = int(chute_str)
    #Variaveis de condição
    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    #Condições para verificar se o número foi adivinhado ou não47
    if(acertou):
        print("Você acertou")
        print("Fim do jogo")
    else:
        if(chute_maior):
            print("Você errou! O chute foi maior do que o número secreto!")
            print("Continue")
        elif(chute_menor):
            print("Você errou! O chute foi menor do que o número secreto!")
            print("Continue")
    #Isso daqui faz com que aumente a rodada até chegar em 3
    rodada = rodada + 1
    
print("Fim do Jogo")
    