from crud import Crud
from models.producto import Producto
from models.clientes import Clientes


class Ventas(Crud):
    def __init__(self, _id: str = None, cliente: Clientes = None, detalle: str = None, producto: Producto = None, fecha: str = None, total: float = None):
        super().__init__()
        self._id: str = _id
        if cliente is None:
            self.cliente = Clientes()
        else:
            self.cliente: dict = vars(cliente)
        self.detalle: str = detalle
        if producto is None:
            self.producto = Producto()
            self.total = 0.0
        else:
            self.producto: list = producto.todos()
            if total is None:
                self.total: float = self.get_total()
            else:
                self.total: float = total
        self.fecha: str = fecha


    def get_total(self):
        total = 0.0
        for producto in self.producto:
            total += producto['precio']
        return total
