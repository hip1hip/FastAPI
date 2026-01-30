from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.database import get_session
from app.repositories.board_user_repository import BoardUserRepository
from app.schemas.board_user_schema import BoardUserCreate, BoardUserRead
from app.services.board_user_service import BoardUserService


router = APIRouter()


@router.post("/", response_model=BoardUserRead, summary="유저 생성")
def create_board_user(
    board_user_in: BoardUserCreate, session: Session = Depends(get_session)
):
    repo = BoardUserRepository(session)
    service = BoardUserService(repo)
    return service.create_board_user(board_user_in)


@router.get("/", response_model=List[BoardUserRead], summary="유저 조회")
def get_all_board_user_list(session: Session = Depends(get_session)):
    repo = BoardUserRepository(session)
    service = BoardUserService(repo)
    return service.get_all_board_users()


@router.delete("/{board_user_id}", summary="유저 삭제")
def delete_board_user(board_user_id, session: Session = Depends(get_session)):
    repo = BoardUserRepository(session)
    service = BoardUserService(repo)

    return service.delete_board_user(board_user_id)
