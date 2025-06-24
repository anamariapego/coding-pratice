"""
Arquivo de configurações da aplicação.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Classe que representa as configurações do projeto. As variáveis são carregadas automaticamente do arquivo .env
    """
    # Configurações do banco de dados
    db_name: str
    db_port: int
    db_host: str
    db_username: str
    db_password: str

    model_config = SettingsConfigDict(env_file=".env")

# Cria a instância da classe
settings = Settings()
