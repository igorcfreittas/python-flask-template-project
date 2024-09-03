import os


class Settings:

    @staticmethod
    def get_mongodb() -> dict:
        return {
            'host': os.environ.get('MONGO_URL'),
            'name': os.environ.get('DB_NAME')
        }

    @staticmethod
    def get_server_settings() -> dict:
        return {
            'host': os.environ.get('APP_HOST'),
            'port': os.environ.get('APP_PORT'),
            'debug': Settings.is_development_env(),
            'passthrough_errors': Settings.is_development_env(),
        }

    @staticmethod
    def is_development_env() -> bool:
        return True if os.environ.get('FLASK_ENV') == 'development' else False
