from typing import Union

from pydantic import Field

from src.utils.enums import ResponseType, ErrorResponseType, MsgText
from src.api.responses.base import BaseResponse
from src.db.models.schemes import guest_schema, user_schema, admin_schema
from src.db.models.schemes import developer_schema, system_schema, _real_schema
from src.api.responses.base import BaseResponse


class BaseErrorResponse(BaseResponse):
    type_: ResponseType = Field(ResponseType.error, const=True, example=ResponseType.error)
    class_: ErrorResponseType
