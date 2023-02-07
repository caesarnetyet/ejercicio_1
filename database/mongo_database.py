from pymongo import MongoClient


class MongoDatabase:
    def __init__(self, host="localhost", port=27017, database="test", collection="test"):
        self.host = host
        self.port = port
        self.database = database
        self.collection = collection
        self.client = MongoClient(host, port)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def insert(self, data):
        self.collection.insert_one(data)

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
