from typing import Any, Optional
from abc import ABC

from fastapi import HTTPException
from pydantic import BaseModel

from src.api.responses.error.error import BaseErrorResponse
from src.api.responses.error.r_404_not_found import BaseNotFound, UserNotFound, PasswordOrUsernameIncorrect
from src.api.exceptions.base import MyBaseHttpException


class NotFoundError(MyBaseHttpException):
    default_status_code = 404
    default_response_model = BaseNotFound


class UserNotFoundError(NotFoundError):
    default_response_model = UserNotFound


class PasswordOrUsernameIncorrectError(NotFoundError):
    default_response_model = PasswordOrUsernameIncorrect
