from flask import Flask
from flask_restful import Api
from config.environment import Settings
from app.routes.api import Router
from app.utils.error_handler import ErrorHandler

app = Flask(__name__)
api = Api(app)

ErrorHandler(app)
Router(api)

if __name__ == '__main__':
    app.run(**Settings.get_server_settings())
