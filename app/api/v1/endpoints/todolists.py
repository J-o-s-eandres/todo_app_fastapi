from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.todolist import TodoListCreate, TodoListOut, TodoListUpdate
from app.repositories.todolist import TodoListRepository
from app.infrastructure.db import get_db

router = APIRouter(prefix="/todolists", tags=["todolists"])

@router.get("/", response_model=List[TodoListOut])
def get_todolists(db: Session = Depends(get_db)):
    repo = TodoListRepository(db)
    return repo.get_all()

@router.get("/{todo_list_id}", response_model=TodoListOut)
def get_todolist(todo_list_id: int, db: Session = Depends(get_db)):
    repo = TodoListRepository(db)
    todolist = repo.get_by_id(todo_list_id)
    if not todolist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TodoList not found")
    return todolist

@router.post("/", response_model=TodoListOut, status_code=status.HTTP_201_CREATED)
def create_todolist(todolist_create: TodoListCreate, db: Session = Depends(get_db)):
    repo = TodoListRepository(db)
    return repo.create(todolist_create)

@router.put("/{todo_list_id}", response_model=TodoListOut)
def update_todolist(todo_list_id: int, todolist_update: TodoListUpdate, db: Session = Depends(get_db)):
    repo = TodoListRepository(db)
    todolist = repo.update(todo_list_id, todolist_update)
    if not todolist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TodoList not found")
    return todolist

@router.delete("/{todo_list_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todolist(todo_list_id: int, db: Session = Depends(get_db)):
    repo = TodoListRepository(db)
    success = repo.delete(todo_list_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TodoList not found")
    return None
