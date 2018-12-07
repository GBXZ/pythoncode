from celery import Celery


app = Celery('send_email')
app.config_from_object('email_app.celeryconfig')