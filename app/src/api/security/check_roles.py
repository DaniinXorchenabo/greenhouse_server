from typing import AsyncIterator, Type
from fastapi import FastAPI, Depends, Security
from types import ModuleType
from typing import Literal

from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.enums import Scopes
from src.api.security.get_user import get_current_user
from src.api.security.schemes import Tab

from src.db.models.connections import _real_connection, guest_connection, user_connection
from src.db.models.connections import admin_connection, developer_connection, system_connection
from src.db.models.tables import TypeReal, TypeGuest, TypeUser, TypeAdmin, TypeDeveloper, TypeSystem

from src.db.models import GuestBox, UserBox, AdminBox, DeveloperBox, SystemBox, _RealBox

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
         session: AsyncSession = Depends(user_connection)) -> UserBox:
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
