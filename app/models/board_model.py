from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel

from app.models.base import TimestampModel

if TYPE_CHECKING:
    from .board_user_model import BoardUser


class BoardBase(SQLModel):
    title: str
    content: str


class Board(BoardBase, TimestampModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # Foreign Key 설정 (@ManyToOne)
    user_id: int = Field(foreign_key="board_user.id")

    # 관계 설정: author를 옹해 유저 객체에 바로 접근 가능
    writer: "BoardUser" = Relationship(back_populates="boards")
