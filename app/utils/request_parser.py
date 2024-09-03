class RequestParser:
    """
        Is possible to use reqparse instead, if you want,
        do not import this class on routes/*_resources
        import:
            from flask_restful import reqparse
    """

    @staticmethod
    def get(request: dict, fields: dict) -> dict:
        errors: dict = {'errors': {}}
        response: dict = {}

        for key, value in fields.items():
            key_is_on_request = key in request

            if not value['required'] and not key_is_on_request:
                response[key] = ''
                continue

            if value['required'] and not key_is_on_request:
                errors['errors'][key] = {'required': True}
                continue

            is_valid_type = isinstance(request[key], value['type'])
            if value['required'] and not is_valid_type:
                errors['errors'][key] = {'type': str(value['type'])}

        if bool(errors['errors']):
            return errors

        for key, value in request.items():
            response[key] = request.get(key, '')

        return response
