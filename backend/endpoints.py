from fastapi import Depends
from app.auth import get_current_user
from app.rate_limit import rate_limit

@auth_required
@rate_limit(limit=100, duration=60)
def list_tasks(offset: int = 0, limit: int = 50, current_user: User = Depends(get_current_user)):
    # Ensure current_user is authenticated
    tasks = session.query(Task).offset(offset).limit(limit).all()
    return tasks