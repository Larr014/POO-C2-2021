from Rectangulo import *

class Triangulo(Rectangulo):

    def __init__(self,lado1,lado2,lado3):
        super().__init__(lado1,lado2)
        self.__lado3 = lado3

    def area(self):
        resultado = super().area() #De la clase super, llama al metodo area
        resultado = resultado / 2 #Base x altura / 2
        return resultado

    def perimetro(self):
        resultado = super().get_base() + super().get_altura() + self.__lado3
        return resultado
