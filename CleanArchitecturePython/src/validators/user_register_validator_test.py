from .user_register_validator import user_register_validator
from src.errors.types import HttpUnprocessableEntityError

class MockRequest:
    def __init__(self) -> None:
        self.json = None

def test_user_register_validator_success():
    """
    Testa validação com dados válidos.
    """
    request = MockRequest()
    request.json = {
        "name": "Usuario",
        "email": "usuario@gmail.com",
        "age": 23
    }

    try:
        user_register_validator(request)
    except Exception as e:
        assert False, f"Validador lançou exceção inesperada: {e}"

def test_user_register_validator_failure():
    """
    Testa validação com dados inválidos.
    """
    request = MockRequest()
    request.json = {
        "name": "",
        "email": "invalid-email",
        # "age" faltando para testar o required
    }

    try:
        user_register_validator(request)
        assert False, "Esperava exceção mas nenhuma foi lançada."
    except HttpUnprocessableEntityError as e:
        assert "name" in str(e.message)
        assert "email" in str(e.message)
        assert "age" in str(e.message)
