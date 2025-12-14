# ===============================
# PROGRAMACIÓN TRADICIONAL
# ===============================
# En este enfoque se utilizan funciones independientes
# sin clases ni objetos.


def ingresar_temperaturas():
    """Solicita al usuario las temperaturas diarias de la semana.
    Retorna una lista con 7 valores."""
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def promedio_semanal(temperaturas):
    """Calcula y retorna el promedio semanal de temperaturas."""
    return sum(temperaturas) / len(temperaturas)


# Programa principal (tradicional)
if __name__ == "__main__":
    print("--- Programación Tradicional ---")
    temps = ingresar_temperaturas()
    promedio = promedio_semanal(temps)
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# ===============================
# PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# ===============================
# En este enfoque se usan clases, encapsulamiento
# y herencia de forma básica.


class ClimaDiario:
    """Clase que representa la temperatura diaria."""

    def __init__(self, temperatura):
        # Encapsulamiento: atributo protegido
        self._temperatura = temperatura

    def obtener_temperatura(self):
        return self._temperatura


class ClimaSemanal:
    """Clase que gestiona las temperaturas de toda la semana."""

    def __init__(self):
        self._dias = []  # lista de objetos ClimaDiario

    def ingresar_datos(self):
        """Ingresa las temperaturas diarias usando objetos."""
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self._dias.append(ClimaDiario(temp))

    def calcular_promedio(self):
        """Calcula el promedio semanal usando los objetos."""
        total = sum(dia.obtener_temperatura() for dia in self._dias)
        return total / len(self._dias)


# Programa principal (POO)
if __name__ == "__main__":
    print("\n--- Programación Orientada a Objetos ---")
    clima = ClimaSemanal()
    clima.ingresar_datos()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")
