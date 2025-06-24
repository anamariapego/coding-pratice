from typing import Dict

class UserRegisterSpy:
    """
    Classe espiã (spy) para simular o comportamento do UserRegister.

    Usada em testes para verificar se o método 'register' foi chamado corretamente e para retornar uma resposta simulada sem depender de um banco de dados real.
    """
    def __init__(self) -> None:
        self.find_attributes = {}

    def register(self, name: str, email: str, age: int) -> Dict:
        """
        Simula o registro de um usuário.

        Args:
            name (str): nome do usuário a ser registrado.
            email (str): email do usuário a ser registrado.
            age (int): idade do usuário a ser registrado.

        Returns:
            Dict: um dicionário com a resposta simulada.
        """
        self.find_attributes["name"] = name
        self.find_attributes["email"] = email
        self.find_attributes["age"] = age

        return {
            "type": "Users",
            "count": 1,
            "attributes": [
                {"name": name, "email": email, "age": age}
            ]
        }
