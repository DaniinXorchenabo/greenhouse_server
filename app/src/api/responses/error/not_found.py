from pydantic import Field

from src.api.responses.error.error import BaseErrorResponse
from src.utils.enums import ErrorResponseType, NotFoundText


class NotFound(BaseErrorResponse):
    class_: ErrorResponseType = Field(ErrorResponseType.not_found, const=True, example=ErrorResponseType.not_found)
    detail: NotFoundText


class UserNotFound(NotFound):
    detail: NotFoundText = Field(NotFoundText.user, const=True, example=NotFoundText.user)
