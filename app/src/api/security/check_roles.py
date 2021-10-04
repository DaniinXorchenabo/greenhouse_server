from fastapi import FastAPI, Depends, Security

# from src.piccolo_db.gh import tables as tab
# from src.piccolo_db.piccolo_conf import guest_engine
# from src.piccolo_db.piccolo_conf import user_engine
# from src.piccolo_db.piccolo_conf import admin_engine
# from src.piccolo_db.piccolo_conf import developer_engine
# from src.piccolo_db.piccolo_conf import system_engine
from src.utils.enums import Scopes
from src.api.security.get_user import get_current_user
from src.api.security.schemes import Tab
from src import db as t
from tortoise.exceptions import OperationalError
from tortoise.models import Model
from tortoise.transactions import atomic, in_transaction

from src.db.tortoise_orm_config import config

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
    try:
        async with in_transaction(config["connections"].get("guest", "default")) as connection:
            print("до транзакции")
            t.guest_t.is_transaction = connection
            yield t.guest_t
            t.guest_t.is_transaction = None
            print("после транзакции")

    except OperationalError:
        pass


async def guest_transaction():
    try:
        async with in_transaction(config["connections"].get("guest", "default")) as connection:
            print("до транзакции")
            t.guest_t.is_transaction = connection
            yield t.guest_t
            t.guest_t.is_transaction = None
            print("после транзакции")

    except OperationalError:
        pass


async def user_transaction():
    try:
        async with in_transaction(config["connections"].get("user", "default")) as connection:
            print("до транзакции")
            t.user_t.is_transaction = connection
            yield t.user_t
            t.user_t.is_transaction = None
            print("после транзакции")

    except OperationalError:
        pass


async def admin_transaction():
    try:
        async with in_transaction(config["connections"].get("admin", "default")) as connection:
            print("до транзакции")
            t.admin_t.is_transaction = connection
            yield t.admin_t
            t.admin_t.is_transaction = None
            print("после транзакции")

    except OperationalError:
        pass


async def developer_transaction():
    try:
        async with in_transaction(config["connections"].get("developer", "default")) as connection:
            print("до транзакции")
            t.dev_t.is_transaction = connection
            yield t.dev_t
            t.dev_t.is_transaction = None
            print("после транзакции")

    except OperationalError:
        pass


async def system_transaction():
    try:
        async with in_transaction(config["connections"].get("system", "default")) as connection:
            print("до транзакции")
            t.system_t.is_transaction = connection
            yield t.system_t
            t.system_t.is_transaction = None
            print("после транзакции")

    except OperationalError:
        pass


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
