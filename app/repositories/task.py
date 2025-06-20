# app/models/task.py
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.infrastructure.db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)
    todo_list_id = Column(Integer, ForeignKey("todolists.id"))

    todolist = relationship("TodoList", back_populates="tasks")
