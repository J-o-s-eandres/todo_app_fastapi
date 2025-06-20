from pydantic import BaseModel
from enum import Enum
from typing import Optional

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: PriorityEnum = PriorityEnum.medium
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    priority: Optional[PriorityEnum]
    completed: Optional[bool]

class TaskOut(TaskBase):
    id: int
    list_id: int

    class Config:
        orm_mode = True
