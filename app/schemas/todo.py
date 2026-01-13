from pydantic import BaseModel
from datetime import datetime


class TodoBase(BaseModel):
    content: str


class TodoCreate(TodoBase):
    pass


class TodoResponse(TodoBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
