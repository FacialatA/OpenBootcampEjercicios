f = open("archivodetexto.txt", "w")
f.write("Esta es la primer linea de texto.\n")
f.write("Esta es mi segunda linea de texto.\n")
f.close

f = open("archivodetexto.txt", "r+")
f.readline()
f.write("Escribiendo por segunda vez en el fichero.")

f.seek(0)
print(f.read())
f.close()