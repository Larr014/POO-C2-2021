import mysql.connector as msql
from Post import *

credenciales = {
    'host':'localhost',
    'user':'root',
    'password':'',
    'database':'c2RedSocial'
}

conexion = msql.connect(**credenciales)
cursor = conexion.cursor()

def registrar_post(p):
    query = 'INSERT INTO post (userId,id,title,body) VALUES (%s,%s,%s,%s)'
    values = (p.get_userId(),p.get_id(),p.get_title(),p.get_body())
    cursor.execute(query,values)
    conexion.commit()
    print("Registro exitoso!")
    
def mostrar_posts():
    query = "SELECT * FROM post"
    cursor.execute(query)
    resultados = cursor.fetchall()
    l = []
    for fila in resultados:
        p = Post(fila[0],fila[1],fila[2],fila[3])
        l.append(p)
    return l