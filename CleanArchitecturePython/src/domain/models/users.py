"""
Classe que representa a entidade de usuário no domínio da aplicação.

Utilizada para abstrair a estrutura de dados do usuário independentemente da tecnologia usada (banco, API etc.).
"""

class Users:
    def __init__(self, name: str, email: str, age: int) -> None:
        """
        Inicializa uma nova instância de usuário.

        Ags:
            name (str): Nome do usuário
            email (str): Email do usuário
            age (int): Idade do usuário
        """
        self.name = name
        self.email = email
        self.age = age

    def __repr__(self) -> str:
        return f"Users(name='{self.name}', email='{self.email}', age={self.age})"
