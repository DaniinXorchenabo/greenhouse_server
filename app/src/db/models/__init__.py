from typing import NamedTuple

from sqlalchemy.ext.asyncio import AsyncSession

from src.sqlalchemy.db.tables import _real, guest, user, admin, developer, system
from src.sqlalchemy.db.tables import TypeReal, TypeGuest, TypeUser, TypeAdmin, TypeDeveloper, TypeSystem
from src.sqlalchemy.db.sessions import _real_session, guest_session, user_session
from src.sqlalchemy.db.sessions import admin_session, developer_session, system_session
from src.sqlalchemy.db.schemes import guest_schema, user_schema, admin_schema
from src.sqlalchemy.db.schemes import developer_schema, system_schema, _real_schema
from src.sqlalchemy.db.schemes import TypeGuestSchema, TypeUserSchema, TypeAdminSchema
from src.sqlalchemy.db.schemes import TypeDeveloperSchema, TypeSystemSchema, TypeRealSchema


class GuestBox(NamedTuple):
    s: AsyncSession
    t: TypeGuest = guest
    p: TypeGuestSchema = guest_schema


class UserBox(NamedTuple):
    u: user.User
    s: AsyncSession
    t: TypeUser = user
    p: TypeUserSchema = user_schema


class AdminBox(NamedTuple):
    u: admin.User
    s: AsyncSession
    t: TypeAdmin = admin
    p: TypeAdminSchema = admin_schema


class DeveloperBox(NamedTuple):
    u: developer.User
    s: AsyncSession
    t: TypeDeveloper = developer
    p: TypeDeveloperSchema = developer_schema


class SystemBox(NamedTuple):
    u: system.User
    s: AsyncSession
    t: TypeSystem = system
    p: TypeSystemSchema = system_schema


class _RealBox(NamedTuple):
    u: _real.User
    s: AsyncSession
    t: TypeReal = _real
    p: TypeRealSchema = _real_schema
