# TaskMaster Database Documentation

## Schema Overview

TaskMaster uses a PostgreSQL database to store user and task information. The database schema is managed using SQLAlchemy and migrations are handled by Alembic.

## Entity Relationships

- **User**: Stores user credentials and profiles.
- **Task**: Contains task details, status, and metadata.

## Migration Guide

Alembic is used for database migrations. To create a new migration script:

1. **Generate a Migration**:
   ```bash
   alembic revision --autogenerate -m "Migration message"
   ```

2. **Apply Migrations**:
   ```bash
   alembic upgrade head
   ```