from inventario import Inventario
from producto import Producto


def main():
    inv = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Anadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario")
        print("6. Salir")

        op = input("Seleccione opcion: ")

        if op == "1":
            id_ = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            p = Producto(id_, nombre, cantidad, precio)
            inv.anadir_producto(p)

        elif op == "2":
            id_ = input("ID a eliminar: ")
            inv.eliminar_producto(id_)

        elif op == "3":
            id_ = input("ID a actualizar: ")
            cantidad = input("Nueva cantidad (enter para omitir): ")
            precio = input("Nuevo precio (enter para omitir): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inv.actualizar_producto(id_, cantidad, precio)

        elif op == "4":
            nombre = input("Nombre a buscar: ")
            inv.buscar_por_nombre(nombre)

        elif op == "5":
            inv.mostrar_todos()

        elif op == "6":
            print("Saliendo...")
            break

        else:
            print("Opcion invalida")


if __name__ == "__main__":
    main()