from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError

def user_register_validator(request: any):
    """
    Valida o corpo da requisição para o registro de usuário..
    """
    body_validator = Validator({
        "name": { "type": "string", "required": True, "empty": False },
        "email": { "type": "string", "required": True, "empty": False },
        "age": { "type": "integer", "required": True, "empty": False }
    })
    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
