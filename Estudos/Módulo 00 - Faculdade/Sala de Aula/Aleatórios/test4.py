fita1 = []
fita2 = []

letra = input('Digite uma fita:')
fita1.append(letra)

for x in fita1:
    if x == 'A':
        fita2.append('T')
    elif x == 'T':
        fita2.append('A')
    elif x == 'C':
        fita2.append('G')
    elif x == 'G':
        fita2.append('C')
print(fita1)
print(fita2)