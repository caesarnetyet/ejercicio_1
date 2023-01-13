import json
from crud import Crud


class ParseJson:
    def __init__(self, file: str):
        self.file = file

    def dump(self, modelo: Crud):
        with open(self.file, 'w') as file:
            if modelo.list_size() > 0:
                json.dump(modelo.todos(), file)
                return
            json.dump(vars(modelo), file)

    def read(self):
        with open(self.file, 'r') as file:
            return json.load(file)
