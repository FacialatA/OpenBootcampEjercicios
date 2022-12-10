import time

fecha = (time.ctime())
lista_fecha = (fecha.split(" "))
hora_con_puntos = lista_fecha[4]
lista_horaconpuntos = hora_con_puntos.split(":")

if int(lista_horaconpuntos[0]) == 19:
    print("Es hora de ir a casa.")
else:
    print("Son las " + hora_con_puntos)
    print("Quedan " + str(19-int(lista_horaconpuntos[0])) + " horas de trabajo.")
