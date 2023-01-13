from models.producto import Producto
from parse import ParseJson

productos = Producto()
productos_2 = Producto()
producto = Producto("2053", "Pipipi", "un objeto producto pipipi", 2042)
producto_dos = Producto("2053", "bromo", "lorem", 2042)
producto_tres = Producto("2053", "trac", "iptsum", 2042)
producto_cuatro = Producto("2053", "buh", "bru", 2042)

productos.agregar(producto, producto_dos, producto_tres, producto_cuatro)

productos.borrar(producto_cuatro)

importado = ParseJson('dumps.json')

importado.dump(productos)

productos_importado = importado.read()

print(productos_importado[0].get('codigo'))
