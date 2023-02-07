import uuid

from controller.venta_controller import VentaController
from models.ventas import Ventas
from models.producto import Producto
from controller.producto_controller import ProductoController

from controller.persona_controller import PersonaController

from views.persona_view import vista_persona
from views.producto_view import vista_producto
from views.ventas_view import vista_ventas


productos_controller = ProductoController()
try:
    productos_controller.cargar_productos()
except:
    print("No hay productos")
personas_controller = PersonaController()

try:
    personas_controller.cargar_clientes()
except:
    print("No hay clientes registrados")

venta_controller = VentaController(personas_controller.clientes, productos_controller.productos)
while True:
    print("1. - Menu Productos")
    print("2. - Menu Ventas")
    print("3. = Menu Clientes")
    print("3. - Salir")
    opcion = int(input("Ingresa una opcion: "))
    if opcion == 1:
        vista_producto(productos_controller)
    elif opcion == 2:
        vista_ventas(venta_controller)
        pass
    elif opcion == 3:
        vista_persona(personas_controller)
        pass
    elif opcion == 4:
        break
    else:
        print("Opcion no valida")
