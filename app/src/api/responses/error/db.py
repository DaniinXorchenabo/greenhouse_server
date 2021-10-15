from pydantic import Field

from src.api.responses.error.error import BaseErrorResponse
from src.utils.enums import ErrorResponseType, DbErrorText


class BaseDbErrorResponse(BaseErrorResponse):
    class_: ErrorResponseType = Field(ErrorResponseType.db_error, const=True, example=ErrorResponseType.db_error)
    message: DbErrorText