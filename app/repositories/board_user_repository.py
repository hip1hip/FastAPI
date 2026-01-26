from sqlmodel import Session, select

from app.models.board_user_model import BoardUser
from app.schemas.board_user_schema import BoardUserCreate

"""
Session은 DB와 연결 통로임, 트랜젝셔널도 관리
__init__ 은 의존성 주입(DI) 이렇게 한번 주입받아서 사용하면 
내부에서 self.session 으로 편하게 꺼내 씀 
"""


class BoardUserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, user_in: BoardUserCreate) -> BoardUser:
        """새로운 유저를 DB에 저장"""
        # 스키마(DTO) 데이터를 모델 객체로 변환
        db_user = BoardUser.model_validate(user_in)

        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def get_by_id(self, user_id: int) -> BoardUser | None:
        """ID로 유저를 조회합니다."""
        return self.session.get(BoardUser, user_id)

    def get_by_nick_name(self, nick_name: str) -> BoardUser | None:
        """닉네임으로 유저를 조회합니다.(중복체크)"""
        stmt = select(BoardUser).where(BoardUser.nick_name == nick_name)
        return self.session.exec(stmt).first()

    def get_all(self):
        """모든 유저 목록을 가져옴"""
        stmt = select(BoardUser)
        return self.session.exec(stmt).all()
        # .exec = 내가 작성한 명령문을 실제 DB 전달해서 실행 요청함

    