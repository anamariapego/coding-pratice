from .user_finder_validator import user_finder_validator
from src.errors.types import HttpUnprocessableEntityError

class MockRequest:
    def __init__(self) -> None:
        self.json = None
        self.args = {} 

def test_user_finder_validator_success():
    """
    Testa validação com parâmetro 'email' válido.
    """
    request = MockRequest()
    request.args = {"email": "usuario@gmail.com"}

    try:
        user_finder_validator(request)
    except Exception as e:
        assert False, f"Validador lançou exceção inesperada: {e}"

def test_user_finder_validator_failure():
    """
    Testa validação com parâmetro 'email' faltando.
    """
    request = MockRequest()
    request.args = {}  # email ausente

    try:
        user_finder_validator(request)
        assert False, "Esperava exceção mas nenhuma foi lançada."
    except HttpUnprocessableEntityError as e:
        # Aqui você pode fazer asserts mais específicos na mensagem, se quiser
        assert "email" in str(e.message) or "email" in str(e)
