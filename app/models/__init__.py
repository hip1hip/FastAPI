"""
__init__.py를 두는 이유는 크게 두 가지입니다.
1. 패키지로 인식시키기: 다른 파일에서 import 할 수 있는 패키지로 인식하게 하기 위함.
2. "Circular Imports" (순환 참조) 방지 및 경로 깔끔하게 만들기
"""

from app.models.base import TimestampModel
from app.models.board_model import Board
from app.models.board_user_model import BoardUser
