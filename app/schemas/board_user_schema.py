from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict


# 1. 공통 필드
class BoardUserBase(BaseModel):
    nick_name: str


# 2. 회원가입/ 생성 요청 DTO
class BoardUserCreate(BoardUserBase):
    pass


# 3. 정보 수정 요청 DTO
class BoardUserUpdate(BaseModel):
    nick_name: Optional[str] = None


# 4. 조회 응답 DTO (API 결과값으로 나가는 형태)
class BoardUserRead(BoardUserBase):
    id: int

    #  DB 객체 (SQLModel)를 Pydantic 모델로 변환 허용
    model_config = ConfigDict(from_attributes=True)
