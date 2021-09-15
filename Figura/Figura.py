class Figura:
    def __init__(self,lados=0,longitud=0.0,apotema=0.0):
        self.lados = lados
        self.long = longitud
        self.__apotema = apotema
        self.__perimetro = self.lados * self.long 

    def __area(self):
        resultado = (self.__apotema*self.__perimetro)/2
        return resultado #Retorna el resultado -> Calculo del area

    def mostrar(self):
        print(f'Lado: {self.lados}')
        print(f'Longitud: {self.long}')
        print(f'Apotema: {self.__apotema}')
        print(f'Perimetro: {self.__perimetro}')
        print(f'Area: {self.__area()}') #Del objeto llama el meto area