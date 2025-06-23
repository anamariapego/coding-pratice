from src.data.use_cases.user_finder import UserFinder
from src.infra.db.tests.users_repository import UsersRepositorySpy

def test_find_user():
    first_name = "Ana"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find_user(first_name)

    assert repo.get_user_by_first_name_attributes["first_name"] == first_name

    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []

def test_find_error_in_valid_name():
    first_name = "Ana123"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try: 
        user_finder.find_user(first_name)
        assert False # forcando falha
    except Exception as expection:
        assert str(expection) == "Nome inválido para a busca"


def test_find_error_user_not_found():

    # Classe que armazena os dados, reprsesentação do que tem na tabela users
    class UsersRepositoryError(UsersRepositorySpy):
        def get_user_by_first_name(self, first_name: str) -> None:
            return []
        
    first_name = "Ana"

    repo = UsersRepositoryError()
    user_finder = UserFinder(repo)

    try: 
        user_finder.find_user(first_name)
        assert False # forcando falha
    except Exception as expection:
        assert str(expection) == "Usuário não encontrado"
