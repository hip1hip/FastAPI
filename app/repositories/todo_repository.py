from fastapi import HTTPException
from app.core.database import get_db


class TodoRepository:
    def fetch_all_todos(self):
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM todo")
        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        return rows

    def insert_todo(self, content):
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO todo (content) VALUES (%s)", (content,))
        conn.commit()

        todo_id = cursor.lastrowid

        cursor.execute("SELECT * FROM todo WHERE id = %s", (todo_id,))

        row = cursor.fetchone()

        cursor.close()
        conn.close()
        return row

    def delete_todo(self, todo_id):
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM todo WHERE id = %s", (todo_id,))
        conn.commit()

        affected = cursor.rowcount

        cursor.close()
        conn.close()

        return affected
