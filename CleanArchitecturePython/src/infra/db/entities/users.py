from src.infra.db.settings.base import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import text

class Users(Base):
    """
    Classe que representa a tabela de usuários no banco de dados.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    # Para retornar uma representação legível do objeto
    def __repr__(self) -> str:
        return f"<User(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', age={self.age})>"
