# app/models/todolist.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base  # Tu clase base declarativa de SQLAlchemy

class TodoList(Base):
    __tablename__ = "todolists"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    # Relación uno a muchos con Task (suponiendo que Task tiene una columna todo_list_id)
    tasks = relationship("Task", back_populates="todolist", cascade="all, delete-orphan")
