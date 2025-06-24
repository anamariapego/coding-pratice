from src.infra.db.settings.base import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import text

class Users(Base):
    """
    Modelo que representa a tabela 'users' no banco de dados.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    age = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    
    def __repr__(self) -> str:
        """ 
        Representação legível do objeto
        """
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}', age={self.age})>"
