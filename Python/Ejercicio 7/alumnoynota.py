class alumno(): 
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def imprimirNombre(self):
        print("Nombre: " + nombre)
        
    def imprimirNota(self):
        print("Nota: " + nota)

    def resumen(self):
            if self.nota >= 7:
                print("Alumno aprobo")
            else:
                print("Alumno desaprobo")
        




Jose = alumno("Jose", 7)
print(Jose)
print(Jose.nota)
print(Jose.resumen)