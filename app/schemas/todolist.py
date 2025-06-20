from pydantic import BaseModel
from typing import Optional, List
from app.schemas.task import TaskOut

class TodoListBase(BaseModel):
    title: str
    description: Optional[str] = None

class TodoListCreate(TodoListBase):
    pass

class TodoListUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]

class TodoListOut(TodoListBase):
    id: int
    tasks: List[TaskOut] = []

    class Config:
        orm_mode = True
