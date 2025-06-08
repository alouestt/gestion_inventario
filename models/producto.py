class Producto:
    def __init__(self, nombre: str):
        self.nombre = nombre.capitalize()

    def to_dict(self):
        return {"nombre": self.nombre}

    @staticmethod
    def from_dict(data):
        return Producto(data["nombre"])
