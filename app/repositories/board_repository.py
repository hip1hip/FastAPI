from sqlmodel import Session, select

from app.models.board_model import Board
from app.schemas.board_schema import BoardCreate, BoardUpdate


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
        return self.session.exec(stmt).all()

    def update(self, board_id: int, board_in: BoardUpdate) -> Board | None:
        """게시글 수정"""
        db_board = self.session.get(Board, board_id)

        # 존재 여부 체크 (Pylance 에러 방지 및 안정성)
        if not db_board:
            return None

        # 전달 받은 board_id 데이터에서 값이 있는 것만 추출 (dict 뱐환)
        update_data = board_in.model_dump(exclude_unset=True)
        db_board.sqlmodel_update(update_data)

        self.session.add(db_board)
        self.session.commit()
        self.session.refresh(db_board)

        return db_board

    def delete(self, board_id: int) -> bool:
        """게시글 삭제"""
        db_board = self.session.get(Board, board_id)

        self.session.delete(db_board)
        self.session.commit()
        return True
