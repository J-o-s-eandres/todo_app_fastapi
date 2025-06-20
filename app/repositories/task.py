# app/repositories/task.py
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Task]:
        return self.db.query(Task).all()

    def get_by_id(self, task_id: int) -> Optional[Task]:
        return self.db.query(Task).filter(Task.id == task_id).first()

    def create(self, task_create: TaskCreate) -> Task:
        db_task = Task(**task_create.dict())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def update(self, task_id: int, task_update: TaskUpdate) -> Optional[Task]:
        db_task = self.get_by_id(task_id)
        if not db_task:
            return None
        update_data = task_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_task, key, value)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def delete(self, task_id: int) -> bool:
        db_task = self.get_by_id(task_id)
        if not db_task:
            return False
        self.db.delete(db_task)
        self.db.commit()
        return True
