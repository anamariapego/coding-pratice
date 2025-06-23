#pylint: disable=broad-exception-raised

from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from typing import Dict, List
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users

# Validações que acontecem antes da lógica, antes de realmente buscar o usuário
class UserFinder(UserFinderInterface):
    def __init__(self, users_repo: UsersRepositoryInterface) -> None:
        self.__users_repo = users_repo

    def find_user(self, first_name: str) -> Dict:

        # # lógica
        # if not first_name.isalpha():
        #     raise Exception("Nome inválido para a busca")
        
        # user = self.__users_repo.get_user_by_first_name(first_name)
        # if user == []:
        #     raise Exception("Usuário não encontrado")
        
        # response = {
        #     "type": "Users",
        #     "count": len(user),
        #     "attributes": user
        # }
        # return response

        # Código refatorado
        self.__validate_name(first_name)
        users = self.__seacher_user(first_name)
        response = self.__format_reponse(users)
        return response

# Mesmo quando houver refatoramento no código os testes não devem quebrar

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise Exception("Nome inválido para a busca")
        
    def __seacher_user(self, first_name: str) -> None:
        user = self.__users_repo.get_user_by_first_name(first_name)
        if user == []:
            raise Exception("Usuário não encontrado")
        return user
    
    @classmethod
    def __format_reponse(cls, users: List[Users]) -> Dict:
        attributes = []
        for user in users:
            attributes.append({
                "last_name": user.last_name,
                "age": user.age
            })


        response = {
            "type": "Users",
            "count": len(users),
            "attributes": attributes
        }
        return response

# first_name contendo apenas letras
# retornar erro caso não encontre usuário
# formatar a resposta