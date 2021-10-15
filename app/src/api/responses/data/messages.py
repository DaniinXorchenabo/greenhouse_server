from typing import Union

from pydantic import Field

from src.utils.enums import ResponseType, DataResponseType, MsgText
from src.api.responses.base import BaseResponse
from src.db.models.schemes import guest_schema, user_schema, admin_schema
from src.db.models.schemes import developer_schema, system_schema, _real_schema
from src.api.responses.data.data import BaseDataResponse


class MessageResponse(BaseResponse):
    class_: DataResponseType = Field(DataResponseType.msg, const=True, example=DataResponseType.msg)
    message: MsgText


class OkMessageResponse(MessageResponse):
    message: MsgText = Field(MsgText.ok, const=True, example=MsgText.ok)
