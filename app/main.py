# app/main.py
from fastapi import FastAPI

app = FastAPI(title="ToDo App")

@app.get("/")
def read_root():
    return {"message": "Todo App API running!"}
