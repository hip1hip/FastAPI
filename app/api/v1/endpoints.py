from fastapi import APIRouter, HTTPException, Request
from app.services.todo_service import TodoService

router = APIRouter()
todo_service = TodoService()


@router.get("/hello")
def say_hello():
    return {"message": "Hello from API endpoints!"}


@router.get("/todos")
def get_todos():
    return todo_service.get_all_todos()


@router.post("/todos")
async def post_create_todo(request: Request):
    body = await request.json()
    content = body.get("content")

    if not content:
        raise HTTPException(status_code=400, detail="content is required")

    return todo_service.create_new_todo(content=content)


@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    return todo_service.delete_one_todo(todo_id)
