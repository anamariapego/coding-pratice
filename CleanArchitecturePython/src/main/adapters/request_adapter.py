from typing import Callable
from flask import request as FlaskRequest
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

def request_adapter(request: FlaskRequest, controller: Callable) -> HttpResponse:
    """
    Adapta a requisição do Flask para o formato esperado pelo controlador da camada de apresentação.

    Extrai os dados relevantes da requisição Flask e os empacota em um HttpRequest da aplicação,
    chamando em seguida o controlador correspondente.

    Ags: 
        request: Objeto de requisição do Flask
        controller: Função controladora que recebe um HttpRequest e retorna um HttpResponse
        
    Return: 
        Objeto HttpResponse contendo status code, headers e body
    """

    body = None
    if request.data: body = request.json

    # Cria o HttpRequest padronizado da aplicação
    http_request = HttpRequest(
        body=body,
        headers=request.headers,
        query_params=request.args,
        path_params=request.view_args,
        url=request.full_path
    )

    # Executa o controlador com a requisição adaptada
    http_response = controller(http_request)
    return http_response
