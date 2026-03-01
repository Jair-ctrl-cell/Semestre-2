import json
from producto import Producto


class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}
        self.cargar()

    # ========================
    # CRUD
    # ========================

    def anadir_producto(self, producto):
        if producto.id in self.productos:
            print("ID ya existe")
            return

        self.productos[producto.id] = producto
        self.guardar()
        print("Producto anadido")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar()
            print("Producto eliminado")
        else:
            print("No existe")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto not in self.productos:
            print("No existe")
            return

        if cantidad is not None:
            self.productos[id_producto].cantidad = cantidad

        if precio is not None:
            self.productos[id_producto].precio = precio

        self.guardar()
        print("Actualizado")

    def buscar_por_nombre(self, nombre):
        encontrados = [
            p for p in self.productos.values()
            if nombre.lower() in p.nombre.lower()
        ]

        if not encontrados:
            print("No encontrado")
        else:
            for p in encontrados:
                print(p)

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacio")
            return

        for p in self.productos.values():
            print(p)

    # ========================
    # ARCHIVO
    # ========================

    def guardar(self):
        datos = [p.to_dict() for p in self.productos.values()]

        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

    def cargar(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)

                for item in datos:
                    producto = Producto.from_dict(item)
                    self.productos[producto.id] = producto

        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = {}