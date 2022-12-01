class Vehiculo:
    color = None
    ruedas = None
    puertas = None

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = None
    
    def __init__(self,  color, ruedas, puertas, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.cilindrada = cilindrada
    
Coche1 = Coche("Rojo", 4, 2, 8000)
print(Coche1)