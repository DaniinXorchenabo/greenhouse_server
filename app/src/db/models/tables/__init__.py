from collections import namedtuple
from typing import NamedTuple, Type

from src.sqlalchemy.db.tables._real import User as _real_User

from src.sqlalchemy.db.tables.guest import User as guest_User

from src.sqlalchemy.db.tables.user import User as user_User

from src.sqlalchemy.db.tables.admin import User as admin_User

from src.sqlalchemy.db.tables.developer import User as dev_User

from src.sqlalchemy.db.tables.system import User as system_User

__all__ = ['_real', 'guest', 'user', 'admin', 'developer', 'system',
           "TypeReal", "TypeGuest", "TypeUser", "TypeAdmin",
           "TypeDeveloper", "TypeSystem", ]


class TypeReal(NamedTuple):
    User: Type[_real_User] = _real_User


class TypeGuest(NamedTuple):
    User: Type[guest_User] = guest_User


class TypeUser(NamedTuple):
    User: Type[user_User] = user_User


class TypeAdmin(NamedTuple):
    User: Type[admin_User] = admin_User


class TypeDeveloper(NamedTuple):
    User: Type[dev_User] = dev_User


class TypeSystem(NamedTuple):
    User: Type[system_User] = system_User


_real = TypeReal()
guest = TypeGuest()
user = TypeUser()
admin = TypeAdmin()
developer = TypeDeveloper()
system = TypeSystem()

