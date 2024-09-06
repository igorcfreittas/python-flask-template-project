from flask_restful import Resource, request
from app.utils.request_parser import RequestParser
from app.middlewares.auth_middleware import auth
from app.controllers.user_controller import UserController


class UserResource(Resource):

    """
        required: False, it will be created with the new document
        but empty (if not present in the POST request body)
    """
    fields: dict = {
        'username': {'required': True, 'type': str},
        'email': {'required': True, 'type': str},
        'password': {'required': True, 'type': str},
        'cellphone': {'required': False, 'type': int},
        'age': {'required': False, 'type': int},
        'birth_date': {'required': False, 'type': str},
    }

    def __init__(self):
        self.user = UserController()

    @auth
    def get(self, _id: str):
        response = self.user.find_by_id(_id)
        return response

    def post(self):
        req = RequestParser.get(request.get_json(), self.fields)
        if 'errors' in req:
            return req['errors'], 400

        response = self.user.create(req)
        return response
