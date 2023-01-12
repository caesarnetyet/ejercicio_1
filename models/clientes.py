from crud import Crud


class Clientes(Crud):
    id: int
    codigo: str
    nombre: str
    descripcion: str
    precio: float

    def obtener_datos(self):
        return {
            "id": self.id,
            "codigo": self.codigo,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio
    }
