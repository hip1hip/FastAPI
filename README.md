# FastAPI

Repository for FastAPI practice
---
# Step 1: uv 설치 및 프로젝트 초기화
# uv가 없다면 설치 (Windows 기준, Mac/Linux는 공식 문서 참조)
powershell -ExecutionPolicy ByPass -c "ir https://astral.sh/uv/install.ps1"

# 프로젝트 폴더 생성 및 이동
mkdir my-fastapi-app
cd my-fastapi-app

# 가상환경 생성 및 활성화
uv init
uv venv
source .venv/Scripts/activate  # Windows
# source .venv/bin/activate    # Mac/Linux

# Step 2: FastAPI 설치
uv add fastapi uvicorn

# 서버 실행 
uv run fastapi dev main.py

- 서버 실행 fastapi install 에러 처리  
uv add "fastapi[standard]" 

- fastapi dev: 개발 모드로 실행한다는 뜻입니다. 코드를 수정하고 저장하면 서버가 자동으로 재시작되어 아주 편리합니다.