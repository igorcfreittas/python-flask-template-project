from app.repositories.repository import Repository
from bson import json_util, ObjectId
import json


class UserRepository(Repository):

    def __init__(self, collection: str = 'users'):
        super().__init__(collection)

    def store(self, attributes: dict) -> dict:
        response = self.db[self.collection].insert_one(attributes).inserted_id
        user_id = json.loads(json_util.dumps(response))
        attributes['_id'] = user_id['$oid']
        attributes.pop('password')
        return attributes

    def find_by_id(self, _id: str):
        response = self.db[self.collection].find_one(
            {'_id': ObjectId(_id)}, {'password': 0}
        )
        if not response:
            return {}

        response.pop('_id')
        response['_id'] = _id
        return response
