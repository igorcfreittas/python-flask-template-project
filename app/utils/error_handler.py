class ErrorHandler:
    def __init__(self, app):
        self.app = app
        self.handle()

    def handle(self):
        @self.app.errorhandler(400)
        def bad_request(error):
            return self.generic_error(error)

        @self.app.errorhandler(401)
        def unauthorized(error):
            return self.generic_error(error)

        @self.app.errorhandler(403)
        def forbidden(error):
            return self.generic_error(error)

        @self.app.errorhandler(404)
        def not_found(error):
            return self.generic_error(error)

    def generic_error(self, error):
        return {"error": str(error)}, getattr(error, "code", 500)
