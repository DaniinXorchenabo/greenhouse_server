from typing import AsyncIterator, Type
from fastapi import FastAPI, Depends, Security
from types import ModuleType
from typing import Literal

from sqlalchemy.ext.asyncio import AsyncSession

# from src.piccolo_db.gh import tables as tab
# from src.piccolo_db.piccolo_conf import guest_engine
# from src.piccolo_db.piccolo_conf import user_engine
# from src.piccolo_db.piccolo_conf import admin_engine
# from src.piccolo_db.piccolo_conf import developer_engine
# from src.piccolo_db.piccolo_conf import system_engine
from src.utils.enums import Scopes
from src.api.security.get_user import get_current_user
from src.api.security.schemes import Tab

from src.piccolo_db.gh.tables import guest as test_guest
from src.sqlalchemy.db.tables import _real as _t_real, guest as t_guest
from src.sqlalchemy.db.tables import user as t_user, admin as t_admin
from src.sqlalchemy.db.tables import developer as t_developer, system as t_system
from src.sqlalchemy.db.connections import _real_connection, guest_connection, user_connection
from src.sqlalchemy.db.connections import admin_connection, developer_connection, system_connection
from src.sqlalchemy.db.tables import TypeReal, TypeGuest, TypeUser, TypeAdmin, TypeDeveloper, TypeSystem

from src.sqlalchemy.db import GuestBox, UserBox, AdminBox, DeveloperBox, SystemBox, _RealBox

__all__ = [
    "guest",
    "user",
    "admin",
    "developer",
    "system",
]


def guest(session: AsyncSession = Depends(guest_connection)) -> GuestBox:
    return GuestBox(s=session)


def user(current_user: AsyncSession = Security(get_current_user, scopes=[Scopes.user.value]),
         session=Depends(user_connection)) -> UserBox:
    return UserBox(u=current_user, s=session)


def admin(current_user=Security(get_current_user, scopes=[Scopes.admin.value]),
          session: AsyncSession = Depends(admin_connection)) -> AdminBox:
    return AdminBox(u=current_user, s=session)


def developer(current_user=Security(get_current_user, scopes=[Scopes.dev.value]),
              session: AsyncSession = Depends(developer_connection)) -> DeveloperBox:
    return DeveloperBox(u=current_user, s=session)


def system(current_user=Security(get_current_user, scopes=[Scopes.system.value]),
           session: AsyncSession = Depends(system_connection)) -> SystemBox:
    return SystemBox(u=current_user, s=session)
