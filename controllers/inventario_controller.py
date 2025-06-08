from models.producto import Producto
from utils.persistencia import guardar_datos, cargar_datos

class InventarioController:
    def __init__(self, archivo="productos.json"):
        self.archivo = archivo
        self.productos = self.cargar()

    def cargar(self):
        datos = cargar_datos(self.archivo)
        return [Producto.from_dict(p) for p in datos]

    def guardar(self):
        datos = [p.to_dict() for p in self.productos]
        guardar_datos(self.archivo, datos)

    def registrar_producto(self, nombre):
        if not nombre.strip():
            raise ValueError("\nEl nombre no puede estar vacío.")
        if any(p.nombre.lower() == nombre.lower() for p in self.productos):
            raise ValueError("\nProducto ya registrado.")
        self.productos.append(Producto(nombre))
        self.guardar()

    def listar_productos(self):
        return self.productos

    def buscar_producto(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

    def editar_producto(self, nombre_actual, nuevo_nombre):
        for p in self.productos:
            if p.nombre.lower() == nombre_actual.lower():
                if not nuevo_nombre.strip():
                    raise ValueError("\nNuevo nombre no puede estar vacío.")
                p.nombre = nuevo_nombre.capitalize()
                self.guardar()
                return
        raise ValueError("\nProducto no encontrado.")

    def eliminar_producto(self, nombre):
        for p in self.productos:
            if p.nombre.lower() == nombre.lower():
                self.productos.remove(p)
                self.guardar()
                return
        raise ValueError("\nProducto no encontrado.")
