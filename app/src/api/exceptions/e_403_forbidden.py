from typing import Any, Optional
from abc import ABC

from fastapi import HTTPException
from pydantic import BaseModel

from src.api.responses.error.error import BaseErrorResponse
from src.api.responses.error.r_403_forbidden import ForbiddenRequest, BaseForbidden
from src.api.exceptions.base import MyBaseHttpException


class BaseForbiddenError(MyBaseHttpException):
    default_status_code = 403
    default_response_model = BaseForbidden


class NotAccessForbidden(BaseForbiddenError):
    default_response_model = ForbiddenRequest
