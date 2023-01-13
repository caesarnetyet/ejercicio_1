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

    def doc_name(self):
        return self.__class__.__name__

    def todos(self):
        lista_json = []
        for objt in self._lista:
            dict_objt = vars(objt)
            lista_json.append(dict_objt)
        return lista_json

    def list_size(self):
        return len(self._lista)
