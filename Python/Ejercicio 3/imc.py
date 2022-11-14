peso = input("Ingrese su peso en kilogramos:")
altura = input("Ingrese su altura en metros: ")
alturacuadrada = float(altura) ** 2
imc = float(peso) / alturacuadrada
print("Su indice de masa corporal es: " + str(imc))