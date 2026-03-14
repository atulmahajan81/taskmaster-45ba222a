from sqlalchemy.orm import selectinload
from pydantic import EmailStr
from sqlalchemy import create_engine
from uuid import UUID
from .cache import redis_cache

engine = create_engine('database_url', pool_size=10, max_overflow=20, pool_timeout=30)

# Redis caching for user retrieval by email
def get_user_by_email(email: EmailStr):
    cached_user = redis_cache.get(f'user_email_{email}')
    if cached_user:
        return cached_user
    user = session.query(User).filter(User.email == email).one_or_none()
    if user:
        redis_cache.set(f'user_email_{email}', user, ex=300)
    return user

# Optimized query to avoid N+1
def get_tasks_by_user(user_id: UUID):
    tasks = session.query(Task).options(selectinload(Task.user)).filter(Task.user_id == user_id).all()
    return tasks

# Celery for background email sending
from celery import Celery
import os

celery_app = Celery('tasks', broker=os.environ['CELERY_BROKER_URL'])

@celery_app.task
def send_email_task(email_data):
    # Email sending logic

def send_email(email_data):
    send_email_task.delay(email_data)