from models.clientes import Clientes
import uuid


class PersonaController:
    def __init__(self):
        self.clientes = Clientes()

    def insertar_cliente(self):
        nombre = input('Ingresa el nombre del cliente')
        rfc = input("Ingresa tu rfc")
        phone = input("Ingresa tu telefono")
        cliente = Clientes(uuid.uuid4().__str__(), nombre, rfc, phone)
        self.clientes.agregar(cliente)

    def modificar_cliente(self, id_: str):

        if self.clientes.size() == 0:
            print("No hay clientes registrados")
            return

        for cliente in self.clientes.lista:
            if cliente.id == id_:
                nombre = input('Ingresa el nombre del cliente')
                rfc = input("Ingresa tu rfc")
                telefono = input("Ingresa tu telefono")
                cliente.nombre = nombre
                cliente.rfc = rfc
                cliente.telefono = telefono
                return
        print("No se encontro el el cliente")
