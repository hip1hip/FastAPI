from fastapi import FastAPI
from app.api.v1.endpoints import router as todo_router
from app.core.database import Base, engine

# 테이블 자동 생성
# Base.metadata.create_all(bind=engine)

app = FastAPI(title="My Todo App")

app.include_router(todo_router, prefix="/api/v1", tags=["todos"])


@app.get("/")
def root():
    return {"message": "Hello I'm Inpyo"}
