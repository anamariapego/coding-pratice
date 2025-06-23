from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Database configuration
    db_name: str
    db_port: int
    db_host: str
    db_username: str
    db_password: str

    model_config = SettingsConfigDict(env_file=".env")

# Cria a instância de configurações
settings = Settings()
