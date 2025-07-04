class HttpBadRequestError(Exception):
    """ 
    Exceção personalizada para erros de requisição inválida.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "BadRequest"
        self.status_code = 400
