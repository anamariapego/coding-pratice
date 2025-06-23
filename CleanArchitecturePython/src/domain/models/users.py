#pylint: disable=redefined-builtin

# Classe que armazena os dados, reprsesentação do que tem na tabela users
class Users:
    def __init__(self, id: int, first_name: str, last_name: str, age: int) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
