from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_USER: str = "todo_user"
    DB_PASSWORD: str = "todo_pass"
    DB_NAME: str = "todo_db"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"

    @property
    def sqlalchemy_database_uri(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"

settings = Settings()
