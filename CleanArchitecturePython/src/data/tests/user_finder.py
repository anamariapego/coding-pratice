from typing import Dict

class UserFinderSpy:
    """
    Classe espiã (spy) para simular o comportamento do UserFinder. 

    Usada em testes para verificar se o método 'find' foi chamado corretamente e para retornar uma resposta simulada sem depender de um banco de dados real. 
    """
    def __init__(self) -> None:
        self.find_attributes = {}

    def find(self, email: str) -> Dict:
        """
        Simula a busca de um usuário pelo email.

        Args:
            email (str): email do usuário a ser buscado.

        Returns:
            Dict: um dicionário com a resposta simulada.
        """
        self.find_attributes["email"] = email

        return {
            "type": "Users",
            "count": 1,
            "attributes": [
                { "name": "Ana", "email": email, "age": 20 }
            ]
        }
