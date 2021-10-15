from typing import Any, Optional
from abc import ABC

from fastapi import HTTPException
from pydantic import BaseModel

from src.api.responses.error.error import BaseErrorResponse
from src.api.responses.error.not_found import NotFound, UserNotFound
from src.api.exceptions.base import MyBaseHttpException


class DbBaseError(MyBaseHttpException):
    pass