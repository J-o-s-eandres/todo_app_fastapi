# app/infrastructure/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Ruta de base de datos SQLite (puedes cambiar a PostgreSQL u otra)
SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"

# Crear motor
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependencia para inyección en FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
