from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class TimestampModel(SQLModel):
    # 1. UUID: 외부 노출용 고유키 (API 호출 시 id 대신 사용 권장)
    uuid: UUID = Field(default_factory=uuid4, index=True, unique=True, nullable=False)

    # 2. 생성일
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)

    # 3. 수정일: sa_column_kwargs를 통해 수정한시간이 자동으로 찍히게 설정
    updated_at: datetime = Field(
        default_factory=datetime.now,
        # sa_column_kwargs 는 SQLAlchemy의 Column 객체를 생성할 때 전달하고 싶은 세부 설정을 딕셔너리로 담아 보내는 보관함.
        sa_column_kwargs={
            "onupdate": datetime.now  # 데이터 수정 시 서버 시간으로 자동 갱신
        },
        nullable=False,
    )

    # 4. Soft Delete
    deleted_at: Optional[datetime] = Field(default=None)
