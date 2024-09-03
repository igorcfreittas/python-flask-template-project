class AuthMiddleware:

    def authentitcate(self, params: dict = {}):
        """
            Tip: Recovering GET or POST data
            If you use request.get_json() to GET method, an error will raise
            req = params if request.method == 'GET' else request.get_json()
        """
        pass


def auth(func):
    def wrapper(*args, **kwargs):
        AuthMiddleware().authentitcate(kwargs)
        return func(*args, **kwargs)
    return wrapper
