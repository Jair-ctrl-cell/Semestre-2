from modelos.producto import Producto
from servicios.inventario import Inventario

def mostrar_menu():
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")

            nueva_cantidad = int(cantidad) if cantidad else None
            nuevo_precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Ingrese nombre o parte del nombre: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.listar_productos()

        elif opcion == "6":
            print(" Saliendo del sistema...")
            break

        else:
            print(" Opción inválida.")

if __name__ == "__main__":
    main()
