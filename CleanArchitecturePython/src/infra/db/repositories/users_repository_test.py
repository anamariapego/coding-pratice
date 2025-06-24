from src.infra.db.repositories.users_repository import UsersRepositories
from src.infra.db.settings.connection import DBConnectionHandler
from sqlalchemy import text
import pytest

# ---------- FIXTURES ----------

@pytest.fixture
def db_engine():
    """
    Fixture que fornece o engine de conexão com o banco de dados.
    """
    handler = DBConnectionHandler()
    engine = handler.get_engine()
    yield engine  # Disponibiliza o engine para o teste
    engine.dispose()  # Fecha conexões após o teste


@pytest.fixture
def db_connection(db_engine):
    """
    Fixture que fornece uma conexão ativa com o banco de dados.
    """
    with db_engine.connect() as connection:
        yield connection

# ---------- TESTES ----------

@pytest.mark.skip(reason="Sensive test")
def test_insert_user(db_connection):
    """
    Testa o método insert_user da classe UsersRepositories. E Valida se o usuário foi inserido corretamente.
    """
    mocked_name = "usuario"
    mocked_email = "usuario@gmail.com"
    mocked_age = 12

    # Executa o insert via repositório
    UsersRepositories.insert_user(mocked_name, mocked_email, mocked_age)

    # Valida se o usuário foi inserido corretamente
    sql = text("""
        SELECT * FROM users
        WHERE name = :name AND email = :email AND age = :age
    """)
    result = db_connection.execute(sql, {
        "name": mocked_name,
        "email": mocked_email,
        "age": mocked_age
    })
    registry = result.fetchone()

    assert registry is not None
    assert registry.name == mocked_name
    assert registry.email == mocked_email
    assert registry.age == mocked_age

    # Limpeza do banco após o teste
    db_connection.execute(
        text("DELETE FROM users WHERE id = :id"), {"id": registry.id}
    )
    db_connection.commit()


@pytest.mark.skip(reason="Sensive test")
def test_get_user_email(db_connection):
    """
    Testa o método get_user_by_email da classe UsersRepositories. E Valida se o usuário foi obtido corretamente.
    """
    mocked_name = "usuario"
    mocked_email = "usuario@gmail.com"
    mocked_age = 12

    insert_sql = text("""
        INSERT INTO users (name, email, age)
        VALUES (:name, :email, :age)
    """)
    db_connection.execute(insert_sql, {
        "name": mocked_name,
        "email": mocked_email,
        "age": mocked_age
    })
    db_connection.commit()

    # Execução da função a ser testada
    users_repo = UsersRepositories()
    user = users_repo.get_user_by_email(mocked_email)

    assert user is not None
    assert user.email == mocked_email

    # Limpeza do banco após o teste
    db_connection.execute(
        text("DELETE FROM users WHERE id = :id"), {"id": user.id}
    )
    db_connection.commit()
