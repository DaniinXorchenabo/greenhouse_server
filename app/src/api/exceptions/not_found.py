from typing import Any, Optional
from abc import ABC

from fastapi import HTTPException
from pydantic import BaseModel

from src.api.responses.error.error import BaseErrorResponse
from src.api.responses.error.not_found import NotFound, UserNotFound
from src.api.exceptions.base import MyBaseHttpException


class NotFoundError(MyBaseHttpException):
    default_status_code = 404
    default_response_model = NotFound


class UserNotFoundError(NotFoundError):
    default_response_model = UserNotFound