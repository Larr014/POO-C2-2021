from Empresa import *

empresas = []


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




while True:
    print('1.- Agregar Empresa')
    print('2.- Eliminar Empresa')
    print('3.- Mostrar Empresas')
    opcion = input("Ingrese una opcion: ")
    if opcion == '1':
        agregar_empresa()
    elif opcion == '2':
        eliminar_empresa()
    elif opcion == '3':
        mostrar_empresas()
    else:
        print('La opcion ingresada no es valida')