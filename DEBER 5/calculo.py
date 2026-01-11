"""
Programa: Cálculo del área de un rectángulo
Descripción: Este programa solicita al usuario el largo y el ancho
de un rectángulo, calcula su área y muestra el resultado.
"""

# Solicitar datos al usuario
largo = float(input("Ingrese el largo del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

# Validar que los valores sean positivos
datos_validos = largo > 0 and ancho > 0

# Verificar si los datos ingresados son correctos
if datos_validos:
    # Cálculo del área
    area_rectangulo = largo * ancho

    # Mostrar el resultado
    print("El área del rectángulo es:", area_rectangulo)
else:
    print("Error: El largo y el ancho deben ser valores positivos.")
