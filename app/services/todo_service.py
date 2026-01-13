from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.todo_repository import TodoRepository


class TodoService:
    def __init__(self, db: Session):
        self.todo_repo = TodoRepository(db)

    def get_all_todos(self):
        todos = self.todo_repo.fetch_all_todos()
        return [
            {"id": t.id, "content": t.content, "created_at": str(t.created_at)}
            for t in todos
        ]

    def create_new_todo(self, content: str):
        todo = self.todo_repo.insert_todo(content)
        return {
            "id": todo.id,
            "content": todo.content,
            "created_at": str(todo.created_at),
        }

    def delete_one_todo(self, todo_id: int):
        affected_count = self.todo_repo.delete_todo(todo_id)

        if affected_count == 0:
            raise HTTPException(status_code=404, detail="Todo not found")

        return {"message": "Todo deleted"}
