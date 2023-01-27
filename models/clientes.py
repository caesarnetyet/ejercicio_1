from crud import Crud


class Clientes(Crud):
    def __init__(self, id: str = None, nombre: str = None, rfc: str = None, telefono: str = None):
        super().__init__()
        self.id: str = id
        self.nombre: str = nombre
        self.rfc: str = rfc
        self.telefono: str = telefono
