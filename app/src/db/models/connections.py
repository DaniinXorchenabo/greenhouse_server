from typing import AsyncIterator

from sqlalchemy.ext.asyncio import  AsyncSession

from src.db.models.sessions import _real_session, guest_session, user_session
from src.db.models.sessions import admin_session, developer_session, system_session


__all__ = ["_real_connection", 'guest_connection', 'user_connection',
           'admin_connection', 'developer_connection', 'system_connection']


async def _real_connection() -> AsyncIterator[AsyncSession]:
    async with _real_session() as session:
        async with session.begin():
            yield session


async def guest_connection() -> AsyncIterator[AsyncSession]:
    async with guest_session() as session:
        async with session.begin():
            yield session


async def user_connection() -> AsyncIterator[AsyncSession]:
    async with user_session() as session:
        async with session.begin():
            yield session


async def admin_connection() -> AsyncIterator[AsyncSession]:
    async with admin_session() as session:
        async with session.begin():
            yield session


async def developer_connection() -> AsyncIterator[AsyncSession]:
    async with developer_session() as session:
        async with session.begin():
            yield session


async def system_connection() -> AsyncIterator[AsyncSession]:
    async with system_session() as session:
        async with session.begin():
            print('системная транзакция началась')
            yield session
            print("системная транзакция закончилась")

#
# async def get_db() -> AsyncIterator[tab.guest]:
#     async with guest_engine.transaction():
#         print("до транзакции")
#         yield tab.guest
#         print("после транзакции")
#
#
# async def guest_transaction():
#
#     async for res in get_db():
#         res
#
#     async with guest_engine.transaction():
#         yield tab.guest
#
#
# async def user_transaction():
#     async with user_engine.transaction():
#         print("before")
#         yield tab.user
#         print("after")
#
#
# async def admin_transaction():
#     async with admin_engine.transaction():
#         yield tab.admin
#
#
# async def developer_transaction():
#     async with developer_engine.transaction():
#         yield tab.developer
#
#
# async def system_transaction():
#     async with system_engine.transaction():
#         yield tab.system
