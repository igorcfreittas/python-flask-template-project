from app.repositories.user_repository import UserRepository


class UserController:

    def __init__(self):
        self.user_repository = UserRepository()

    def create(self, user_data: dict) -> dict:
        response = self.user_repository.store(user_data)
        return response

    def find_by_id(self, _id: str):
        try:
            response = self.user_repository.find_by_id(_id)
            return response
        except Exception as e:
            return {'error': e.__str__()}, 400
