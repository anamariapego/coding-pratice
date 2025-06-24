from typing import List
from src.domain.models.users import Users

class UsersRepositorySpy:
    """
    Repositório espião (spy) de usuários. Simula os métodos insert_user e get_user_by_email para testes unitários.
    """

    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.get_user_by_email_attributes = {}

    def insert_user(self, name: str, email: str, age: int) -> None:
        self.insert_user_attributes["name"] = name
        self.insert_user_attributes["email"] = email
        self.insert_user_attributes["age"] = age


    def get_user_by_email(self, email: str) -> List[Users]:
        self.get_user_by_email_attributes["email"] = email
        return [
            Users("usuário", email, 43),
            Users("usuario2", email, 12)
        ]
