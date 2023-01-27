from models.ventas import Ventas
from models.clientes import Clientes
from pprint import pprint
from models.producto import Producto
from parse import ParseJson


class VentaController:

    def __init__(self):
        self.ventas = Ventas()
        self.file = 'dumps/ventas.json'

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
                ParseJson(self.file).dump(self.ventas)
                return
        print("No se encontro el cliente")

    def cargar_ventas(self):
        ventas = ParseJson(self.file).read()
        for venta in ventas:
            self.ventas.agregar(Ventas(venta['cliente'], venta['descripcion'], venta['productos']))
