from pydantic import BaseModel

# Base model with consistent naming for both frontend and backend
class TaskBase(BaseModel):
    text: str
    completed: bool = False

# For POST /api/tasks/
class TaskCreate(BaseModel):
    text: str  # Only `text` is expected on creation

# For PATCH / PUT updates
class TaskUpdate(BaseModel):
    text: str | None = None
    completed: bool | None = None

# Final Task schema returned by the API
class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True  # Enables ORM mode for SQLAlchemy compatibility
