from fastapi import HTTPException
from app.repositories.todo_repository import TodoRepository


class TodoService:
    def __init__(self):
        self.todo_repo = TodoRepository()

    def get_all_todos(self):
        rows = self.todo_repo.fetch_all_todos()
        # 리시트 컴프리헨션 가공 로직을 여기서 처리!
        return [{"id": r[0], "content": r[1], "created_at": str(r[2])} for r in rows]

    def create_new_todo(self, content):
        row = self.todo_repo.insert_todo(content)
        return {"id": row[0], "content": row[1], "created_at": str(row[2])}

    def delete_one_todo(self, todo_id):
        affected_count = self.todo_repo.delete_todo(todo_id)

        if affected_count == 0:
            raise HTTPException(status_code=404, detail="Todo not found")

        return {"message": "Todo deleted"}
