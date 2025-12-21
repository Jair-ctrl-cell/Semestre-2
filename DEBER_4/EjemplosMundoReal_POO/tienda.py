# Clase Producto
# Representa un producto disponible en la tienda
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # Método para mostrar información del producto
    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}"

    # Método para reducir el stock cuando se realiza una compra
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            return False


# Clase Cliente
# Representa a un cliente de la tienda
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    # Método para agregar productos al carrito
    def agregar_al_carrito(self, producto, cantidad):
        if producto.vender(cantidad):
            self.carrito.append((producto.nombre, cantidad))
            print(f"{cantidad} unidad(es) de {producto.nombre} agregadas al carrito.")
        else:
            print("No hay suficiente stock disponible.")


# Uso de las clases (interacción entre objetos)
producto1 = Producto("Laptop", 800, 5)
producto2 = Producto("Mouse", 20, 10)

cliente1 = Cliente("Juan")

print(producto1.mostrar_info())
print(producto2.mostrar_info())

cliente1.agregar_al_carrito(producto1, 1)
cliente1.agregar_al_carrito(producto2, 2)

print("Carrito del cliente:", cliente1.carrito)
