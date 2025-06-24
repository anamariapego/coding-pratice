from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.user_finder import  UserFinderInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class UserFinderController(ControllerInterface):
    """
    Controller responsável por orquestrar a busca de usuários.

    Recebe a requisição HTTP, extrai os parâmetros necessários,
    executa o caso de uso e retorna a resposta HTTP formatada.
    """
    def __init__(self, use_case: UserFinderInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.query_params["first_name"]

        response = self.__use_case.find(first_name)

        return HttpResponse(
            status_code=200,
            body={ "data": response }
        )
