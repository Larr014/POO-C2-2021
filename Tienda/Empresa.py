class Empresa:

    
    def __init__(self):
        self.__id = input("Ingrese codigo empresa: ")
        self.__nombre = input("Ingrese nombre de la empresa: ")
        
        

    def mostrar(self):
        print(f'Codigo: {self.__id}')
        print(f'Empresa: {self.__nombre}')

    #Un get te permite recuperar un atributo privado en otra clase
    def get_id(self):
        return self.__id