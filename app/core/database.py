import mysql.connector
from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 세션 팩토리: DB에 접속하는 '접속권'을 찍어내는 기계
# SessionLocal = sessionmaker(autocommit=False, autiflush=False, bind=engine)

# 베이스 클래스: 모든 DB 모델(테이블)의 부모가 될 클래스
# Base = declarative_base()


# DB 세션 의존성 주입을 위한 함수
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


def get_db():
    return mysql.connector.connect(
        host="localhost",
        port=3308,
        user="tester",
        password="tester",
        database="llmagent",
    )
