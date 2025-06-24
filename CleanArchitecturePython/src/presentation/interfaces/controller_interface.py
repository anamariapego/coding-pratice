from abc import ABC, abstractmethod
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class ControllerInterface(ABC):
    """
    Interface para controllers, definindo o método obrigatório handle.
    """
    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse: pass
