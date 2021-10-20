class Persona:

    def __init__(self):
        self.__fullname = input("Ingrese nombre: ")
        self.__profession = input("Ingrese profesion: ")
        self.__birth = input("Ingrese fecha de nacimiento: (Año-Mes-Dia) ")
        self.__genre = input("Ingrese su genero: (M/F) ").upper()
        self.__bodyweight = float(input("Ingrese peso: "))
        self.__height = float(input("Ingrese altura: "))
        self.__nationality = input("Ingrese nacionalidad: ")

    def get_fullname(self):
        return self.__fullname

    def get_profession(self):
        return self.__profession

    def get_birth(self):
        return self.__birth

    def get_genre(self):
        return self.__genre

    def get_bodyweight(self):
        return self.__bodyweight

    def get_height(self):
        return self.__height

    def get_nationality(self):
        return self.__nationality