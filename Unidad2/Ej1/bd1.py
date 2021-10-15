import mysql.connector #Que vamos a usar mysql

credenciales = {
    'host':'localhost',
    'user':'root',
    'password':'',
    'database':'bdC2'
}

#Establecer conexion con esas credenciales
conexion = mysql.connector.connect(**credenciales)

#Cuando quiero recuperar datos de una tabla, necesito un cursor
#Cursor: Puente con la base de datos, recupera y almacena los resultados de la query
cursor = conexion.cursor()

#Crear una query
query = "SELECT * FROM people where genre='F' AND nationality='Brasil'" #Busca todo lo que tiene la tabla people

#Indicar al cursos que ejecute esa query
cursor.execute(query)

#Retornar el resultado
resultados = cursor.fetchall()

print(resultados)
print()

for tupla in resultados:
    print(tupla)

print()

for tupla in resultados:
    print(f'{tupla[0]} {tupla[1]} {tupla[7]}')