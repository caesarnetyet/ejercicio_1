import json
from crud import Crud
from models.ventas import Ventas


class ParseJson:
    def __init__(self, file: str = None):
        self.file = file

    def dump(self, modelo: Crud | dict):
        directory: str
        if self.file is not None:
            directory = 'dumps/'+self.file+'.json'
        else:
            directory = 'dumps/' + modelo.doc_name()+'.json'

        with open(directory, 'w') as file:
            if modelo is dict:
                json.dump(modelo, file)
                return
            elif modelo.size() > 0:
                json.dump(modelo.todos(), file)
                return
            else:
                json.dump(vars(modelo), file)

    def read(self):
        try:
            with open(self.file, 'r') as file:
                dictionary_file = json.load(file)
                print(dictionary_file)
                return dictionary_file

        except FileNotFoundError:
            return []
