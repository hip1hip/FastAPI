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
        # 상세 조회 로직
        board = self.board_repo.get_by_id(board_id)

        # 여기서 비즈니스 규칙 추가: "글이 없으면 에러를 던져라" 같은 처리
        if not board:
            # TODO: 리턴 대신 바로 에러를 던짐 (404 Not Found)
            # 보통 HTTPException을 발생시키기도 합니다 .
            return None
        return board

    def get_all_boards(self):
        return self.board_repo.get_all()

    def update_board(self, board_id: int, board_in: BoardUpdate):
        # Service 에서만 검증 (존재 여부 확인)
        board = self.board_repo.get_by_id(board_id)
        if not board:
            return None

        # 검증 통고하하면 Repository에 위임
        return self.board_repo.update(board_id, board_in)

    def delete_board(self, board_id: int):
        board = self.board_repo.get_by_id(board_id)
        if not board:
            return None

        return self.board_repo.delete(board_id)
