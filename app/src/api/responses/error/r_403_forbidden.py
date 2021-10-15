from pydantic import Field

from src.api.responses.error.error import BaseErrorResponse
from src.utils.enums import ErrorResponseType, ForbiddenText

__all__ = ['BaseForbidden', 'ForbiddenRequest']


class BaseForbidden(BaseErrorResponse):
    class_: ErrorResponseType = Field(ErrorResponseType.forbidden, const=True,
                                      example=ErrorResponseType.forbidden)
    detail: ForbiddenText


class ForbiddenRequest(BaseErrorResponse):
    detail: ForbiddenText = Field(ForbiddenText.base, const=True, example=ForbiddenText.base)
