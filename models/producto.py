from crud import Crud


class Producto(Crud):
    def __init__(self, id: str = None, nombre: str = None, descripcion: str = None, precio: float = None):
        super().__init__()

        self.id: str = id
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.precio: float = precio

