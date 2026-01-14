from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field

# env_path = Path(__file__).parent.parent.pa


class Settings(BaseSettings):
    # 1. 타입이 자동으로 지정됨 (MYSQL_PORT는 정수로 자동 변환)
    MYSQL_USER: str = ""
    MYSQL_PASSWORD: str = ""
    MYSQL_HOST: str = ""
    MYSQL_PORT: int = 3307
    MYSQL_DB: str = ""

    # 2. @property 대신 @computed_field를 쓰면 나중에 출력이 가능함
    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URL(self) -> str:
        return f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
print(f"연결할 DB 주소: {settings.SQLALCHEMY_DATABASE_URL}")
