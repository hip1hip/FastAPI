from sqlmodel import create_engine, Session, SQLModel
from app.core.config import settings

# 1. 엔진 생성: DB와의 실제 통로를 뚫는 역할
# echo=True 터미널에 실제 실행되는 SQL 로그가 찍힘(디버그용)
engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, echo=True)


# 2. DB 테이블 생성  (Nest 에 synchronize: true 역할)
# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)


# 3. 세션 주입
def get_session():
    with Session(engine) as session:
        yield session
