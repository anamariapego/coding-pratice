from src.presentation.controllers.user_register_controller import UserRegisterController
from src.data.tests.user_register import UserRegisterSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self) -> None:
        self.body = { "name": "Usuario", "email": "usuario@gmail.com", "age": 38 }

def test_handle():
    """
    Testa o método handle do UserRegisterController com sucesso.
    Usa um caso de uso espião (UserRegisterSpy) e um HttpRequest simulado.
    """
    http_request_mock = HttpRequestMock()
    use_case = UserRegisterSpy() # Simula a lógica do caso de uso
    user_finder_controller = UserRegisterController(use_case)

    response = user_finder_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
