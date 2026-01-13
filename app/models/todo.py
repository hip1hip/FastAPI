from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    class Config:
        from_attributes = True
