# qr_generator/utils/api_response.py

from rest_framework.response import Response
from rest_framework import status
from typing import Any, Optional, Dict, Union
from dataclasses import dataclass

@dataclass
class ResponseCode:
    SUCCESS: int = 0
    ERROR: int = 1
    VALIDATION_ERROR: int = 2
    NOT_FOUND: int = 3
    UNAUTHORIZED: int = 4

class APIResponse:
    @staticmethod
    def success(
        data: Any = None,
        message: str = "Success",
        status_code: int = status.HTTP_200_OK
    ) -> Response:
        response_data = {
            "code": ResponseCode.SUCCESS,
            "status": "success",
            "message": message,
            "data": data
        }
        return Response(response_data, status=status_code)

    @staticmethod
    def error(
        message: str = "Error",
        code: int = ResponseCode.ERROR,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        data: Optional[Dict] = None
    ) -> Response:
        response_data = {
            "code": code,
            "status": "error",
            "message": message
        }
        if data is not None:
            response_data["data"] = data
        return Response(response_data, status=status_code)

    @staticmethod
    def validation_error(
        message: str = "Validation Error",
        errors: Optional[Dict] = None
    ) -> Response:
        return APIResponse.error(
            message=message,
            code=ResponseCode.VALIDATION_ERROR,
            status_code=status.HTTP_400_BAD_REQUEST,
            data={"errors": errors} if errors else None
        )
