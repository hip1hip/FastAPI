from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

from app.schemas.board_user_schema import BoardUserRead

"""
BaseModel은 Pydantic(파이던틱) 이라는 라이브러리에서 제공하는 "데이터 설계도"
FastAPI에서 BaseModel을 상속받아 클래스를 만드는 이유 3가지 
1. 데이터 검증: 프론트에서 보낸 데이터가 우리가 정한 규칙에 맞는지
2. 직렬화 및 역직렬화: HTTP 요청으로 들어온 JSON 데이터를 파이썬 객체로 변환 
3. 자동 문서화: /docs에 자동 저장 

Pydantic (BaseModel): "이 데이터의 **형식(Type)**이 맞는지만 검사할게!" (데이터 검증 전용)

SQLModel (SQLModel): "난 형식 검사도 할 수 있고, DB 테이블로 변환될 준비도 되어 있어!" (검증 + DB 통합)

"""


# 게시글 공통 필드
class BoardBase(BaseModel):
    title: str
    content: str


# 게시글 생성 요청
class BoardCreate(BoardBase):
    # user_id: int
    pass


# 게시글 수정 요청
class BoardUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


# 게시글 상세 조회 응담 (작성자 정보 포함)
class BoardRead(BoardBase):
    id: int = Field(..., serialization_alias="board_id")
    created_at: datetime
    updated_at: datetime

    writer: BoardUserRead

    model_config = ConfigDict(from_attributes=True)
