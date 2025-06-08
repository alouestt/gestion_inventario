from controllers.inventario_controller import InventarioController

def main():
    inventario = InventarioController()

    while True:
        print("\n===== SISTEMA DE GESTIÓN DE INVENTARIOS =====")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Editar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("\nSeleccione opción: ").strip()

        try:

            match opcion:
                case '1':
                    nombre = input("\nNombre producto: ").strip()
                    inventario.registrar_producto(nombre)
                    print("\nProducto registrado.")
                
                case '2':
                    productos = inventario.listar_productos()
                    if productos:
                        for i, p in enumerate(productos, 1):
                            print(f"{i}. {p.nombre}")
                    else:
                        print("\nNo hay productos.")
                
                case '3':
                    nombre = input("\nBuscar producto: ").strip()
                    encontrados = inventario.buscar_producto(nombre)
                    if encontrados:
                        for p in encontrados:
                            print("-", p.nombre)
                    else:
                        print("\nNo encontrado.")
                
                case '4':
                    nombre_actual = input("\nNombre producto a editar: ").strip()
                    nuevo_nombre = input("\nNuevo nombre: ").strip()
                    inventario.editar_producto(nombre_actual, nuevo_nombre)
                    print("\nProducto actualizado.")
                
                case '5':
                    nombre = input("\nNombre producto a eliminar: ").strip()
                    inventario.eliminar_producto(nombre)
                    print("\nProducto eliminado.")
                
                case '6':
                    print("\nHa salido del sistema.")
                    break
                
                case _:
                    print("\nOpción inválida.")

        except ValueError as e:
            print("Error:", e)
