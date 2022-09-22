#Faça um programa que leia dois vetores de 3 posições, que representam forças sobre um ponto no espaço 3D, e escreva a força resultante.
#Dica: força resultante é obtida pela soma dos valores das coordenadas correspondentes nos dois vetores (x1 + x2),(y1 + y2), (z1 + z2)

vetor_x = []
vetor_y = []

for i in range(3):
    vetor_x.append(int(input("Digite a posição %d do vetor x: " %(i+1))))

for i in range(3):
    vetor_y.append(int(input("Digite a posição %d do vetor y: " %(i+1))))

forcresult = [vetor_x[0]+vetor_y[0], vetor_x[1]+vetor_y[1], vetor_x[2]+vetor_y[1]]
print("\nForça resultante: ", forcresult)