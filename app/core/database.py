from sqlmodel import create_engine, Session, SQLModel
from app.core.config import settings

# 1. 엔진 생성: DB와의 실제 통로를 뚫는 역할
# echo=True 터미널에 실제 실행되는 SQL 로그가 찍힘(디버그용)
engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, echo=True)


# 2. DB 테이블 생성  (Nest 에 synchronize: true 역할)
# FIXME: EC2 에 올릴 때 DB 초기화 된 상태로 올라감 , 따라서 자동 생성 되게 해야함. 추후 RDS 쓰면 해당 건 주석 처리 필요.
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# 3. 세션 주입
def get_session():
    with Session(engine) as session:
        yield session
