"""
의사코드 

중복체크 ,  입력받은 이름이 있는지 확인 
400 , 409 에러 던짐 
없으면 저장 

레포지토리는 DB에 Insert 
"""


from app.schemas.board_user_schema import BoardUserCreate
from app.repositories.board_user_repository import BoardUserRepository


class BoardUserService: 
    def __init__(self, board_user_repo: BoardUserRepository):
        self.board_user_repo = board_user_repo

    def create_board_user(self, board_user_in: BoardUserCreate):
        # 중복 체크 같은 유저, 닉네임 있는지 확인  
        if self.board_user_repo.get_by_nick_name(board_user_in.nick_name):
            return "이미 존재하는 닉네임입니다." 
        # 없으면 저장
        else:
            return self.board_user_repo.create(board_user_in)

    def get_all_board_user_list(self):
        return self.board_user_repo.get_all()


