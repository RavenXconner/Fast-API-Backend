from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None

class Task(TaskBase):
    id: int

    model_config = {
        "from_attributes": True
    }