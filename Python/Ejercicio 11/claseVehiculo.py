class Vehiculo:
    color = None
    ruedas = None
    puertas = None
    
    def __init__(self,  color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        
FordKa = Vehiculo("Azul claro", 4, 2)

import pickle as p

f = open("ObjetoFordKa.bin", "w")
p.dump(FordKa, f)
f.close()

