from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.core.database import get_session
from app.repositories.board_repository import BoardRepository
from app.schemas.board_schema import BoardCreate, BoardRead, BoardUpdate
from app.services.board_service import BoardService

# 1. 라우터 설정(prefix는 URL 앞에 붙을 공통 주소입니다.)
router = APIRouter()

# TODO: 추후 리펙토링 , 중복되는 코드 정리: session: Session = Depends(get_session)


@router.post("/", response_model=BoardRead)
def create_board(board_in: BoardCreate, session: Session = Depends(get_session)):
    repo = BoardRepository(session)
    service = BoardService(repo)
    return service.create_board(board_in)


@router.get("/", response_model=List[BoardRead])
def get_boards(session: Session = Depends(get_session)):
    repo = BoardRepository(session)
    service = BoardService(repo)
    return service.get_all_boards()


@router.get("/{board_id}", response_model=BoardRead)
def get_board_detail(board_id: int, session: Session = Depends(get_session)):
    repo = BoardRepository(session)
    service = BoardService(repo)

    board = service.get_board_detail(board_id)
    if not board:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    return board


@router.put("/{board_id}", response_model=BoardRead)
def update_board(
    board_id: int, board_in: BoardUpdate, session: Session = Depends(get_session)
):
    repo = BoardRepository(session)
    service = BoardService(repo)

    return service.update_board(board_id, board_in)
