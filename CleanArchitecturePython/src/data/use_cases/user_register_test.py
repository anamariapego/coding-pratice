from src.infra.db.tests.users_repository import UsersRepositorySpy
from src.data.use_cases.user_register import UserRegister


def test_register_user():
    """ 
    Teste de sucesso para o cadastro de um usuário.
    """
    name = "Usuario"
    email = "usuario@gmail"
    age = 34

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)
    response = user_register.register(name, email, age)

    assert repo.insert_user_attributes["name"] == name
    assert repo.insert_user_attributes["email"] == email
    assert repo.insert_user_attributes["age"] == age
    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributes"]

def test_register_email_error():
    """ 
    Teste de erro para o cadastro de um usuário com email inválido.
    """
    name = "Usuario"
    email = "usuario"
    age = 3

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    try:
        user_register.register(name, email, age)
        assert False
    except Exception as exception:
        assert str(exception) == "Email inválido para o cadastro"
