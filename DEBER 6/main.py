# Archivo principal de ejecución

from modelos.persona import Persona
from modelos.estudiante import Estudiante
from servicios.gestor_personas import GestorPersonas

def main():
    # Crear instancias de las clases
    persona1 = Persona("Carlos", 40)
    estudiante1 = Estudiante("Jair", 20, "Ingeniería en Sistemas")

    # Crear gestor
    gestor = GestorPersonas()

    # Agregar objetos
    gestor.agregar_persona(persona1)
    gestor.agregar_persona(estudiante1)

    # Mostrar resultados
    gestor.mostrar_presentaciones()

if __name__ == "__main__":
    main()
