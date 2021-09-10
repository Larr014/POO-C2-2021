from Auto import *

a1 = Auto("rojo",5) #Uso el constructor para crear el objeto
print(a1.color)
print(a1.aceleracion)
a2 = Auto("azul",10)
print(a2.color)
print(a2.aceleracion)
a1.acelerar()
print(f'Auto1 Velocidad: {a1.velocidad}')
a1.acelerar()
print(f'Auto1 Velocidad: {a1.velocidad}')
for x in range(0,4):
    a2.acelerar()
print(f'Auto2 Velocidad: {a2.velocidad}')
a2.frenar()
a2.frenar()
print(f'Auto2 Velocidad: {a2.velocidad}')
a2.frenar()
a2.frenar()
a2.frenar()
print(f'Auto2 Velocidad: {a2.velocidad}')
print(f'Auto2: color: {a2.color}')
a2.color = "morado"
print(f'Auto2: color: {a2.color}')
print(f'Auto1: color: {a1.color}')

print(Auto.ruedas)
print(a1.ruedas)
print(a2.ruedas)
a1.ruedas = 3
print(Auto.ruedas)
print(a1.ruedas)
print(a2.ruedas)
a3 = Auto("Verde",20)
print(a3.ruedas)