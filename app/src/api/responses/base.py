from typing import Union
from pydantic import BaseModel

from src.utils.enums import ResponseType, ErrorResponseType, DataResponseType


class BaseResponse(BaseModel):
    type_: ResponseType
    class_: Union[ErrorResponseType, DataResponseType]
