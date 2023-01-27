from models.ventas import Ventas
from models.clientes import Clientes
from pprint import pprint
from models.producto import Producto


class VentaController:

    def __init__(self):
        self.ventas = Ventas()

    def insertar_venta(self, clientes: Clientes, productos: Producto):
        if clientes.size() == 0:
            print("No hay clientes registrados")
            return
        if productos.size() == 0:
            print("No hay productos registrados")
            return
        pprint(clientes.obtener_nombres())
        cliente_id = input("Ingresa el id del cliente")
        for cliente in clientes.lista:
            if cliente.id == cliente_id:
                descripcion = input("Ingresa la descripcion de la venta")
                venta = Ventas(cliente, descripcion, productos)
                self.ventas.agregar(venta)
                return
        print("No se encontro el cliente")


