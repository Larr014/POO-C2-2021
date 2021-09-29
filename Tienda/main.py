from Empresa import *
from Cliente import *

empresas = []
clientes = []

#Mostrar las empresas
def mostrar_empresas():
    for empresa in empresas:
        empresa.mostrar()
#Agregar una empresa
def agregar_empresa():
    e = Empresa() #Llamo al constructor y creo una empresa
    empresas.append(e)
#Eliminar una empresa
def eliminar_empresa():
    mostrar_empresas() #Mostramos las empresas
    id = input("Ingrese codigo de empresa a eliminar: ") #Solicitamos el id de la empresa a eliminar
    for empresa in empresas: #Recorremos la lista de empresas
        if empresa.get_id() == id: #Comparamos cada id de cada empresa con el id ingresado por el usuario
            empresas.remove(empresa) #Eliminar de la lista la empresa que tenga ese id

def agregar_cliente():
    c = Cliente() #Cree un cliente
    clientes.append(c) #Agrego a la lista el cliente creado

def mostrar_clientes():
    for cliente in clientes:
        cliente.mostrar()

def eliminar_cliente():
    mostrar_clientes()
    rut = input("Ingrese rut del cliente a eliminar: ")
    for cliente in clientes:
        if cliente.get_rut() == rut:
            clientes.remove(cliente)
            break

def agregar_cliente_empresa():
    mostrar_empresas()
    id = input("Ingrese codigo de empresa: ") #Solicitamos el id de la empresa
    for empresa in empresas:
        if empresa.get_id() == id:
            mostrar_clientes()
            rut = input("Ingrese rut del cliente: ")
            for cliente in clientes:
                if cliente.get_rut()==rut:
                    empresa.agregar_cliente(cliente) #La empresa que buscas va a agregar el cliente que buscas
                    break

def mostrar_clientes_empresa():
    mostrar_empresas()
    id = input("Ingrese codigo de empresa: ") #Solicitamos el id de la empresa
    for empresa in empresas:
        if empresa.get_id() == id:
            empresa.mostrar_clientes() #Llama a la funcion mostrar clientes de cada empresa
            break

def eliminar_cliente_empresa():
    mostrar_empresas()
    id = input("Ingrese codigo de empresa: ") #Solicitamos el id de la empresa
    for empresa in empresas:
        if empresa.get_id() == id:
            empresa.eliminar_cliente() #Llama a la funcion mostrar clientes de cada empresa
            break


def agregar_empleado_empresa():
    mostrar_empresas()
    id = input("Ingrese codigo de empresa: ") #Solicitamos el id de la empresa
    for empresa in empresas:
        if empresa.get_id() == id:
            empresa.agregar_empleado()
            break

def mostrar_empleados_empresa():
    mostrar_empresas()
    id = input("Ingrese codigo de empresa: ") #Solicitamos el id de la empresa
    for empresa in empresas:
        if empresa.get_id() == id:
            empresa.mostrar_empleados()
            break

def eliminar_empleado_empresa():
    mostrar_empresas()
    id = input("Ingrese codigo de empresa: ") #Solicitamos el id de la empresa
    for empresa in empresas:
        if empresa.get_id() == id:
            empresa.eliminar_empleado() #Llama a la funcion mostrar clientes de cada empresa
            break


while True:
    print('1.- Agregar Empresa')
    print('2.- Eliminar Empresa')
    print('3.- Mostrar Empresas')
    print('4.- Agregar Cliente')
    print('5.- Eliminar Cliente')
    print('6.- Mostrar Clientes')
    print('7.- Agregar Cliente x Empresa')
    print('8.- Eliminar Cliente x Empresa')
    print('9.- Mostrar Clientes x Empresa')
    print('10.- Agregar Empleado x Empresa')
    print('11.- Eliminar Empleado x Empresa')
    print('12.- Mostrar Empleado x Empresa')
    opcion = input("Ingrese una opcion: ")
    if opcion == '1':
        agregar_empresa()
    elif opcion == '2':
        eliminar_empresa()
    elif opcion == '3':
        mostrar_empresas()
    elif opcion == '4':
        agregar_cliente()
    elif opcion == '5':
        eliminar_cliente()
    elif opcion == '6':
        mostrar_clientes()
    elif opcion == '7':
        agregar_cliente_empresa()
    elif opcion == '8':
        eliminar_cliente_empresa()
    elif opcion == '9':
        mostrar_clientes_empresa()
    elif opcion == '10':
        agregar_empleado_empresa()
    elif opcion == '11':
        eliminar_empleado_empresa()
    elif opcion == '12':
        mostrar_empleado_empresa()
    else:
        print('La opcion ingresada no es valida')