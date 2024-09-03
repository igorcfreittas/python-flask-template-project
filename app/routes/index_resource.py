from flask_restful import Resource


class IndexResource(Resource):
    def get(self):
        return {"index": 'route GET /'}
