from modelos.archivo import Archivo

class GestorArchivos:
    """
    Clase de servicio que gestiona operaciones sobre archivos.
    """

    def crear_y_escribir(self, nombre_archivo, contenido):
        """
        Crea un archivo, escribe contenido y permite observar
        el uso del constructor y destructor.
        """
        archivo = Archivo(nombre_archivo)
        archivo.escribir(contenido)
        print("[SERVICIO] Escritura completada.")
        return archivo

