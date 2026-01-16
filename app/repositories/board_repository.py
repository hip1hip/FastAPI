from sqlmodel import Session, select

from app.models.board_model import Board
from app.schemas.board_schema import BoardCreate


class BoardRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, board_in: BoardCreate) -> Board:
        """게시글 새로 생성"""
        db_board = Board.model_validate(board_in)

        self.session.add(db_board)
        self.session.commit()
        self.session.refresh(db_board)
        return db_board

    def get_by_id(self, board_id: int) -> Board | None:
        """ID로 특정 게시글 하나를 조회합니다 (상세보기용)"""
        return self.session.get(Board, board_id)

    def get_all(self):
        """모든 게시판 조회"""
        stmt = select(Board)
        return self.session.exec(stmt).all
