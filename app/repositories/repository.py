from database.adapter import DatabaseAdapter


class Repository(DatabaseAdapter):

    def __init__(self, collection: str = ''):
        super().__init__(collection)
