from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = (
        "mysql+pymysql://tester:tester@localhost:3308/llmagent?charset=utf8mb4"
    )

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
