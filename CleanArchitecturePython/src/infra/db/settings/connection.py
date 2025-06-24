from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.config import settings

# Quando usa container o valor de host vai mudar, usando o endereço do IP do banco de dados
class DBConnectionHandler:

    def __init__(self) -> None:

        self.__connection_string = f"postgresql+psycopg2://{settings.db_username}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self) -> "create_engine":
        """
        Método para criar a engine de conexão com o banco de dados.
        """
        engine = create_engine(self.__connection_string, echo=True, future=True, # echo=True para logar as queries SQL e future=True para usar a API futura do SQLAlchemy
                               pool_pre_ping=True)  # importante para evitar conexões mortas
        return engine
    
    def get_engine(self) -> None:
        """
        Método para obter a engine de conexão com o banco de dados.
        """
        return self.__engine
    
    def dispose_engine(self):
        self.__engine.dispose()
    
    def __enter__(self) -> "DBConnectionHandler":
        """
        Método para entrar no contexto do gerenciador de contexto.
        """
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
 
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """
        Método para sair do contexto do gerenciador de contexto.
        """
        if self.session:
            self.session.close()
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")
