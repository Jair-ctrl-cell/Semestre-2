class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def sonido(self):
        return "Guau!"

class Gato(Animal):
    def sonido(self):
        return "Miau!"

perro = Perro("Firulais")
gato = Gato("Michi")

print(perro.nombre, "dice:", perro.sonido())
print(gato.nombre, "dice:", gato.sonido())
