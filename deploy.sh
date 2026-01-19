cd /home/ubuntu/workspace/FastAPI

echo "1. 프로젝트 폴더로 이동 완료"

git pull origin main

echo "2. 최신 코드 pull 완료"

CURRENT_PID=$(pgrep -f "uvicorn main:app")
if [ -z "$CURRENT_PID" ]; then
    echo "현재 실행 중인 uvicorn 프로세스가 없습니다."
else 
    echo "기존 프로세스 종료 시도 (PID: $CURRENT_PID)"
    kill -15 $CURRENT_PID
    sleep 2 
fi

echo "3. 프로세스 정리 완료"

nohup uv run fastapi run app/main.py --host 0.0.0.0 --port 8000 \
    > /dev/null 2>&1 < /dev/null &

echo "4. 서버 백그라운드 실행 완료!"

#chmod +x deploy.sh -> 파일 권한 수정