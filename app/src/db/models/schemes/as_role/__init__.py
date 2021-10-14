from collections import namedtuple
from typing import NamedTuple, Type

from src.db.models.schemes.as_role._real import DbUser as _real_DbUser
from src.db.models.schemes.as_role._real import CreateUser as _real_CreateUser
from src.db.models.schemes.as_role._real import InUser as _real_InUser
from src.db.models.schemes.as_role._real import OutUser as _real_OutUser

from src.db.models.schemes.as_role.guest import DbUser as guest_DbUser
from src.db.models.schemes.as_role.guest import InUser as guest_InUser
from src.db.models.schemes.as_role.guest import OutUser as guest_OutUser

from src.db.models.schemes.as_role.user import DbUser as user_DbUser
from src.db.models.schemes.as_role.user import OutUser as user_OutUser
from src.db.models.schemes.as_role.user import InUser as user_InUser
from src.db.models.schemes.as_role.user import UpdateMyself as user_UpdateMyself

from src.db.models.schemes.as_role.admin import DbUser as admin_DbUser
from src.db.models.schemes.as_role.admin import InUser as admin_InUser
from src.db.models.schemes.as_role.admin import OutUser as admin_OutUser

from src.db.models.schemes.as_role.developer import DbUser as dev_DbUser
from src.db.models.schemes.as_role.developer import InUser as dev_InUser
from src.db.models.schemes.as_role.developer import OutUser as dev_OutUser

from src.db.models.schemes.as_role.system import DbUser as system_DbUser
from src.db.models.schemes.as_role.system import InUser as system_InUser
from src.db.models.schemes.as_role.system import OutUser as system_OutUser
from src.db.models.schemes.as_role.system import CreateUser as system_CreateUser

__all__ = ['_real', 'guest', 'user', 'admin', 'developer', 'system',
           "TypeRealSchema", "TypeGuestSchema", "TypeUserSchema", "TypeAdminSchema",
           "TypeDeveloperSchema", "TypeSystemSchema", ]


class TypeRealSchema(NamedTuple):
    DbUser: Type[_real_DbUser] = _real_DbUser
    CreateUser: Type[_real_CreateUser] = _real_CreateUser
    InUser: Type[_real_InUser] = _real_InUser
    OutUser: Type[_real_OutUser] = _real_OutUser


class TypeGuestSchema(NamedTuple):
    DbUser: Type[guest_DbUser] = guest_DbUser
    InUser: Type[guest_InUser] = guest_InUser
    OutUser: Type[guest_OutUser] = guest_OutUser


class TypeUserSchema(NamedTuple):
    DbUser: Type[user_DbUser] = user_DbUser
    OutUser: Type[user_OutUser] = user_OutUser
    InUser: Type[user_InUser] = user_InUser
    UpdateMyself: Type[user_UpdateMyself] = user_UpdateMyself


class TypeAdminSchema(NamedTuple):
    User: Type[admin_DbUser] = admin_DbUser
    InUser: Type[admin_InUser] = admin_InUser
    OutUser: Type[admin_OutUser] = admin_OutUser


class TypeDeveloperSchema(NamedTuple):
    DbUser: Type[dev_DbUser] = dev_DbUser
    InUser: Type[dev_InUser] = dev_InUser
    OutUser: Type[dev_OutUser] = dev_OutUser


class TypeSystemSchema(NamedTuple):
    DbUser: Type[system_DbUser] = system_DbUser
    InUser: Type[system_InUser] = system_InUser
    OutUser: Type[system_OutUser] = system_OutUser
    CreateUser: Type[system_CreateUser] = system_CreateUser


_real = TypeRealSchema()
guest = TypeGuestSchema()
user = TypeUserSchema()
admin = TypeAdminSchema()
developer = TypeDeveloperSchema()
system = TypeSystemSchema()
