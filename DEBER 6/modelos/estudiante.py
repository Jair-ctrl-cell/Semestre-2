# Clase derivada Estudiante
# Hereda de Persona y sobrescribe un método (polimorfismo)

from modelos.persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.carrera = carrera

    # Polimorfismo: sobrescritura del método presentarse
    def presentarse(self):
        return f"Soy el estudiante {self.get_nombre()}, tengo {self.get_edad()} años y estudio {self.carrera}."
