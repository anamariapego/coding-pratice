from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError

def user_finder_validator(request: any):
    """
    Valida os parâmetros da query string da requisição para busca de usuário.
    """
    query_validator = Validator({
        "email": { "type": "string", "required": True, "empty": False }
    })
    response = query_validator.validate(request.args)

    if response is False:
        raise HttpUnprocessableEntityError(query_validator.errors)
