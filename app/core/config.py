import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()


class Settings:
    # 기본값을 지정하여 None 에러 방지
    MYSQL_USER: str = os.getenv("MYSQL_USER", "")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_HOST: str = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT", "3307")
    MYSQL_DB: str = os.getenv("MYSQL_DB", "")

    # 포멧팅을 사용해 URL 생성
    @property
    def SQLALCHEMY_DATABASE_URL(self) -> str:
        return f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

    settings = Settings()
