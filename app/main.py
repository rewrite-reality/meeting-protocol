"""Точка входа FastAPI-приложения."""

from fastapi import FastAPI

from app.config import settings

app = FastAPI(
    title="Meeting Protocol Service",
    description="Автоматическая расшифровка, диаризация и протоколирование производственных совещаний",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    """Проверка работоспособности сервиса."""
    return {"status": "ok", "service": "api", "env": settings.app_env}


@app.get("/version")
def version() -> dict[str, str]:
    """Версия API и этап разработки."""
    return {"version": app.version, "stage": "M0-bootstrap"}
