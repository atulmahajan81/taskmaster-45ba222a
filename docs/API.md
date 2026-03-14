# TaskMaster API Reference

## Authentication

### Register a New User
- **Endpoint**: `POST /api/v1/auth/register`
- **Description**: Register a new user
- **Request**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "UUID",
    "email": "string"
  }
  ```

### Login a User
- **Endpoint**: `POST /api/v1/auth/login`
- **Description**: Login a user and return tokens
- **Request**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "string",
    "refresh_token": "string"
  }
  ```

## User Management

### Get Current User
- **Endpoint**: `GET /api/v1/users/me`
- **Description**: Get the current user's profile
- **Response**:
  ```json
  {
    "id": "UUID",
    "email": "string",
    "created_at": "TIMESTAMP"
  }
  ```

## Task Management

### Create a New Task
- **Endpoint**: `POST /api/v1/tasks`
- **Description**: Create a new task
- **Request**:
  ```json
  {
    "title": "string",
    "description": "string",
    "due_date": "DATE",
    "priority": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "UUID",
    "title": "string",
    "due_date": "DATE"
  }
  ```

### Retrieve All Tasks
- **Endpoint**: `GET /api/v1/tasks`
- **Description**: Retrieve all tasks for the current user
- **Response**:
  ```json
  {
    "tasks": [
      {
        "id": "UUID",
        "title": "string",
        "due_date": "DATE"
      }
    ]
  }
  ```