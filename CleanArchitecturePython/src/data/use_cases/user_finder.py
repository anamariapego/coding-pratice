from typing import Dict, List
from src.domain.models.users import Users
from src.errors.types import HttpNotFoundError, HttpBadRequestError
from src.domain.use_cases.user_finder import UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface

class UserFinder(UserFinderInterface):
    """
    Caso de uso que busca um usuário no repositório, aplicando validações e formatação de resposta.
    """
    def __init__(self, users_repo: UsersRepositoryInterface) -> None:
        self.__users_repo = users_repo

    def find_user(self, email: str) -> Dict:
        """
        Executa o fluxo completo de busca de um usuário:
        - Valida o email
        - Busca o usuário
        - Formata a resposta

        Args:
            email (str): email do usuário a ser buscado.

        Returns:
            Dict: um dicionário com a resposta formatada.
        """
        # Código refatorado
        self.__validate_email(email)
        users = self.__seacher_user(email)
        response = self.__format_reponse(users)
        return response

# obs: mesmo quando houver refatoramento no código os testes não devem quebrar

    @classmethod
    def __validate_email(cls, email: str) -> None:
        """
        Valida o formato do email.
        """
        if "@" not in email or "." not in email:
            raise HttpBadRequestError("Email inválido para a busca")
        
    def __seacher_user(self, email: str) -> List[Users]:
        """
        Busca o usuário no repositório.
        """
        user = self.__users_repo.get_user_by_email(email)
        if user == []:
            raise HttpNotFoundError("Usuário não encontrado")
        return user
    
    @classmethod
    def __format_reponse(cls, users: List[Users]) -> Dict:
        """
        Formata os dados dos usuários em um dicionário.
        """
        attributes = []
        for user in users:
            attributes.append({
                "name": user.name,
                "email": user.email,
                "age": user.age
            })

        response = {
            "type": "Users",
            "count": len(users),
            "attributes": attributes
        }
        return response
