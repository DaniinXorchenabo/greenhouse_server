from pydantic import Field

from src.api.responses.error.error import BaseErrorResponse
from src.utils.enums import ErrorResponseType, NotFoundText


__all__ = ['BaseNotFound', 'UserNotFound', 'PasswordOrUsernameIncorrect']

class BaseNotFound(BaseErrorResponse):
    class_: ErrorResponseType = Field(ErrorResponseType.not_found, const=True, example=ErrorResponseType.not_found)
    detail: NotFoundText


class UserNotFound(BaseNotFound):
    detail: NotFoundText = Field(NotFoundText.user, const=True, example=NotFoundText.user)


class PasswordOrUsernameIncorrect(BaseNotFound):
    detail: NotFoundText = Field(NotFoundText.username_or_password, const=True,
                                 example=NotFoundText.username_or_password)