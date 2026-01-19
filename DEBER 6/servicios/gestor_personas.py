# Clase de servicio que maneja objetos Persona y Estudiante

class GestorPersonas:
    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def mostrar_presentaciones(self):
        # Demostración de polimorfismo
        for persona in self.personas:
            print(persona.presentarse())
