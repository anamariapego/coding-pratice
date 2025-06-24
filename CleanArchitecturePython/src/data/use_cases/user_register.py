from typing import Dict
from src.errors.types import HttpBadRequestError
from src.domain.use_cases.user_register import UserRegisterInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface

class UserRegister(UserRegisterInterface):
    """
    Classe de uso responsável por registrar um usuário novo
    """
    
    def __init__(self, users_repo: UsersRepositoryInterface) -> None:
        self.__users_repo = users_repo

    def register(self, name: str, email: str, age: int) -> Dict:
        """
        Executa o fluxo completo de registro de um novo usuário:
        - Valida o email
        - Registra o usuário
        - Retorna uma resposta formatada

        Args:
            name (str): nome do usuário a ser registrado.
            email (str): email do usuário a ser registrado.
            age (int): idade do usuário a ser registrado.

        Returns:
            Dict: um dicionário com a resposta formatada.
        """
        self.__validate_email(email)
        self.__register_user_information(name, email, age)
        response = self.__format_reponse(name, email, age)
    
        return response
     
    @classmethod
    def __validate_email(cls, email: str) -> None:
        """
        Valida o formato do email.
        """
        if "@" not in email or "." not in email:
            raise HttpBadRequestError("Email inválido para o cadastro")

    def __register_user_information(self, name: str, email: str, age: int) -> None:
        """
        Registra o usuário no repositório.
        """
        self.__users_repo.insert_user(name, email, age)

    @classmethod
    def __format_reponse(cls, name: str, email: str, age: int) -> Dict:
        """
        Formata os dados do novo usuário registrado.
        """
        response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                "name": name,
                "email": email,
                "age": age
            }
        }
        return response
