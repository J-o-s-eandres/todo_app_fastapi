from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.task import TaskCreate, TaskOut, TaskUpdate
from app.repositories.task import TaskRepository
from app.infrastructure.db import get_db

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=List[TaskOut])
def get_tasks(db: Session = Depends(get_db)):
    repo = TaskRepository(db)
    return repo.get_all()

@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    repo = TaskRepository(db)
    task = repo.get_by_id(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task_create: TaskCreate, db: Session = Depends(get_db)):
    repo = TaskRepository(db)
    return repo.create(task_create)

@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    repo = TaskRepository(db)
    task = repo.update(task_id, task_update)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    repo = TaskRepository(db)
    success = repo.delete(task_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return None
