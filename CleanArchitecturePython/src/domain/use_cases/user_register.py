from abc import ABC, abstractmethod
from typing import Dict
 
class UserRegisterInterface(ABC):
    """ 
    Interface para caso de uso de registro de usuário
    """
    @abstractmethod
    def register(self, name: str, email: str, age: int) -> Dict:
        """ 
        Registra um novo usuário

        Ags:
            name (str): Nome do usuário
            email (str): Email do usuário
            age (int): Idade do usuário

        Returns:    
            Dict: Dicionário com os dados formatados do usuário
        """
        pass
