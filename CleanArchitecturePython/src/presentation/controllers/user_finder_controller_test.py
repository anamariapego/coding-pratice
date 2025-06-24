from src.presentation.controllers.user_finder_controller import UserFinderController
from src.data.tests.user_finder import UserFinderSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = { "email": "usuario@gmail.com" }

def test_handle():
    """
    Testa o método handle do UserFinderController com sucesso.
    Usa um caso de uso espião (UserFinderSpy) e um HttpRequest simulado.
    """
    http_request_mock = HttpRequestMock()
    use_case = UserFinderSpy() # Simula a lógica do caso de uso
    user_finder_controller = UserFinderController(use_case)

    response = user_finder_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
