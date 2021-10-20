import mysql.connector

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
