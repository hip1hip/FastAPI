from app.core.exceptions import NotFoundError
from app.repositories.board_repository import BoardRepository
from app.schemas.board_schema import BoardCreate, BoardUpdate


class BoardService:
    def __init__(self, board_repo: BoardRepository):
        self.board_repo = board_repo

    def create_board(self, board_in: BoardCreate):
        # 1. 여기에 비즈니스 로직을 넣을 수 있습니다.
        # 예: 금지어가 포함되어 있는지 검사하거나, 유저 등급에 따른 권한 체크

        # 2. 로직이 통과하면 리포지토리를 통해 DB 저장
        return self.board_repo.create(board_in)

    def get_board_detail(self, board_id: int):
        """상세 조회 로직"""
        board = self.board_repo.get_by_id(board_id)
        # TODO: 중복되는 NotFoundError 수정하기 , find_id , get_id 로 나눠서 리포에서 처리하거나 , 헬퍼 함수 서비스단에 만들어서 사용.
        if not board:
            raise NotFoundError("게시글을 찾을 수 없습니다.")
        return board

    def get_all_boards(self):
        return self.board_repo.get_all()

    def update_board(self, board_id: int, board_in: BoardUpdate):
        board = self.board_repo.get_by_id(board_id)
        if not board:
            raise NotFoundError("게시글을 찾을 수 없습니다.")
        return self.board_repo.update(board_id, board_in)

    def delete_board(self, board_id: int):
        board = self.board_repo.get_by_id(board_id)
        if not board:
            raise NotFoundError("게시글을 찾을 수 없습니다.")
        return self.board_repo.delete(board_id)
