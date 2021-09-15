from Vehiculo import *

class Moto(Vehiculo):

    def __init__(self):
        super().__init__("Moto")

    def num_ruedas(self):
        print("Tengo 2 ruedas")