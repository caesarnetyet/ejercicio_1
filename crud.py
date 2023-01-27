class Crud:
    def __init__(self):
        self.lista = []

    def agregar(self, *modelos: object):
        for modelo in modelos:
            self.lista.append(modelo)

    def borrar(self, modelo: object):
        for x, model in enumerate(self.lista):
            if model == modelo:
                del self.lista[x]

    def doc_name(self):
        return self.__class__.__name__

    def todos(self):
        lista_json = []
        for objt in self.lista:
            objt_dict = vars(objt)
            lista_json.append(objt_dict)
        return lista_json

    def size(self):
        return len(self.lista)

    def obtener_nombres(self):
        lista = []
        for objt in self.lista:
            lista.append({
                "id": objt.id,
                "nombre": objt.nombre})
        return lista


