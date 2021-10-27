from Persona import *
import crud

def registrar_persona():
    fullname = input("Ingrese nombre: ")
    profession = input("Ingrese profesion: ")
    birth = input("Ingrese fecha de nacimiento: (Año-Mes-Dia) ")
    genre = input("Ingrese su genero: (M/F) ").upper()
    bodyweight = float(input("Ingrese peso: "))
    height = float(input("Ingrese altura: "))
    nationality = input("Ingrese nacionalidad: ")
    p = Persona(fullname,profession,birth,genre,bodyweight,height,nationality)
    crud.registrar_persona(p)

def buscar_persona():
    id = input("Ingrese id de la persona: ")
    p = crud.buscar_persona(id)
    return p

def modificar_persona():
    p = buscar_persona()
    if p != None:
        opcion = input("Desea modificar el nombre: s/n ")
        if opcion.lower() == 's':
            nombre = input("Ingrese nombre: ")
            p.set_fullname(nombre)
        opcion = input("Desea modificar profesion: s/n ")
        if opcion.lower() == 's':
            profesion = input("Ingrese profesion: ")
            p.set_profession(profesion)
        opcion = input("Desea modificar fecha nacimiento: s/n ")
        if opcion.lower() == 's':
            fecha = input("Ingrese fecha de nacimiento: (Año-Mes-Dia) ")
            p.set_birth(fecha)
        opcion = input("Desea modificar genero: s/n ")
        if opcion.lower() == 's':
            genero = input("Ingrese su genero: (M/F) ").upper()
            p.set_genre(genero)
        opcion = input("Desea modificar peso: s/n ")
        if opcion.lower() == 's':
            peso = float(input("Ingrese peso: "))
            p.set_bodyweight(peso)
        opcion = input("Desea modificar altura: s/n ")
        if opcion.lower() == 's':
            altura = float(input("Ingrese altura: "))
            p.set_height(altura)
        opcion = input("Desea modificar nacionalidad: s/n ")
        if opcion.lower() == 's':
            nacionalidad = input("Ingrese nacionalidad: ")
            p.set_nationality(nacionalidad)
        crud.modificar_persona(p)


def eliminar_persona():
    p = buscar_persona()
    if p!=None:
        opcion = input("Desea eliminar a esta persona: s/n ")
        if opcion.lower() == 's':
            crud.eliminar_persona(p)

def mostrar_personas():
    crud.mostrar_personas()

while True:
    print("1.- Registrar Persona")
    print("2.- Buscar Persona")
    print("3.- Modificar Persona")
    print("4.- Eliminar Persona")
    print("5.- Mostrar Personas")
    opcion = input("Ingrese una opcion: ")
    if opcion == '1':
        registrar_persona()
    elif opcion=='2':
        buscar_persona()
    elif opcion=='3':
        modificar_persona()
    elif opcion=='4':
        eliminar_persona()
    elif opcion=='5':
        mostrar_personas()
    else:
        print("Opcion incorrecta")