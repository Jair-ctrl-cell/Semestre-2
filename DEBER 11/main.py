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
            try:
                id_p = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                # MÉTODO CORRECTO
                inventario.añadir_producto(id_p, nombre, cantidad, precio)

            except ValueError:
                print("Error: cantidad y precio deben ser numéricos")

        elif opcion == "2":
            id_p = input("ID a eliminar: ")
            inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID a actualizar: ")
            nombre = input("Nuevo nombre: ")
            cantidad = input("Nueva cantidad: ")
            precio = input("Nuevo precio: ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_p, nombre or None, cantidad, precio)

        elif opcion == "4":
            id_p = input("ID a buscar: ")
            producto = inventario.buscar_producto(id_p)

            if producto:
                print(
                    f"ID:{producto.get_id()} "
                    f"Nombre:{producto.get_nombre()} "
                    f"Cantidad:{producto.get_cantidad()} "
                    f"Precio:{producto.get_precio()}"
                )
            else:
                print("Producto no encontrado")

        elif opcion == "5":
            inventario.listar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()