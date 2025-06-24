from typing import Dict
from abc import ABC, abstractmethod

class UserFinderInterface(ABC):
    """
    Interface para o caso de uso de busca de usuários.
    """
    @abstractmethod
    def find_user(self, email: str) -> Dict:
        """
        Executa a busca por usuários a partir do primeiro nome.

        Ags:
            email (str): Email do usuário a ser buscado

        Returns:
            Dict: Dicionário com os dados formatados do usuário.
        """
        pass
