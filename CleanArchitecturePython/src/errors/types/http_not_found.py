class HttpNotFoundError(Exception):
    """ 
    Exceção personalizada para indicar que um recurso não foi encontrado.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "NotFound"
        self.status_code = 404
