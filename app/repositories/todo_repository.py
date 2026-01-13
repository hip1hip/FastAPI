from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoCreate


class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def fetch_all_todos(self):
        return self.db.query(Todo).all()

    def insert_todo(self, content: str):
        new_todo = Todo(content=content)
        self.db.add(new_todo)
        self.db.commit()
        self.db.refresh(new_todo)
        return new_todo

    def delete_todo(self, todo_id: int):
        todo = self.db.query(Todo).filter(Todo.id == todo_id).first()

        if not todo:
            return 0

        self.db.delete(todo)
        self.db.commit()

        return 1
