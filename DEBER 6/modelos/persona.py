# Clase base Persona
# Aplica encapsulación usando atributos privados

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre      # Atributo privado (encapsulación)
        self.__edad = edad

    # Métodos getter (acceso controlado)
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Método que será sobrescrito (polimorfismo)
    def presentarse(self):
        return f"Hola, soy {self.__nombre} y tengo {self.__edad} años."
