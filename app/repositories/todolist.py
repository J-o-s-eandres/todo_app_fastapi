from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.todolist import TodoList  
from app.schemas.todolist import TodoListCreate, TodoListUpdate

class TodoListRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[TodoList]:
        return self.db.query(TodoList).all()

    def get_by_id(self, todo_list_id: int) -> Optional[TodoList]:
        return self.db.query(TodoList).filter(TodoList.id == todo_list_id).first()

    def create(self, todo_list_create: TodoListCreate) -> TodoList:
        db_todo_list = TodoList(**todo_list_create.dict())
        self.db.add(db_todo_list)
        self.db.commit()
        self.db.refresh(db_todo_list)
        return db_todo_list

    def update(self, todo_list_id: int, todo_list_update: TodoListUpdate) -> Optional[TodoList]:
        db_todo_list = self.get_by_id(todo_list_id)
        if not db_todo_list:
            return None
        update_data = todo_list_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_todo_list, key, value)
        self.db.commit()
        self.db.refresh(db_todo_list)
        return db_todo_list

    def delete(self, todo_list_id: int) -> bool:
        db_todo_list = self.get_by_id(todo_list_id)
        if not db_todo_list:
            return False
        self.db.delete(db_todo_list)
        self.db.commit()
        return True
