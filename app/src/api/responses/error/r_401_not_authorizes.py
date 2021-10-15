from pydantic import Field

from src.api.responses.error.error import BaseErrorResponse
from src.utils.enums import ErrorResponseType, NotAuthorizedText

__all__ = ['NotAuthorized']


class BaseNotAuthorized(BaseErrorResponse):
    class_: ErrorResponseType = Field(ErrorResponseType.not_found, const=True, example=ErrorResponseType.not_found)
    detail: NotAuthorizedText


class NotAuthorized(BaseNotAuthorized):
    detail: NotAuthorizedText = Field(NotAuthorizedText.not_authorized, const=True,
                                      example=NotAuthorizedText.not_authorized)