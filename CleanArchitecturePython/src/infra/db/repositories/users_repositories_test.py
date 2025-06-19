from src.infra.db.repositories.users_repositories import UsersRepositories
from src.infra.db.settings.connection import DBConnectionHandler
from sqlalchemy import text
import pytest

# ---------- FIXTURES ----------

@pytest.fixture
def db_engine():
    handler = DBConnectionHandler()
    engine = handler.get_engine()
    yield engine  # disponibiliza para os testes
    engine.dispose()  # encerra conexões ao final


@pytest.fixture
def db_connection(db_engine):
    with db_engine.connect() as connection:
        yield connection


# ---------- TESTES ----------

@pytest.mark.skip(reason="Sensive test")
def test_insert_user(db_connection):
    """
    Testa o método insert_user da classe UsersRepositories.
    """
    mocked_first_name = "Camila"
    mocked_last_name = "Torres"
    mocked_age = 12

    # Executa o insert via repositório
    UsersRepositories.insert_user(mocked_first_name, mocked_last_name, mocked_age)

    # Validação
    sql = text("""
        SELECT * FROM users
        WHERE first_name = :first_name AND last_name = :last_name AND age = :age
    """)
    result = db_connection.execute(sql, {
        "first_name": mocked_first_name,
        "last_name": mocked_last_name,
        "age": mocked_age
    })
    registry = result.fetchone()

    assert registry is not None
    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

    # Limpeza
    db_connection.execute(
        text("DELETE FROM users WHERE id = :id"), {"id": registry.id}
    )
    db_connection.commit()

@pytest.mark.skip(reason="Sensive test")
def test_get_all_users(db_connection):
    """
    Testa o método get_all_users da classe UsersRepositories.
    """
    mocked_first_name = "Antonio"
    mocked_last_name = "Globo"
    mocked_age = 12

    insert_sql = text("""
        INSERT INTO users (first_name, last_name, age)
        VALUES (:first_name, :last_name, :age)
    """)
    db_connection.execute(insert_sql, {
        "first_name": mocked_first_name,
        "last_name": mocked_last_name,
        "age": mocked_age
    })
    db_connection.commit()

    users_repo = UsersRepositories()
    users = users_repo.get_all_users()

    assert users is not None
    assert any(user.first_name == mocked_first_name for user in users)

    # Limpeza
    user_to_delete = next(u for u in users if u.first_name == mocked_first_name)
    db_connection.execute(
        text("DELETE FROM users WHERE id = :id"), {"id": user_to_delete.id}
    )
    db_connection.commit()

@pytest.mark.skip(reason="Sensive test")
def test_get_user_by_first_name(db_connection):
    """
    Testa o método get_user_by_first_name da classe UsersRepositories.
    """
    mocked_first_name = "Antonio"
    mocked_last_name = "Globo"
    mocked_age = 12

    insert_sql = text("""
        INSERT INTO users (first_name, last_name, age)
        VALUES (:first_name, :last_name, :age)
    """)
    db_connection.execute(insert_sql, {
        "first_name": mocked_first_name,
        "last_name": mocked_last_name,
        "age": mocked_age
    })
    db_connection.commit()

    users_repo = UsersRepositories()
    user = users_repo.get_user_by_first_name(mocked_first_name)

    assert user is not None
    assert user.first_name == mocked_first_name

    db_connection.execute(
        text("DELETE FROM users WHERE id = :id"), {"id": user.id}
    )
    db_connection.commit()

@pytest.mark.skip(reason="Sensive test")
def test_update_user(db_connection):
    """
    Testa o método update_user da classe UsersRepositories.
    """
    mocked_first_name = "Antonio"
    mocked_last_name = "Globo"
    mocked_age = 12

    insert_sql = text("""
        INSERT INTO users (first_name, last_name, age)
        VALUES (:first_name, :last_name, :age)
        RETURNING id
    """)
    result = db_connection.execute(insert_sql, {
        "first_name": mocked_first_name,
        "last_name": mocked_last_name,
        "age": mocked_age
    })
    user_id = result.fetchone().id
    db_connection.commit()

    new_first_name = "Antonio"
    new_last_name = "Silva"
    new_age = 15

    UsersRepositories.update_user(user_id, new_first_name, new_last_name, new_age)

    updated_user = db_connection.execute(
        text("SELECT * FROM users WHERE id = :id"), {"id": user_id}
    ).fetchone()

    assert updated_user is not None
    assert updated_user.first_name == new_first_name
    assert updated_user.last_name == new_last_name
    assert updated_user.age == new_age

    # Limpeza
    db_connection.execute(
        text("DELETE FROM users WHERE id = :id"), {"id": user_id}
    )
    db_connection.commit()

def test_delete_user(db_connection):
    """
    Testa o método delete_user da classe UsersRepositories.
    """
    mocked_first_name = "Antonio"
    mocked_last_name = "Globo"
    mocked_age = 12

    insert_sql = text("""
        INSERT INTO users (first_name, last_name, age)
        VALUES (:first_name, :last_name, :age)
        RETURNING id
    """)
    result = db_connection.execute(insert_sql, {
        "first_name": mocked_first_name,
        "last_name": mocked_last_name,
        "age": mocked_age
    })
    user_id = result.fetchone().id
    db_connection.commit()

    UsersRepositories.delete_user(user_id)

    deleted_user = db_connection.execute(
        text("SELECT * FROM users WHERE id = :id"), {"id": user_id}
    ).fetchone()

    assert deleted_user is None