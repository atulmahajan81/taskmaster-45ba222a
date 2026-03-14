from sqlalchemy import create_engine
import os

DATABASE_URL = os.environ['DATABASE_URL']

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=10, pool_timeout=30)