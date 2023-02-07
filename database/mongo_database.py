from pprint import pprint

from pymongo import MongoClient

from crud import Crud
from parse import ParseJson


class MongoDatabase:
    def __init__(self, host="localhost", port=27017, database="test", collection="test"):
        self.host = host
        self.port = port
        self.database = database
        self.collection = collection
        self.client = MongoClient(host, port, serverSelectionTimeoutMS=3000)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def insert_one(self, data):
        try:
            self.collection.insert_one(data)
            failed = ParseJson('dumps/failed.json').read()
            if len(failed) > 1:
                try:
                    pprint(failed)
                    self.collection.insert_many(failed)
                    ParseJson('dumps/failed.json').delete()
                    print("Se insertaron los datos que no se pudieron insertar anteriormente")
                except:
                    print("Error al insertar los datos que no se pudieron insertar anteriormente")
                    return
            return True
        except:
            print("Error al insertar en la base de datos")
            json_fallidos = ParseJson('dumps/failed.json').read()
            json_fallidos.append(data)
            ParseJson('dumps/failed.json').dump(json_fallidos)
            return False

    def insert_many(self, data):
        self.collection.insert_many(data)

    def find(self, query):
        return self.collection.find(query)

    def update(self, query, data):
        self.collection.update_one(query, data)

    def delete(self, query):
        self.collection.delete_one(query)

    def count(self, query):
        return self.collection.count_documents(query)

    def drop(self):
        self.collection.drop()

    def close(self):
        self.client.close()

    def set_collection(self, collection):
        self.collection = self.db[collection]

    def set_database(self, database):
        self.db = self.client[database]

    def set_host(self, host):
        self.host = host
        self.client = MongoClient(host, self.port)

    def set_port(self, port):
        self.port = port
        self.client = MongoClient(self.host, port)