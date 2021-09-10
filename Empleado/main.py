from Empleado import *
e1 = Empleado()
e2 = Empleado()
e1.mostrar()
e2.mostrar()
e1.impuestos()
e2.impuestos()

#A esto queremos llegar
empleados = []
for i in range(4):
    e = Empleado() #Crear un nuevo objeto
    empleados.append(e) #Agregar ese objeto a la lista

for x in empleados:
    x.mostrar()