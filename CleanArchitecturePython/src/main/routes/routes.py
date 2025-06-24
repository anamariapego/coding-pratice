from flask import Blueprint, request, jsonify

# Import adapters
from src.main.adapters.request_adapter import request_adapter

# Import composers
from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_register_composer

# Import Validators
from src.main.validators.user_register_validator import user_register_validator
from src.main.validators.user_finder_validator import user_finder_validator

# Import error handlers
from src.main.errors.errors_handler import handle_errors

# Blueprint de rotas do usuário
user_route_bp = Blueprint("user_route_bp", __name__)

@user_route_bp.route("/user", methods=["POST"])
def register_user():
    """
    Endpoint POST /user
    Registra um novo usuário com nome, email e idade.
    """
    http_response = None

    try:
        user_register_validator(request) # Valida o corpo da requisição
        http_response = request_adapter(request, user_register_composer()) #Executa o controlador
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

@user_route_bp.route("/user/find", methods=["GET"])
def find_user():
    """
    Endpoint GET /user/find
    Busca usuários pelo primeiro nome (passado por query param).
    """
    http_response = None

    try:
        user_finder_validator(request) # Valida os parâmetros de entrada
        http_response = request_adapter(request, user_finder_composer()) #Executa o controlador
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code
