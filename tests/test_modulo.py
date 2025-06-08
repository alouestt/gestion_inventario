import unittest
from controllers.inventario_controller import InventarioController

class TestInventario(unittest.TestCase):
    def setUp(self):
        self.inv = InventarioController(archivo="test_productos.json")
        self.inv.productos = []
        self.inv.guardar()

    def test_registrar_producto(self):
        self.inv.registrar_producto("Manzana")
        self.assertEqual(len(self.inv.productos), 1)
        with self.assertRaises(ValueError):
            self.inv.registrar_producto("")

    def test_eliminar_producto(self):
        self.inv.registrar_producto("Pera")
        self.inv.eliminar_producto("Pera")
        self.assertEqual(len(self.inv.productos), 0)
        with self.assertRaises(ValueError):
            self.inv.eliminar_producto("Naranja")

if __name__ == '__main__':
    unittest.main()
