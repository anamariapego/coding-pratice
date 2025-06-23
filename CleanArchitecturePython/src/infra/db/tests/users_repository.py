from typing import List
from src.domain.models.users import Users

# Simular o comportamento do banco de dados em testes
class UsersRepositorySpy:

    # Mostrar quais são os atributos que foram chamados
    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.get_user_by_first_name_attributes = {}

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attributes["first_name"] = first_name
        self.insert_user_attributes["last_name"] = last_name
        self.insert_user_attributes["age"] = age


    def get_user_by_first_name(self, first_name: str) -> List[Users]:
        self.get_user_by_first_name_attributes["first_name"] = first_name
        return [
            Users(23, first_name, 'last', 43),
            Users(23, first_name, 'last_2', 12)
        ]
