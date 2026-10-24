"""Celery-приложение: очередь задач обработки аудио."""

from celery import Celery

from app.config import settings

celery_app = Celery("meeting_protocol", broker=settings.redis_url, backend=settings.redis_url)
celery_app.conf.task_track_started = True


@celery_app.task(name="worker.ping")
def ping() -> str:
    """Проверка, что воркер поднялся и видит брокер."""
    return "pong"
