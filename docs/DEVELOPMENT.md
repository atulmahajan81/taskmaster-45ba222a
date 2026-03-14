# TaskMaster Development Guide

## Local Development Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/taskmaster.git
   cd taskmaster
   ```

2. **Install Dependencies**:
   - **Backend**:
     ```bash
     cd backend
     pip install -r requirements.txt
     ```
   - **Frontend**:
     ```bash
     cd frontend
     npm install
     ```

3. **Run the Development Servers**:
   - **Backend**:
     ```bash
     uvicorn main:app --reload
     ```
   - **Frontend**:
     ```bash
     npm run dev
     ```

## Running Tests

- **Backend Tests**:
  ```bash
  cd backend
  pytest
  ```

- **Frontend Tests**:
  ```bash
  cd frontend
  npm run test
  ```

## Code Structure
- **Backend**: Organized by feature with FastAPI routers
- **Frontend**: Structured by pages and components

## Contributing Guide
- Fork the repository
- Create a new feature branch
- Commit your changes with meaningful messages
- Push the branch to your fork
- Open a pull request against `main`