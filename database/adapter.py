from pymongo import MongoClient
from config.environment import Settings


class DatabaseAdapter:

    def __init__(self, collection: str):
        self.collection = collection
        self.mongo_config = Settings.get_mongodb()
        self.client = MongoClient(self.mongo_config['host'])
        self.db = self.client[self.mongo_config['name']]
