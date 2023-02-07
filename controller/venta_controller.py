from database.mongo_database import MongoDatabase
from models.ventas import Ventas
from models.clientes import Clientes
from pprint import pprint
from models.producto import Producto
from parse import ParseJson
from datetime import date
from copy import deepcopy
from uuid import uuid4
class VentaController:

    def __init__(self, clientes: Clientes, productos: Producto):
        self.ventas = Ventas()
        self.file = 'dumps/Ventas.json'
        self.clientes:Clientes = clientes
        self.productos:Producto = productos
        self.db = MongoDatabase()
        self.db.set_collection('ventas')

    def insertar_venta(self):
        if self.clientes.size() == 0:
            print("No hay clientes registrados")
            return
        if self.productos.size() == 0:
            print("No hay productos registrados")
            return
        pprint(self.clientes.obtener_nombres())
        cliente_id = input("Selecciona e ingresa el id del cliente")
        for cliente in self.clientes.lista:
            if cliente.id == cliente_id:
                productos = self.productos_seleccionados()
                descripcion = input("Ingresa el detalle de la venta")
                fecha = date.today().__str__()
                venta = Ventas(uuid4().__str__(), cliente, descripcion, productos, fecha)
                venta_ref = deepcopy(venta)
                self.ventas.agregar(venta)
                if self.db.insert_one(venta_ref.__dict__):
                    ParseJson(self.file).dump(self.ventas)
                    print("Venta registrada")
                return
        print("No se encontro el cliente")

    def productos_seleccionados(self):
        productos = Producto()
        seguir = True
        pprint(self.productos.obtener_nombres())
        while seguir:
            seleccion = input("Selecciona e ingresa el id del producto que deseas agregar")
            for producto in self.productos.lista:
                if producto.id == seleccion:
                    productos.agregar(producto)
            seguir = input("Quieres agregar otro producto? s/n") == "s"
        return productos

    def cargar_ventas(self):
        ventas = ParseJson(self.file).read()
        print(ventas)
        for venta in ventas:
            cliente = Clientes(venta['cliente']['id'], venta['cliente']['nombre'], venta['cliente']['rfc'], venta['cliente']['telefono'])
            producto = Producto()
            for prod in venta['producto']:
                producto.agregar(Producto(prod['id'], prod['nombre'], prod['precio']))

            self.ventas.agregar(Ventas(venta['_id'], cliente, venta['detalle'], producto, venta['fecha'], venta['total']))


