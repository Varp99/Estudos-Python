#Calcula a distancia entre dois pontos num plano cartesiano.

from math import sqrt

xa = int(input("Insira o valor de XA: "))
xb = int(input("Insira o valor de XB: "))
ya = int(input("Insira o valor de YA: "))
yb = int(input("Insira o valor de YB: "))

dist_AB = sqrt(((xb - xa)**2) + ((yb - ya)**2))

print(int(dist_AB))