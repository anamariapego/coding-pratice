class HttpUnprocessableEntityError(Exception):
    """ 
    Exceção personalizada para representar erro 422
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422
