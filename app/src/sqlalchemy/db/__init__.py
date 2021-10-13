from typing import NamedTuple

from sqlalchemy.ext.asyncio import AsyncSession

from src.sqlalchemy.db.tables import _real, guest, user, admin, developer, system
from src.sqlalchemy.db.tables import TypeReal, TypeGuest, TypeUser, TypeAdmin, TypeDeveloper, TypeSystem
from src.sqlalchemy.db.sessions import _real_session, guest_session, user_session
from src.sqlalchemy.db.sessions import admin_session, developer_session, system_session


class GuestBox(NamedTuple):
    s: AsyncSession
    t: TypeGuest = guest


class UserBox(NamedTuple):
    u: user.User
    s: AsyncSession
    t: TypeUser = user


class AdminBox(NamedTuple):
    u: admin.User
    s: AsyncSession
    t: TypeAdmin = admin


class DeveloperBox(NamedTuple):
    u: developer.User
    s: AsyncSession
    t: TypeDeveloper = developer


class SystemBox(NamedTuple):
    u: system.User
    s: AsyncSession
    t: TypeSystem = system


class _RealBox(NamedTuple):
    u: _real.User
    s: AsyncSession
    t: TypeReal = _real
