from typing import Union

from pydantic import Field

from src.utils.enums import ResponseType, DataResponseType, MsgText
from src.api.responses.base import BaseResponse
from src.db.models.schemes import guest_schema, user_schema, admin_schema
from src.db.models.schemes import developer_schema, system_schema, _real_schema
from src.api.responses.data.data import BaseDataResponse


class ManyUsersResponse(BaseDataResponse):
    class_: DataResponseType = Field(DataResponseType.many_users, const=True, example=DataResponseType.many_users)
    users: list[Union[_real_schema.OutUser, system_schema.OutUser,
                      developer_schema.OutUser, admin_schema.OutUser,
                      user_schema.OutUser, guest_schema.OutUser]]


class GetUserResponse(BaseDataResponse):
    class_: DataResponseType = Field(DataResponseType.one_user, const=True, example=DataResponseType.one_user)
    user: Union[_real_schema.OutUser, system_schema.OutUser,
                developer_schema.OutUser, admin_schema.OutUser,
                user_schema.OutUser, guest_schema.OutUser]