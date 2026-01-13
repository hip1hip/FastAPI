from fastapi import APIRouter, Depends, HTTPException, Request
from app.core.database import get_db
from app.services.todo_service import TodoService
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/hello")
def say_hello():
    return {"message": "Hello from API endpoints!"}


@router.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    service = TodoService(db)
    return service.get_all_todos()


@router.post("/todos")
async def post_create_todo(request: Request, db: Session = Depends(get_db)):
    body = await request.json()
    content = body.get("content")

    if not content:
        raise HTTPException(status_code=400, detail="content is required")

    service = TodoService(db)
    return service.create_new_todo(content=content)


@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    service = TodoService(db)
    return service.delete_one_todo(todo_id)
