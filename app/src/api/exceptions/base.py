from typing import Any, Optional
from abc import ABC

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.api.responses.error.error import BaseErrorResponse
from src.api.responses.error.r_404_not_found import BaseNotFound, UserNotFound


class MyBaseHttpException(HTTPException, ABC):
    default_status_code = 400
    default_response_model = BaseErrorResponse
    default_headers: dict[str, str] = dict()

    def __init__(self, answer: BaseErrorResponse = None,
                 status_code: int = None,
                 headers: Optional[dict[str, Any]] = None, **kwargs):
        status_code = status_code or self.default_status_code
        answer: BaseErrorResponse = answer or self.default_response_model(**kwargs)
        super(MyBaseHttpException, self).__init__(status_code, detail=answer,
                                                  headers=self.default_headers | headers)
        self.detail: BaseErrorResponse = answer

    @property
    def response(self) -> JSONResponse:
        return JSONResponse(content=self.detail.dict(), status_code=self.status_code, headers=self.headers)

    def __repr__(self):
        model_ = ", ".join([f"{key}='{str(val.value)}'" for key, val in self.detail.dict().items()])
        return f'{self.__class__.__name__}(st_code={self.status_code}, answer=({model_}))'

    def __str__(self):
        return self.__repr__()
