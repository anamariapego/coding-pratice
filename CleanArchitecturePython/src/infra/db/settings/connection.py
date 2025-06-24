from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.config import settings

class DBConnectionHandler:
    """
    Gerenciador de contexto para conexão com banco de dados usando SQLAlchemy.

    Cria engine, gerencia sessão e garante fechamento adequado da conexão.
    """

    def __init__(self) -> None:
        # String de conexão para PostgreSQL usando psycopg2
        self.__connection_string = f"postgresql+psycopg2://{settings.db_username}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self) -> "create_engine":
        """
        Cria o engine do SQLAlchemy com configuração para log e conexão saudável.
        """
        engine = create_engine(
            self.__connection_string,
            echo=True,        # Loga as queries SQL para facilitar debugging
            future=True,      # Usa a API futura do SQLAlchemy
            pool_pre_ping=True  # Verifica conexões antes de usar para evitar erros de conexão morta
        )
        return engine
    
    def get_engine(self) -> None:
        """
        Retorna a engine para uso direto.
        """
        return self.__engine
    
    def dispose_engine(self):
        """
        Encerra a engine (fechamento de conexões).
        """
        self.__engine.dispose()
    
    def __enter__(self) -> "DBConnectionHandler":
        """
        Inicia o contexto, cria e retorna a sessão.
        """
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
 
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """
         Fecha a sessão ao sair do contexto.
        """
        if self.session:
            self.session.close()
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")
