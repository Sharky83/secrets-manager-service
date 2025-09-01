import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY", "changeme")
    DB_URL: str = os.getenv("DB_URL", "sqlite:///secrets.db")
    AUDIT_LOG_ENABLED: bool = True

settings = Settings()
