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
    not_found = "not found"
    db_error = 'db_error'


class MsgText(str, Enum):
    ok = 'ok'


class NotFoundText(str, Enum):
    user = 'User not found'


class DbErrorText(str, Enum):
    unique = 'Какое-то из полей запроса уже имеется в БД. Поле должно быть уникальным!'
    permission = 'Вы не имеете доступа, необходимого для выполнения запроса'
