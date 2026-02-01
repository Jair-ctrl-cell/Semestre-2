import os
import subprocess
import platform
import sys
from colorama import init, Fore

# Inicializar colorama
init(autoreset=True)

def mostrar_bienvenida():
    print(Fore.CYAN + "=" * 55)
    print(Fore.CYAN + "   PROGRAMACIÓN ORIENTADA A OBJETOS")
    print(Fore.CYAN + "   Dashboard de Gestión de Scripts")
    print(Fore.CYAN + "=" * 55)

def mostrar_ayuda():
    print(Fore.GREEN + "\n=== AYUDA DEL SISTEMA ===")
    print("Este dashboard permite organizar y ejecutar")
    print("los scripts del curso de Programación Orientada a Objetos.\n")

    print(Fore.YELLOW + "¿Cómo usar el dashboard?")
    print("- Seleccione una unidad desde el menú principal.")
    print("- Elija una subcarpeta correspondiente al tema.")
    print("- Visualice el código del script.")
    print("- Decida si desea ejecutarlo.\n")

    print(Fore.YELLOW + "Opciones disponibles:")
    print("1, 2, ...  → Seleccionar unidad")
    print("H          → Mostrar esta ayuda")
    print("S          → Ver información del sistema")
    print("0          → Salir del programa\n")

    print(Fore.YELLOW + "¿Dónde pedir ayuda?")
    print("- Tutorías del docente según horario establecido.")
    print("- Compañeros de clase mediante foros académicos.")
    print("- Documentación oficial de Python: https://docs.python.org")
    print("- Repositorio del curso en GitHub.")
    print("- Uso de comentarios y mensajes de error del sistema.")

def mostrar_info_sistema():
    print(Fore.GREEN + "\n=== INFORMACIÓN DEL SISTEMA ===")
    print(f"Sistema operativo : {platform.system()} {platform.release()}")
    print(f"Arquitectura      : {platform.machine()}")
    print(f"Procesador        : {platform.processor()}")
    print(f"Versión de Python : {platform.python_version()}")
    print(f"Implementación    : {platform.python_implementation()}")
    print(f"Ruta de ejecución : {os.getcwd()}")
    print(f"Ejecutable Python : {sys.executable}")

def mostrar_codigo(ruta_script):
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(Fore.CYAN + f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except Exception as e:
        print(Fore.RED + f"Error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        print(Fore.GREEN + "Ejecutando script...")
        if os.name == 'nt':
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(Fore.RED + f"Error al ejecutar: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    mostrar_bienvenida()

    while True:
        print(Fore.BLUE + "\n=== MENÚ PRINCIPAL ===")
        for key in unidades:
            print(Fore.YELLOW + f"{key} - {unidades[key]}")
        print(Fore.YELLOW + "H - Ayuda")
        print(Fore.YELLOW + "S - Información del sistema")
        print(Fore.RED + "0 - Salir")

        opcion = input("Seleccione una opción: ").upper()

        if opcion == '0':
            print(Fore.GREEN + "Saliendo del programa.")
            break
        elif opcion == 'H':
            mostrar_ayuda()
        elif opcion == 'S':
            mostrar_info_sistema()
        elif opcion in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[opcion]))
        else:
            print(Fore.RED + "Opción no válida.")

def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = sorted([f.name for f in os.scandir(ruta_unidad) if f.is_dir()])

    while True:
        print(Fore.BLUE + "\n--- SUBMENÚ ---")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(Fore.YELLOW + f"{i} - {carpeta}")
        print(Fore.RED + "0 - Regresar")

        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            break
        if not opcion.isdigit():
            print(Fore.RED + "Entrada no válida.")
            continue

        indice = int(opcion) - 1
        if 0 <= indice < len(sub_carpetas):
            mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[indice]))
        else:
            print(Fore.RED + "Opción fuera de rango.")

def mostrar_scripts(ruta_sub_carpeta):
    scripts = sorted([
        f.name for f in os.scandir(ruta_sub_carpeta)
        if f.is_file() and f.name.endswith('.py')
    ])

    while True:
        print(Fore.BLUE + "\n--- SCRIPTS DISPONIBLES ---")
        for i, script in enumerate(scripts, start=1):
            print(Fore.YELLOW + f"{i} - {script}")
        print(Fore.RED + "0 - Regresar")

        opcion = input("Seleccione un script: ")

        if opcion == '0':
            break
        if not opcion.isdigit():
            print(Fore.RED + "Entrada no válida.")
            continue

        indice = int(opcion) - 1
        if 0 <= indice < len(scripts):
            ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
            codigo = mostrar_codigo(ruta_script)

            if codigo:
                ejecutar = input("¿Ejecutar script? (1: Sí / 0: No): ")
                if ejecutar == '1':
                    ejecutar_codigo(ruta_script)
                else:
                    print(Fore.YELLOW + "Ejecución cancelada.")
                input("\nPresione Enter para continuar...")
        else:
            print(Fore.RED + "Opción fuera de rango.")

# Ejecutar dashboard
if __name__ == "__main__":
    mostrar_menu()
