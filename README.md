# 🚀 FastAPI Practice with uv

이 저장소는 **uv 패키지 관리자**를 사용하여
**FastAPI 실습 환경을 구축하고 학습**하기 위한 프로젝트입니다.

---

## 🛠️ 1. 환경 설정 (Setup)

### 1️⃣ uv 설치 (Windows)

`uv`는 기존 `pip`보다 훨씬 빠른 파이썬 패키지 관리자입니다.
PowerShell에서 아래 명령어를 실행하세요.

```powershell
powershell -ExecutionPolicy ByPass -c "Invoke-RestMethod https://astral.sh/uv/install.ps1 | Invoke-Expression"
```

---

### 2️⃣ 프로젝트 초기화 및 가상환경 설정

프로젝트 폴더로 이동한 후 아래 단계를 진행합니다.

```bash
# 1. 프로젝트 폴더로 이동
cd my-fastapi-app

# 2. 프로젝트 초기화 (처음 생성 시에만 실행)
uv init

# 3. 의존성 동기화 및 가상환경 생성
# (기존 프로젝트를 클론한 경우 .venv가 자동으로 구성됩니다)
uv sync

# 4. 가상환경 활성화 (Windows 기준)
.venv\Scripts\activate
```

---

## 📦 2. 패키지 관리

실습에 필요한 필수 패키지를 설치합니다.

`fastapi[standard]`를 설치하면 개발 서버인 **uvicorn**이 함께 포함되어
별도로 설치할 필요가 없습니다.

```bash
uv add "fastapi[standard]"
```

---

## 🏃 3. 서버 실행 (Execution)

개발용 모드로 서버를 실행합니다.
코드를 수정하고 저장하면 서버가 **자동으로 재시작(Hot Reload)** 됩니다.

```bash
uv run fastapi dev main.py
```

---

## 📁 프로젝트 구조 예시

```text
my-fastapi-app/          # 프로젝트 루트 (현재 있는 곳)
├── app/                 # 전체 소스코드가 들어가는 폴더
│   ├── __init__.py      # 이 폴더가 파이썬 패키지임을 알림 (빈 파일)
│   ├── main.py          # FastAPI 앱 객체를 생성하고 서버를 실행하는 진입점
│   ├── api/             # API 경로(Route)들을 정의하는 곳
│   │   ├── __init__.py
│   │   └── v1/          # API 버전 관리 (선택 사항)
│   │       └── endpoints.py
│   ├── core/            # 공통 설정 (DB 연결 정보, 보안 설정 등)
│   ├── models/          # 데이터베이스 테이블 정의 (DB 모델)
│   └── schemas/         # 데이터 검증 및 직렬화 정의 (Pydantic 모델)
├── .env                 # 환경 변수 설정 (비밀번호 등)
└── pyproject.toml       # (uv 사용 시) 프로젝트 설정 및 의존성 관리 파일
```
