from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.api.v1.router import api_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.exceptions import APIException

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


@app.exception_handler(APIException)
async def api_exception_handler(request, exc):
    # request: 에러가 발생했을 당시의 요청 정보 (URL, 헤더 등)
    # exc: 발생한 에러 객체 그자체 (우리가 raise한 녀석)
    return JSONResponse(
        # HTTP 상태 코드를 결정 (예: 404)
        status_code=exc.status_code,
        # 클라이언트가 실제로 받게 될 JSON 내용
        content={"error": True, "status_code": exc.status_code, "detail": exc.detail},
    )


@app.exception_handler(Exception)  # 모든 파이썬 기본 에러를 낚아챔
async def unhandler_exception_handler(request, exc):
    # 여기서 로그를 남기면 디버깅이 편함
    print(f"시스템 에러 발생: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={
            "error": True,
            "status_code": 500,
            "detail": "서버 내부 오류가 발생했습니다. 잠시 후 다시 시도해주십쇼",
        },
    )


def main():
    print("Hello from fastapi!")
