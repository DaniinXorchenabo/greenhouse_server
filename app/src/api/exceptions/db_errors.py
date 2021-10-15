from typing import Any, Optional
from abc import ABC

from fastapi import HTTPException
from pydantic import BaseModel

from src.api.responses.error.error import BaseErrorResponse
from src.api.responses.error.db import UniqueDbErrorResponse, PermissionDbErrorResponse, BaseDbErrorResponse
from src.api.exceptions.base import MyBaseHttpException

__all__ = ['DbBaseError', 'UniqueDbBaseError', 'PermissionDbBaseError']


class DbBaseError(MyBaseHttpException):
    default_status_code = 400
    default_response_model = BaseDbErrorResponse


class UniqueDbBaseError(MyBaseHttpException):
    default_status_code = 400
    default_response_model = UniqueDbErrorResponse


class PermissionDbBaseError(MyBaseHttpException):
    default_status_code = 400
    default_response_model = PermissionDbErrorResponse
