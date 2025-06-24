from typing import List
from abc import ABC, abstractmethod
from src.domain.models.users import Users

class UsersRepositoryInterface(ABC):
    """
    Interface de repositório de usuários.

    Define os métodos que um repositório de usuários deve implementar.
    """
    @abstractmethod
    def insert_user(self, name: str, email: str, age: int) -> None: 
        """
        Insere um novo usuário no repositório.

        Args:
            name (str): none do usuário.
            email (str): email do usuário.
            age (int): idade do usuário.
        """
        pass
       
    @abstractmethod
    def get_user_by_email(self, email: str) -> List[Users]: 
        """
        Busca um usuário pelo email.
        Args:
            email (str): email do usuário.

        Returns:
            List[Users]: Lista de usuários encontrados.
        """
        pass
