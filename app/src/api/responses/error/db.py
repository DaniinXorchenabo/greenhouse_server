from pydantic import Field

from src.api.responses.error.error import BaseErrorResponse
from src.utils.enums import ErrorResponseType, DbErrorText


__all__ = ["BaseDbErrorResponse", "BaseDbErrorResponse", 'PermissionDbErrorResponse']

class BaseDbErrorResponse(BaseErrorResponse):
    class_: ErrorResponseType = Field(ErrorResponseType.db_error, const=True, example=ErrorResponseType.db_error)
    message: DbErrorText


class UniqueDbErrorResponse(BaseDbErrorResponse):
    message: DbErrorText = Field(DbErrorText.unique, const=True, example=DbErrorText.unique)


class PermissionDbErrorResponse(BaseDbErrorResponse):
    message: DbErrorText = Field(DbErrorText.permission, const=True, example=DbErrorText.permission)