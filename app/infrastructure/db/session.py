from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.sqlalchemy_database_uri, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
