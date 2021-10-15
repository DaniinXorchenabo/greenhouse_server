from typing import Any, Optional
from abc import ABC

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.api.responses.error.error import BaseErrorResponse
from src.api.responses.error.not_found import NotFound, UserNotFound


class MyBaseHttpException(HTTPException, ABC):
    default_status_code = 400
    default_response_model = BaseErrorResponse

    def __init__(self, answer: BaseErrorResponse = None,
                 status_code: int = None,
                 headers: Optional[dict[str, Any]] = None, **kwargs):
        status_code = status_code or self.default_status_code
        answer: BaseErrorResponse = answer or self.default_response_model(**kwargs)
        super(MyBaseHttpException, self).__init__(status_code, detail=answer, headers=headers)
        self.detail: BaseErrorResponse = answer

    @property
    def response(self) -> JSONResponse:
        return JSONResponse(content=self.detail.dict(), status_code=self.status_code, headers=self.headers)
