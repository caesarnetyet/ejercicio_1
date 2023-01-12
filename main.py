from models.producto import Producto
import pprint

productos = Producto()

producto = Producto("2053", "Pipipi", "un objeto producto pipipi", 2042)
producto_dos = Producto("2053", "Pipipi", "un objeto producto pipipi", 2042)
producto_tres = Producto("2053", "Pipipi", "un objeto producto pipipi", 2042)
producto_cuatro = Producto("2053", "Pipipi", "un objeto producto pipipi", 2042)

productos.agregar(producto, producto_dos, producto_tres, producto_cuatro)

productos.borrar(producto_cuatro)

# pprint.pprint(productos.mostrar())

# transformar string a json


print(producto.diccionario())
