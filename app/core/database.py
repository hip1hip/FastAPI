from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# 데이터 베이스 엔진 생성
engine = create_engine(
    settings.DATABASE_URL,
    echo=False,  # SQL 로그 출력 여뷰
    pool_pre_ping=True,
    pool_recycle=3600,
)

# 세션 팩토리 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base 클래스 (ORM 모델이 상속할 기본 클래스)
Base = declarative_base()


# 세션 의존성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
