from enum import Enum


__all__ = ["Scopes", "ResponseType", "DataResponseType", "ErrorResponseType",
           "MsgText"]


class Scopes(str, Enum):
    guest = 'g'
    user = 'u'
    admin = 'a'
    dev = 'd'
    system = 's'


class ResponseType(str, Enum):
    data = 'data'
    error = 'error'


class DataResponseType(str, Enum):
    many_users = 'many_users'
    one_user = 'one_user'
    msg = 'message'


class ErrorResponseType(str, Enum):
    pass


class MsgText(str, Enum):
    ok = 'ok'



