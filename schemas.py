from pydantic import BaseModel

class TaskBase(BaseModel):
    text: str
    completed: bool = False

class TaskCreate(BaseModel):
    text: str  # ✅ matches frontend POST payload

class TaskUpdate(BaseModel):
    text: str | None = None
    completed: bool | None = None

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True  # ✅ enables SQLAlchemy -> Pydantic model parsing
