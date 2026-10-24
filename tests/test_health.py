"""Проверка базовых эндпоинтов."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["service"] == "api"


def test_version_reports_stage() -> None:
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json()["stage"] == "M0-bootstrap"
