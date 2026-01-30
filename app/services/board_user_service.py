from app.core.exceptions import BadRequestError, NotFoundError
from app.schemas.board_user_schema import BoardUserCreate
from app.repositories.board_user_repository import BoardUserRepository


class BoardUserService:
    def __init__(self, board_user_repo: BoardUserRepository):
        self.board_user_repo = board_user_repo

    def create_board_user(self, board_user_id: BoardUserCreate):
        """유저 생성 로직"""
        if self.board_user_repo.get_by_nick_name(board_user_id.nick_name):
            raise BadRequestError("이미 존재하는 닉네임입니다.")

        return self.board_user_repo.create(board_user_id)

    def get_all_board_users(self):
        return self.board_user_repo.get_all()

    def delete_board_user(self, board_user_id: int):
        board_user = self.board_user_repo.get_by_id(board_user_id)
        if not board_user:
            raise NotFoundError("유저를 찾을 수 없습니다.")

        return self.board_user_repo.delete_board_user(board_user_id)
