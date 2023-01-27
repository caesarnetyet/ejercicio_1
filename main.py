import uuid

from controller.venta_controller import VentaController
from models.ventas import Ventas
from models.producto import Producto
from controller.producto_controller import ProductoController
from models.clientes import Clientes
from controller.persona_controller import PersonaController
from parse import ParseJson
from pprint import pprint

from views.producto_view import vista_producto

productos = Producto()
productos_2 = Producto()
producto = Producto("2053", "Pipipi", "un objeto producto pipipi", 2042)
producto_dos = Producto("2053", "bromo", "lorem", 2042)
producto_tres = Producto("2053", "trac", "iptsum", 2042.3)
producto_cuatro = Producto("2053", "buh", "bru", 2042)

clientes = Clientes()

cliente = Clientes("sadnkjasn", "julio", "TOX2309", "8139895086")
cliente_dos = Clientes("sadnkjasn", "julio", "TOX2309", "8139895086")
cliente_tres = Clientes("sadnkjasn", "julio", "TOX2309", "8139895086")

print(uuid.uuid4().__str__())

clientes.agregar(cliente, cliente_dos, cliente_tres)

productos.agregar(producto, producto_dos, producto_tres, producto_cuatro)

productos.borrar(producto_cuatro)

ventas = Ventas()
ventas.agregar(Ventas(cliente, "Venta en computadora", productos, "09/01/2023"))
ParseJson("Ventadas").dump(ventas)
ParseJson("productos").dump(productos)

productos_controller = ProductoController()

vista_producto(productos_controller)

personas = PersonaController()

personas.insertar_cliente()


productos_controller.insertar_producto()

venta_controller = VentaController()

venta_controller.insertar_venta(personas.clientes, productos_controller.productos)


ParseJson(input("Ingresa el nombre del archivo")).dump(venta_controller.ventas)

ventas_1 = Ventas(cliente, "Venta en computadora", productos, "09/01/2023")
