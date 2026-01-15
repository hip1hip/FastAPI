from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Relationship, SQLModel, Field
from .base import TimestampModel


if TYPE_CHECKING:
    from .board_model import Board


# 1. 공통 필드 정의 (Pydantic 모델 역할)
class BoardUserBase(SQLModel):
    nick_name: str = Field(index=False)


class BoardUser(BoardUserBase, TimestampModel, table=True):
    # 테이블 이름 명시
    __tablename__: str = "board_user"

    id: Optional[int] = Field(default=None, primary_key=True)

    # @OneToMany
    boards: List["Board"] = Relationship(back_populates="writer")
