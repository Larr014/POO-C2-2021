from Cuadrado import Cuadrado
from Rectangulo import *
from Triangulo import *

r1 = Rectangulo(4,5)
print(r1.area())
print(r1.perimetro())
r1.imprimir()

c1 = Cuadrado(4)
print(c1.area())
print(c1.perimetro())
c1.imprimir()

t1 = Triangulo(3,4,5)
print(t1.area())
print(t1.perimetro())
t1.imprimir()