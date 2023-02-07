from models.clientes import Clientes
import uuid
from parse import ParseJson
from database.mongo_database import MongoDatabase


class PersonaController:
    def __init__(self):
        self.clientes = Clientes()
        self.file = 'dumps/clientes.json'
        self.db = MongoDatabase()
        self.db.set_collection('clientes')

    def cargar_clientes(self):
        clientes = ParseJson(self.file).read()

        for cliente in clientes:
            self.clientes.agregar(Clientes(cliente['id'], cliente['nombre'],
                                            cliente['rfc'], cliente['telefono']))

    def insertar_cliente(self):

        seguir = True
        while seguir:
            nombre = input('Ingresa el nombre del cliente')
            rfc = input("Ingresa el rfc del cliente")
            telefono = input("ingresa el telefono del cliente")
            persona = Clientes(uuid.uuid4().__str__(), nombre, rfc, telefono)
            self.clientes.agregar(persona)
            seguir = input("Deseas seguir agregando clientes? (s/n)") == 's'

        ParseJson(self.file).dump(self.clientes)

    def modificar_cliente(self, id_: str):
        if self.clientes.size() == 0:
            print("No hay productos")
            return

        for cliente in self.clientes.lista:
            if cliente.id == id_:
                nombre = input('Ingresa el nombre del cliente: ')
                rfc = input("Ingresa el rfc del cliente: ")
                telefono = input("Ingresa el numero de telefono del cliente: ")
                cliente.nombre = nombre
                cliente.rfc = rfc
                cliente.telefono = telefono
                ParseJson(self.file).dump(self.clientes)
                return
        print("No se encontro el cliente")

    def eliminar_cliente(self, cliente_id: str):
        for cliente in self.clientes.lista:
            if cliente.id == cliente_id:
                self.clientes.borrar(cliente)
                ParseJson(self.file).dump(self.clientes)