# app/main.py
from fastapi import FastAPI
from app.api.v1.endpoints.tasks import task
from app.api.v1.endpoints.todolists import todolist
from app.infrastructure.db.base import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todolist.router)
app.include_router(task.router)
