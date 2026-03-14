from celery import Celery

celery = Celery()

@celery.task
def send_email(email_data):
    # email sending logic