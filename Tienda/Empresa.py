from Empleado import Empleado


class Empresa:

    
    def __init__(self):
        self.__id = input("Ingrese codigo empresa: ")
        self.__nombre = input("Ingrese nombre de la empresa: ")
        self.__clientes = [] #Lista de clientes vacia
        self.__empleados = []

    def mostrar(self):
        print(f'Codigo: {self.__id}')
        print(f'Empresa: {self.__nombre}')

    #Un get te permite recuperar un atributo privado en otra clase
    def get_id(self):
        return self.__id


    def agregar_cliente(self,cliente):
        self.__clientes.append(cliente) #Vamos a agregar el cliente que viene del main a la lista de clientes de la empresa

    def mostrar_clientes(self):
        for cliente in self.__clientes:
            cliente.mostrar()

    def eliminar_cliente(self):
         self.mostrar_clientes()
         rut = input("Ingrese rut del cliente a eliminar: ")
         for cliente in self.__clientes:
             if cliente.get_rut() == rut:
                 self.__clientes.remove(cliente)
         
    def agregar_empleado(self):
        e = Empleado()
        self.__empleados.append(e)

    def mostrar_empleados(self):
        for empleado in self.__empleados:
            empleado.mostrar()

    def eliminar_empleado(self):
        self.mostrar_empleados()
        rut = input("Ingrese rut del empleado a eliminar: ")
        for empleado in self.__empleados:
            if empleado.get_rut() == rut:
                self.__empleados.remove(empleado)

         