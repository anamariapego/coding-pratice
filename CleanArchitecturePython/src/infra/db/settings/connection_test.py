import pytest
from src.infra.db.settings.connection import DBConnectionHandler
from sqlalchemy import text

# @pytest.mark.skip(reason="Sensive test") # Para não executar este teste automaticamente
def test_db_connection_handler():
    """
    Testa a criação da conexão com o banco de dados.
    """
    db_connection_handler = DBConnectionHandler()
    engine = db_connection_handler.get_engine()

    assert engine is not None, "A engine de conexão não foi criada corretamente."

def test_list_all_databases():
    """
    Testa a listagem de todos os bancos de dados disponíveis no PostgreSQL.
    """
    db_connection_handler = DBConnectionHandler()
    
    # 💡 Força o descarte de conexões antigas
    db_connection_handler.dispose_engine()
    
    engine = db_connection_handler.get_engine()

    with engine.connect() as connection:
        result = connection.execute(text("SELECT datname FROM pg_database WHERE datistemplate = false;"))
        databases = [row[0] for row in result.fetchall()]

    print("Bancos encontrados:", databases)

    assert len(databases) > 0, "Nenhum banco de dados foi encontrado."

