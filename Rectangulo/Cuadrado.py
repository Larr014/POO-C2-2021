from Rectangulo import *
class Cuadrado(Rectangulo): #Cuadrado hereda de Rectangulo

    def __init__(self,lado):
        super().__init__(lado,lado) #Cuadrado es un Rectangulo, por ende uso su constructor

