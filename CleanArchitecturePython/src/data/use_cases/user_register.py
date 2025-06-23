#pylint: disable=broad-exception-raised

from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from typing import Dict

# Implementando a interface
class UserRegister(UserRegisterInterface):
    
    def __init__(self, users_repo: UsersRepositoryInterface) -> None:
        self.__users_repo = users_repo

    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        self.__validate_name(first_name)
        self.__validate_name(last_name)

        self.__register_user_information(first_name, last_name, age)
        response = self.__format_reponse(first_name, last_name, age)
        return response
     
    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise Exception("Nome invalido para o cadastro")

    def __register_user_information(self, first_name: str, last_name: str, age: int) -> None:
        self.__users_repo.insert_user(first_name, last_name, age)

    @classmethod
    def __format_reponse(cls, first_name: str, last_name: str, age: int) -> Dict:
        response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age
            }
        }
        return response
