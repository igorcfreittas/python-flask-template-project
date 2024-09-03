from app.routes.index_resource import IndexResource
from app.routes.user_resource import UserResource


class Router:
    def __init__(self, api):
        api.add_resource(IndexResource, '/')
        api.add_resource(UserResource, '/user', '/user/<string:_id>')
