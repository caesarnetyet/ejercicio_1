from models.producto import Producto
import uuid
from parse import ParseJson


class ProductoController:
    def __init__(self):
        self.productos = Producto()
        self.file = 'dumps/productos.json'

    def cargar_productos(self):
        product = ParseJson(self.file).read()

        for producto in product:
            self.productos.agregar(Producto(producto['id'], producto['nombre'],
                                            producto['descripcion'], producto['precio']))

    def insertar_producto(self):
        seguir = True
        while seguir:
            nombre = input('Ingresa el nombre del producto')
            descripcion = input("Ingresa los detalles de tu producto")
            precio = float(input("Que precio tiene tu producto?"))
            producto = Producto(uuid.uuid4().__str__(), nombre, descripcion, precio)
            self.productos.agregar(producto)
            seguir = input("Deseas seguir agregando productos? (s/n)") == 's'
        ParseJson(self.file).dump(self.productos)

    def modificar_producto(self, id_: str):

        if self.productos.size() == 0:
            print("No hay productos")
            return

        for producto in self.productos.lista:
            if producto.id == id_:
                nombre = input('Ingresa el nombre del producto')
                descripcion = input("Ingresa los detalles de tu producto")
                precio = float(input("Que precio tiene tu producto?"))
                producto.nombre = nombre
                producto.descripcion = descripcion
                producto.precio = precio
                return
        print("No se encontro el producto")

    def eliminar_producto(self, producto_id: str):
        for producto in self.productos.lista:
            if producto.id == producto_id:
                self.productos.borrar(producto)
                ParseJson(self.file).dump(self.productos)