from crud import Crud
from producto import Producto


class Ventas(Crud):
    def __init__(self, cliente, detalle, producto, fecha, total):
        super().__init__()

        self.cliente: str = cliente
        self.detalle: str = detalle
        self.producto: Producto = producto
        self.fecha: str = fecha
        self.total: float = total

    def obtener_datos(self):
        return {

            "cliente": self.cliente,
            "detalle": self.detalle,
            "producto": self.producto,
            "fecha": self.fecha,
            "total": self.total,

        }
