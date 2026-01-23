from fastapi import FastAPI
from app.api.v1.router import api_router
from fastapi.middleware.cors import CORSMiddleware
from app.models.board_model import Board
from app.models.board_user_model import BoardUser

# from app.core.database import create_db_and_tables

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (임시)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드(GET, POST 등) 허용
    allow_headers=["*"],  # 모든 헤더 허용
)


# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()
#     print("DB 테이블 생성 시도 완료!")


def main():
    print("Hello from fastapi!")
