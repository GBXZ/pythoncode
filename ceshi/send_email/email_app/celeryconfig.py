from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TIMEZONE = 'Asia/Shanghai'  # 一定要指定时区

CELERY_IMPORTS = (
        'email_app.task'
)

CELERYBEAT_SCHEDULE = {
        'task': {
                'task': 'email_app.task.sendemail',
                'schedule': timedelta(seconds=10),
},
}
