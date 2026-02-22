import os
from modelos.producto import Producto


class Inventario:
    def __init__(self):
        # ruta del archivo en carpeta servicios
        carpeta = os.path.dirname(os.path.abspath(__file__))
        self.archivo = os.path.join(carpeta, "inventario.txt")

        self.productos = []

        # crear archivo si no existe
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", encoding="utf-8"):
                pass
            print("Archivo inventario.txt creado")

        # cargar datos
        self.cargar_desde_archivo()

    # ======================
    # CARGAR ARCHIVO
    # ======================
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id_p, nombre, cantidad, precio = datos
                        self.productos.append(
                            Producto(id_p, nombre, int(cantidad), float(precio))
                        )
        except Exception as e:
            print("Error al cargar inventario:", e)

    # ======================
    # GUARDAR ARCHIVO
    # ======================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(
                        f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    )
        except Exception as e:
            print("Error al guardar inventario:", e)

    # ======================
    # AÑADIR PRODUCTO
    # ======================
    def añadir_producto(self, id_producto: object, nombre: object, cantidad: object, precio: object) -> None:
        """

        :param id_producto:
        :param nombre:
        :param cantidad:
        :param precio:
        :return:
        :rtype: None
        """
        # verificar duplicado
        if self.buscar_producto(id_producto):
            print("Error: ID ya existe")
            return

        # crear producto
        nuevo = Producto(id_producto, nombre, cantidad, precio)

        # añadir a lista
        self.productos.append(nuevo)

        # guardar archivo
        self.guardar_en_archivo()

        print("Producto añadido correctamente")

    # ======================
    # ELIMINAR
    # ======================
    def eliminar_producto(self, id_producto):
        producto = self.buscar_producto(id_producto)
        if producto:
            self.productos.remove(producto)
            self.guardar_en_archivo()
            print("Producto eliminado")
        else:
            print("Producto no encontrado")

    # ======================
    # ACTUALIZAR
    # ======================
    def actualizar_producto(self, id_producto, nombre=None, cantidad=None, precio=None):
        producto = self.buscar_producto(id_producto)

        if not producto:
            print("Producto no encontrado")
            return

        if nombre:
            producto.set_nombre(nombre)

        if cantidad is not None:
            producto.set_cantidad(cantidad)

        if precio is not None:
            producto.set_precio(precio)

        self.guardar_en_archivo()
        print("Producto actualizado")

    # ======================
    # BUSCAR
    # ======================
    def buscar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                return p
        return None

    # ======================
    # LISTAR
    # ======================
    def listar_productos(self):
        if not self.productos:
            print("Inventario vacío")
            return

        print("=== INVENTARIO ===")
        for p in self.productos:
            print(
                f"ID:{p.get_id()} "
                f"Nombre:{p.get_nombre()} "
                f"Cantidad:{p.get_cantidad()} "
                f"Precio:{p.get_precio()}"
            )