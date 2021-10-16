from typing import AsyncIterator, Type
from fastapi import FastAPI, Depends, Security
from types import ModuleType
from typing import Literal

from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.enums import Scopes
from src.api.routs.security.get_user import get_current_user

from src.db.models.connections import _real_readonly_conn, guest_readonly_conn, user_readonly_conn
from src.db.models.connections import admin_readonly_conn, developer_readonly_conn, system_readonly_conn
from src.db.models.tables import TypeReal, TypeGuest, TypeUser, TypeAdmin, TypeDeveloper, TypeSystem

from src.db.models import GuestBox, UserBox, AdminBox, DeveloperBox, SystemBox, _RealBox

__all__ = [
    "guest",
    "user",
    "admin",
    "developer",
    "system",
]


def guest(session: AsyncSession = Depends(guest_readonly_conn)) -> GuestBox:
    return GuestBox(s=session)


def user(current_user: AsyncSession = Security(get_current_user, scopes=[Scopes.user.value]),
         session: AsyncSession = Depends(user_readonly_conn)) -> UserBox:
    return UserBox(u=current_user, s=session)


def admin(current_user=Security(get_current_user, scopes=[Scopes.admin.value]),
          session: AsyncSession = Depends(admin_readonly_conn)) -> AdminBox:
    return AdminBox(u=current_user, s=session)


def developer(current_user=Security(get_current_user, scopes=[Scopes.dev.value]),
              session: AsyncSession = Depends(developer_readonly_conn)) -> DeveloperBox:
    return DeveloperBox(u=current_user, s=session)


def system(current_user=Security(get_current_user, scopes=[Scopes.system.value]),
           session: AsyncSession = Depends(system_readonly_conn)) -> SystemBox:
    return SystemBox(u=current_user, s=session)
