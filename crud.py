class Crud:
    def __init__(self):
        self._lista = []

    def agregar(self, *modelos: object):
        for modelo in modelos:
            self._lista.append(modelo)

    def borrar(self, modelo: object):
        for x, model in enumerate(self._lista):
            if model == modelo:
                del self._lista[x]

    def mostrar(self):
        lista_json = []
        for objt in self._lista:
            dict_objt = vars(objt)
            dict_objt.pop("_lista")
            lista_json.append(dict_objt)

        return lista_json