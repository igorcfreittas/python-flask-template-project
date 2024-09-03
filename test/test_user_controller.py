import unittest
import requests
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from app.controllers.user_controller import UserController


def get_user_data(user_id = ""):
    response = requests.get(f"http://127.0.0.1/user/{user_id}")
    return response.json()

class TestUserController(unittest.TestCase):

    def setUp(self):
        self.controller = UserController()
        self.controller.user_repository = MagicMock()

    @patch('requests.get')
    def test_request_success_get_user(self, mock_get):
        mock_response = Mock()
        response_dict = {
            "cellphone": "",
            "username": "asdsada",
            "email": "ola",
            "_id": "66d53add0ea3952e6079c6ad"
        }
        mock_response.json.return_value = response_dict
        type(mock_response).status_code = PropertyMock(return_value=200)
        mock_get.return_value = mock_response

        user_data = get_user_data('66d53add0ea3952e6079c6ad')

        mock_get.assert_called_with("http://127.0.0.1/user/66d53add0ea3952e6079c6ad")
        self.assertEqual(mock_response.status_code, 200)
        self.assertEqual(user_data, response_dict)

    @patch('requests.get')
    def test_request_fail_get_user(self, mock_get):
        mock_response = Mock()
        expected_response = {
            "error": "404 Not Found: The requested URL was not found on the server. If you entered the URL manually "
                     "please check your spelling and try again."
        }

        mock_response.json.return_value = expected_response
        type(mock_response).status_code = PropertyMock(return_value=404)
        mock_get.return_value = mock_response

        user_data = get_user_data()

        mock_get.assert_called_with("http://127.0.0.1/user/")
        self.assertEqual(mock_response.status_code, 404)
        self.assertEqual(user_data, expected_response)

    def test_success_create_user(self):
        user_data = self.get_user_data()
        expected_response = self.get_success_create_user_response()

        self.controller.user_repository.store.return_value = expected_response
        response = self.controller.create(user_data)

        self.controller.user_repository.store.assert_called_once_with(user_data)
        self.assertEqual(response, expected_response)

    def test_fail_create_user(self):
        user_data = {}
        expected_response = self.get_fail_create_user_response()

        self.controller.user_repository.store.return_value = expected_response
        response = self.controller.create(user_data)

        self.controller.user_repository.store.assert_called_once_with(user_data)
        self.assertEqual(response, expected_response)

    def get_user_data(self):
        return {
            "username": "asdsada",
            "password": "icf123",
            "email": "ola"
        }

    def get_success_create_user_response(self):
        return {
            "cellphone": "",
            "age": "",
            "birth_date": "",
            "username": "asdsada",
            "email": "ola",
            "_id": "66d78958929c926aaf82ee5d"
        }

    def get_fail_create_user_response(self):
        return {
            "username": {
                "required": True
            },
            "email": {
                "required": True
            },
            "password": {
                "required": True
        }
}

if __name__ == '__main__':
    unittest.main()