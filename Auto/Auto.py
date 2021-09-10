class Auto:

    ruedas = 4
    #Constructor de la clase
    def __init__(self,color,aceleracion):
        self.color = color #Crear el atributo color y asignarle un color
        self.aceleracion = aceleracion  #Crear el atributo aceleracion y asignarle una aceleracion
        self.velocidad = 0
    

    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion
        
    def frenar(self):
        v = self.velocidad - self.aceleracion
        if v<0:
            v = 0
        self.velocidad = v

    