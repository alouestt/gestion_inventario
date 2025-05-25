# main.py - Proyecto base en Python para gestión de inventario

productos = []

def registrar_producto():
    while True:
        nombre = input("\nIngrese el nombre del producto: ").strip()

        if not nombre:
            print("\nEl nombre no puede estar vacío.")
        elif nombre.lower() in [p.lower() for p in productos]:
            print("\nEl producto ya está registrado.")
        else:
            productos.append(nombre.capitalize())
            print("\nProducto registrado.")
            break

def listar_productos():
    if productos:
        print("\nLista de productos:\n")
        for i, p in enumerate(productos, 1):
            print(f"{i}. {p}")
    else:
        print("\nNo hay productos registrados.")

def buscar_producto():
    nombre = input("\nIngrese el nombre del producto a buscar: ").strip()

    encontrados = [p for p in productos if nombre.lower() in p.lower()]
    if encontrados:
        print("\nProductos encontrados:\n")
        for p in encontrados:
            print("-", p)
    else:
        print("\nNo se encontraron productos.")

def editar_producto():
    while True:
        nombre = input("\nIngrese el nombre del producto a editar (o escriba 'salir' para cancelar): ").strip()
        
        if nombre.lower() == 'salir':
            print("\nEdición cancelada.")
            break

        for i, p in enumerate(productos):
            if p.lower() == nombre.lower():
                while True:
                    nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
                    if nuevo_nombre:
                        productos[i] = nuevo_nombre.capitalize()
                        print("\nProducto actualizado.")
                        return
                    else:
                        print("\nEl nuevo nombre no puede estar vacío.")
        
        print("\nProducto no encontrado. Intente de nuevo.")

def eliminar_producto():
    while True:
        nombre = input("\nIngrese el nombre del producto a eliminar (o escriba 'salir' para cancelar): ").strip()
        
        if nombre.lower() == 'salir':
            print("\nEliminación cancelada.")
            break

        for p in productos:
            if p.lower() == nombre.lower():
                productos.remove(p)
                print("\nProducto eliminado.")
                return
            
        print("\nProducto no encontrado. Intente de nuevo.")

def main():
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE INVENTARIOS =====")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Editar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        match opcion:
            case '1':
                registrar_producto()
            case '2':
                listar_productos()
            case '3':
                buscar_producto()
            case '4':
                editar_producto()
            case '5':
                eliminar_producto()
            case '6':
                print("\nHa salido del sistema.")
                break
            case _:
                print("\nOpción inválida.")
                
if __name__ == "__main__":
    main()
