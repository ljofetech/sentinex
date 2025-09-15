# Self-hosted Uptime Monitor + Notifier

## Что это

    Лёгкий self-hosted сервис мониторинга доступности сайтов, API и сервисов.

## Почему полезно

    Многие используют UptimeRobot, но не хотят зависеть от внешнего сервиса.

## Фичи

    Добавление url для мониторинга. +
    Интервалы, пинг, логи.
    Уведомления: Telegram, Email, Slack.
    Графики и история доступности.
    Всё через Docker + Django Admin.

## Создать минимальную, но рабочую версию

    Можно добавить сайт/endpoint на мониторинг. +
    Проверки выполняются по расписанию.
    Результаты сохраняются.
    Есть простой web-интерфейс + API.
    Отправляются уведомления при падении.

## Архитектура и технологии

    Backend: Django
    Мониторинг задач: Celery + Redis
    База данных: PostgreSQL
    Web UI: Django templates (или Admin на первом этапе)
    Докеризация: Docker + Docker Compose
    Уведомления: Telegram (первый канал, затем Slack, Email)
    Периодичность: Celery periodic tasks (или custom scheduler)

```bash
class Endpoint(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    check_interval = models.IntegerField(default=5)  # в минутах
    last_checked = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    notify_on_failure = models.BooleanField(default=True)

class CheckLog(models.Model):
    endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)
    status_code = models.IntegerField()
    response_time = models.FloatField()
    is_up = models.BooleanField()
    checked_at = models.DateTimeField(auto_now_add=True)

class NotificationConfig(models.Model):
    endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)
    telegram_chat_id = models.CharField(max_length=100)
    telegram_token = models.CharField(max_length=200)
    # позже можно добавить email, slack и т.д.
```

## Основная логика (Core)

    1. Список endpoint'ов берётся из БД. +
    2. Для каждого запускается задача (Celery или scheduler).
    3. Делаем HTTP GET с timeout.
    4. Сохраняем CheckLog.
    5. Если сервис был доступен и стал недоступен → отправляем уведомление.
    6. Обратное — тоже уведомление.

```bash
@shared_task
def check_endpoint(endpoint_id):
    # Получить endpoint
    # Сделать запрос
    # Сохранить результат
    # Проверить статус → вызвать уведомление, если нужно

@periodic_task(run_every=crontab(minute="*/1"))
def schedule_checks():
    # Запускает задачи по расписанию для всех endpoint'ов

def send_telegram_notification(chat_id, token, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    requests.post(url, data=data)
```

## UI / API (Django Admin + Simple UI)

    Django Admin:
        для управления endpoint'ами и логами.
    Позже можно добавить:
        Страницу с графиками (response time).
        Отдельный frontend (например, React или HTMX).
