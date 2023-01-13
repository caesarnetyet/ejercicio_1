from crud import Crud


class Producto(Crud):
    def __init__(self, codigo: str = None, nombre: str = None, descripcion: str = None, precio: float = None):
        super().__init__()

        self.codigo: str = codigo
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.precio: float = precio
