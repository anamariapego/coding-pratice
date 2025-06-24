from src.data.use_cases.user_finder import UserFinder
from src.infra.db.tests.users_repository import UsersRepositorySpy

def test_find_user_success():
    """
    Teste de sucesso para a busca de um usuário.
    """
    email = "usuario@gmail.com"
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find_user(email)

    assert repo.get_user_by_email_attributes["email"] == email
    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []

def test_find_error_in_valid_email():
    """
    Testa se é levantado um erro ao passar email inválido.
    """
    email = "usuario"

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try: 
        user_finder.find_user(email)
        assert False # forcando falha
    except Exception as expection:
        assert str(expection) == "Email inválido para a busca"


def test_find_error_user_not_found():
    """
    Teste onde nenhum usuário é encontrado.
    """
    class UsersRepositoryError(UsersRepositorySpy):
        def get_user_by_email(self, email: str) -> None:
            return []
        
    email = "usuario@gmail.com"

    repo = UsersRepositoryError()
    user_finder = UserFinder(repo)

    try: 
        user_finder.find_user(email)
        assert False # forcando a falha
    except Exception as expection:
        assert str(expection) == "Usuário não encontrado"
