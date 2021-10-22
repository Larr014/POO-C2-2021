import mysql.connector
from Persona import *


credenciales = {
    'host':'localhost',
    'user':'root',
    'password':'',
    'database':'bdC2'
}

conexion = mysql.connector.connect(**credenciales)
cursor = conexion.cursor()

def registrar_persona(p):
    query = "INSERT INTO people (fullname,profession,birth,genre,bodyweight,height,nationality) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (p.get_fullname(),p.get_profession(),p.get_birth(),p.get_genre(),p.get_bodyweight(),p.get_height(),p.get_nationality())
    cursor.execute(query,values)
    #Despues de ejecutar un cambio en la base de datos se debe hacer un commit(Aplicar cambios)
    conexion.commit()

def mostrar_personas():
    query = "SELECT * FROM people"
    cursor.execute(query)
    #Despues de ejecutar un select se debe recuperar los resultados
    resultados = cursor.fetchall()
    print("---------Resultados----------")
    for fila in resultados:
        print(f'{fila[0]} {fila[1]}')

def buscar_persona(id):
    query = "SELECT * FROM people WHERE id=%s"
    values = (id,)
    cursor.execute(query,values)
    #Despues de un execute en un select se deben recuperar los resultados
    resultado = cursor.fetchone()
    print(resultado)
    p = Persona(resultado[1],resultado[2],resultado[3],resultado[4],resultado[5],resultado[6],resultado[7],resultado[0])
    return p

def modificar_persona(p):
    #Completar los campos que se quieren actualizar
    query = "UPDATE people SET fullname = %s,profession = %s WHERE id = %s"