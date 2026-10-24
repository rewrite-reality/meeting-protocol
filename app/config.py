"""Конфигурация приложения из переменных окружения."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "local"
    api_port: int = 8000
    database_url: str = "postgresql+psycopg://meetings:change_me@localhost:5432/meetings"
    redis_url: str = "redis://localhost:6379/0"
    minio_endpoint: str = "localhost:9000"
    minio_bucket: str = "meetings-audio"


settings = Settings()
