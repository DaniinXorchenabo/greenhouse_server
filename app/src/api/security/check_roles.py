from fastapi import FastAPI, Depends, Security

from src.piccolo_db.gh import tables as tab
from src.piccolo_db.piccolo_conf import guest_engine
from src.piccolo_db.piccolo_conf import user_engine
from src.piccolo_db.piccolo_conf import admin_engine
from src.piccolo_db.piccolo_conf import developer_engine
from src.piccolo_db.piccolo_conf import system_engine
from src.utils.enums import Scopes
from src.api.security.get_user import get_current_user
from src.api.security.schemes import Tab


__all__ = [
    "guest",
    "user",
    "admin",
    "developer",
    "system",
    "guest_transaction",
    "user_transaction",
    "admin_transaction",
    "developer_transaction",
    "system_transaction",
]


async def get_db():
    async with guest_engine.transaction():
        print("до транзакции")
        yield tab.guest
        print("после транзакции")


async def guest_transaction():
    async with guest_engine.transaction():
        yield tab.guest


async def user_transaction():
    async with user_engine.transaction():
        yield tab.guest


async def admin_transaction():
    async with admin_engine.transaction():
        yield tab.guest


async def developer_transaction():
    async with developer_engine.transaction():
        yield tab.guest


async def system_transaction():
    async with system_engine.transaction():
        yield tab.guest


def guest(table=Depends(guest_transaction)):
    return table


def user(user=Security(get_current_user, scopes=[Scopes.user.value]),
         table=Depends(user_transaction)):
    return Tab(u=user, t=table)


def admin(user=Security(get_current_user, scopes=[Scopes.admin.value]),
          table=Depends(admin_transaction)):
    return Tab(u=user, t=table)


def developer(user=Security(get_current_user, scopes=[Scopes.dev.value]),
              table=Depends(developer_transaction)):
    return Tab(u=user, t=table)


def system(user=Security(get_current_user, scopes=[Scopes.system.value]),
           table=Depends(system_transaction)):
    """Неиспользуется"""
    return Tab(u=user, t=table)
