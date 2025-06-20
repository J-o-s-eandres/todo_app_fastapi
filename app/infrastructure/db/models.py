from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship, declarative_base
import enum

Base = declarative_base()

class PriorityEnum(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TodoList(Base):
    __tablename__ = "todo_lists"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    tasks = relationship("Task", back_populates="todo_list", cascade="all, delete")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    priority = Column(Enum(PriorityEnum), default=PriorityEnum.medium)

    list_id = Column(Integer, ForeignKey("todo_lists.id"))
    todo_list = relationship("TodoList", back_populates="tasks")
