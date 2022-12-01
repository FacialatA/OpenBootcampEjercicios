def esBisiesto():
    print("Es bisiesto?")
    año = int(input("Ingrese el año de su consulta: "))
    if int(año) % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
       print("El año es bisiesto.")
    else:
       print("El año no es bisiesto.")
       
esBisiesto()