from typing import Union

from pydantic import Field

from src.utils.enums import ResponseType, DataResponseType, MsgText
from src.api.responses.base import BaseResponse
from src.db.models.schemes import guest_schema, user_schema, admin_schema
from src.db.models.schemes import developer_schema, system_schema, _real_schema


class BaseDataResponse(BaseResponse):
    type_: ResponseType = Field(ResponseType.data, const=True, example=ResponseType.data)
    class_: DataResponseType

