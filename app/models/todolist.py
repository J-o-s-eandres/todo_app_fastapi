from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.infrastructure.db.base import Base

class TodoList(Base):
    __tablename__ = "todolists"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)


    tasks = relationship("Task", back_populates="todolist", cascade="all, delete-orphan")
