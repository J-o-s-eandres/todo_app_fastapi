# app/models/task.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.db import Base  # asegúrate de importar tu Base declarativa

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)
    todo_list_id = Column(Integer, ForeignKey("todolists.id"))

    # Relación inversa hacia TodoList
    todolist = relationship("TodoList", back_populates="tasks")
