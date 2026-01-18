from fastapi import APIRouter

from app.api.v1 import board_router, board_user_router


api_router = APIRouter()
api_router.include_router(board_router.router, prefix="/boards", tags=["boards"])
api_router.include_router(
    board_user_router.router, prefix="/board_users", tags=["board_users"]
)
