from fastapi import FastAPI, Request, HTTPException
import mysql.connector
import os
import logging
from logging.handlers import RotatingFileHandler


# ---------------------------
# [TASK 1] 로그 저장 폴더 생성
# ---------------------------
# TODO: "logs"라는 이름의 폴더를 생성해주세요!
# Hint: os.makedirs()를 활용하면 됩니다. 이미 폴더가 있어도 에러가 나지 않도록 exist_ok=True 옵션 사용
os.makedirs("logs", exist_ok=True)  # 이 부분을 채워주세요!

# ---------------------------
# [TASK 2] 로그 포맷 및 핸들러 설정
# ---------------------------
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

# TODO: LOG_FORMAT을 사용하여 formatter를 생성하세요
# Hint: logging.Formatter()를 사용하여 LOG_FORMAT을 전달
formatter = logging.Formatter(LOG_FORMAT)  # 이 부분을 채워주세요!

file_handler = RotatingFileHandler(
    # TODO: 로그 파일 경로를 지정하세요 (logs 폴더 안에 app.log 파일)
    # Hint: "logs/파일명.확장자" 형식으로 작성
    filename="logs/app.log",  # 이 부분을 채워주세요!
    # TODO: 로그 파일의 최대 크기를 바이트 단위로 지정하세요
    # Hint: 1MB = 1024 * 1024 바이트
    maxBytes=1024 * 1024,  # 이 부분을 채워주세요!
    # TODO: 보관할 백업 파일 개수를 지정하세요
    # Hint: 5개의 백업 파일을 유지하려면?
    backupCount=5,  # 이 부분을 채워주세요!
    encoding="utf-8",
)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# ---------------------------
# [TASK 3] 루트 로거 통합 설정
# ---------------------------
root_logger = logging.getLogger()

# TODO: 로그 레벨을 INFO로 설정하세요
# Hint: logging 모듈의 INFO 상수를 사용하세요
root_logger.setLevel(logging.INFO)  # 이 부분을 채워주세요!

# TODO: 파일 핸들러를 루트 로거에 추가하세요
# Hint: addHandler() 메서드를 사용하여 file_handler를 추가
root_logger.addHandler(file_handler)  # 이 부분을 채워주세요!
root_logger.addHandler(console_handler)

# TODO: 콘솔 핸들러를 루트 로거에 추가하세요
# Hint: addHandler() 메서드를 사용하여 console_handler를 추가

logging.getLogger("uvicorn").handlers = root_logger.handlers
logging.getLogger("uvicorn.access").handlers = root_logger.handlers

app = FastAPI()


def get_db():
    return mysql.connector.connect(
        host="localhost",
        port=3307,
        user="user",
        password="user1234",
        database="my_fastapi_db",
    )


# ---------------------------
# [참고] TODO 테이블 자동 생성 함수
# ---------------------------
# 아래 주석을 해제하면 서버 시작 시 자동으로 todo 테이블이 생성됩니다.
# MySQL에 todo 테이블이 없다면 주석을 해제하여 사용하세요!

# @app.on_event("startup")
# async def startup_event():
#     conn = get_db()
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS todo (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             content VARCHAR(255) NOT NULL,
#             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#         )
#     """)
#     conn.commit()
#     cursor.close()
#     conn.close()


# ---------------------------
# CREATE
# ---------------------------
@app.post("/todos")
async def create_todo(request: Request):
    body = await request.json()
    content = body.get("content")

    if not content:
        raise HTTPException(status_code=400, detail="content is required")

    conn = get_db()
    cursor = conn.cursor()

    # 👉 학생이 작성해야 하는 SQL
    # INSERT 문 작성
    # 예: INSERT INTO todo (content) VALUES (%s)
    cursor.execute(
        ### TODO: 여기에 INSERT SQL 작성 ###
        "INSERT INTO todo (content) VALUES (%s)",
        (content,),
    )
    conn.commit()

    todo_id = cursor.lastrowid

    # 👉 학생이 작성해야 하는 SQL
    # SELECT 문 작성하여 방금 만든 todo 조회
    cursor.execute(
        ### TODO: 여기에 SELECT SQL 작성 ###
        "SELECT * FROM todo WHERE id = %s",
        (todo_id,),
    )
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    return {"id": row[0], "content": row[1], "created_at": str(row[2])}


# ---------------------------
# READ
# ---------------------------
@app.get("/todos")
def get_todos():
    conn = get_db()
    cursor = conn.cursor()

    # 👉 학생이 작성해야 하는 SQL
    # 전체 todo 조회 SELECT 문 작성
    cursor.execute(
        ### TODO: 여기에 전체 조회 SELECT SQL 작성 ###
        "SELECT id, content, created_at FROM todo ORDER BY id DESC"
    )
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [{"id": r[0], "content": r[1], "created_at": str(r[2])} for r in rows]


# ---------------------------
# DELETE
# ---------------------------
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    conn = get_db()
    cursor = conn.cursor()

    # 👉 학생이 작성해야 하는 SQL
    # 삭제 DELETE 문 작성
    cursor.execute(
        ### TODO: 여기에 DELETE SQL 작성 ###
        "DELETE FROM todo WHERE id = %s",
        (todo_id,),
    )
    conn.commit()

    affected = cursor.rowcount

    cursor.close()
    conn.close()

    if affected == 0:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": "Todo deleted"}
