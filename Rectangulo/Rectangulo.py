class Rectangulo:

    def __init__(self,base,altura):
        self.__base = base
        self.__altura = altura

    def area(self):
        resultado = self.__base*self.__altura
        return resultado

    def perimetro(self):
        resultado = self.__base*2+self.__altura*2
        return resultado

    def imprimir(self):
        print(f'Base: {self.__base}')
        print(f'Altura: {self.__altura}')

    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura