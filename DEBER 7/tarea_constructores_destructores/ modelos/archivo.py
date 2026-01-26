class Archivo:
    """
    Clase que representa un archivo del sistema.
    """

    def __init__(self, nombre, modo="w"):
        """
        Constructor (__init__)
        Inicializa el nombre del archivo, el modo de apertura
        y abre el archivo para su uso.
        """
        self.nombre = nombre
        self.modo = modo
        self.archivo = open(self.nombre, self.modo)
        print(f"[INIT] Archivo '{self.nombre}' abierto en modo '{self.modo}'.")

    def escribir(self, texto):
        """
        Escribe texto dentro del archivo.
        """
        self.archivo.write(texto + "\n")

    def __del__(self):
        """
        Destructor (__del__)
        Se ejecuta cuando el objeto es eliminado.
        Intenta cerrar el archivo si aún está abierto,
        liberando el recurso del sistema.
        """
        try:
            if not self.archivo.closed:
                self.archivo.close()
                print(f"[DEL] Archivo '{self.nombre}' cerrado correctamente.")
        except AttributeError:
            print("[DEL] El archivo ya fue eliminado.")
