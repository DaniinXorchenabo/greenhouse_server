from enum import Enum

__all__ = ["Scopes", "ResponseType", "DataResponseType", "ErrorResponseType",
           "MsgText", 'ForbiddenText']


class _MyBaseEnum(str, Enum):
    def __repr__(self):
        return super(str, self).__repr__()

    def __str__(self):
        return super(str, self).__str__()


class Scopes(str, Enum):
    guest = 'g'
    user = 'u'
    admin = 'a'
    dev = 'd'
    system = 's'


class ResponseType(_MyBaseEnum):
    data = 'data'
    error = 'error'


class DataResponseType(_MyBaseEnum):
    many_users = 'many_users'
    one_user = 'one_user'
    msg = 'message'


class ErrorResponseType(_MyBaseEnum):
    not_found = "not found"
    forbidden = "forbidden"
    db_error = 'db_error'


class MsgText(_MyBaseEnum):
    ok = 'ok'


class NotFoundText(_MyBaseEnum):
    user = 'User not found'
    username_or_password = 'Username or password is incorrect'


class ForbiddenText(_MyBaseEnum):
    base = "You can't access rights for getting this url"


class NotAuthorizedText(_MyBaseEnum):
    not_authorized = "user can't be authorized in system"


class DbErrorText(_MyBaseEnum):
    unique = 'Какое-то из полей запроса уже имеется в БД. Поле должно быть уникальным!'
    permission = 'Вы не имеете доступа, необходимого для выполнения запроса'
