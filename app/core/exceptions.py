class APIException(Exception):
    """기본 API 예외"""

    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail


class NotFoundError(APIException):
    """404 Not Found"""

    def __init__(self, detail: str):
        super().__init__(status_code=404, detail=detail)


class BadRequestError(APIException):
    """400 Bad Request"""

    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)


class Unauthorized(APIException):
    """401 Unauthorized"""

    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)


class Forbidden(APIException):
    """403 Forbidden"""

    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)
