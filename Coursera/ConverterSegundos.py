#Converter uma quantidade de segundos

segundos = int(input("Insira a quantidade de segundos que queira converter: "))

horas = segundos // 3600
segs_restantes = segundos % 3600
minutos = segs_restantes // 60
segs_rest_final = segs_restantes % 60

print("{} horas, {} minutos, {} segundos".format(horas, minutos, segs_rest_final))