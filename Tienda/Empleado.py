from Persona import *

class Empleado(Persona): #Empleado es una subclase de Persona

    def __init__(self):
        super().__init__() #Llamado al contructor de la clase super
        self.__sueldo_bruto = float(input("Ingrese sueldo: "))
        self.__salud = input("Ingrese sistema salud: ")
        self.__afp = input("Ingrese sistema de afp: ")

    def mostrar(self):
        super().mostrar()
        print(f'Sueldo Bruto: {self.__sueldo_bruto}')
        print(f'Salud: {self.__salud}')
        print(f'Afp: {self.__afp}')
        self.calcular_salario_neto()

    def calcular_salario_neto(self):
        if self.__salud == 'fonasa':
            descuento_salud = self.__sueldo_bruto * 0.07 
        else:
            descuento_salud = self.__sueldo_bruto * 0.08

        if self.__afp == "afp1":
            descuento_afp = self.__sueldo_bruto * 0.10
        else:
            descuento_afp = self.__sueldo_bruto * 0.11

        sueldo_liquido = self.__sueldo_bruto - descuento_salud - descuento_afp
        print(f'Sueldo Liquido: {sueldo_liquido}')

    