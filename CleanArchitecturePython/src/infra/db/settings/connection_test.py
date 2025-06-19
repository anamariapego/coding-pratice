import pytest
from src.infra.db.settings.connection import DBConnectionHandler

@pytest.mark.skip(reason="Sensive test") # Para não executar este teste automaticamente
def test_db_connection_handler():
    """
    Testa a criação da conexão com o banco de dados.
    """
    db_connection_handler = DBConnectionHandler()
    engine = db_connection_handler.get_engine()

    assert engine is not None, "A engine de conexão não foi criada corretamente."
