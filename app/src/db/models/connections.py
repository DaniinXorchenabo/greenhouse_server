from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.sessions import _real_session, guest_session, user_session
from src.db.models.sessions import admin_session, developer_session, system_session

__all__ = ["_real_readonly_conn", 'guest_readonly_conn', 'user_readonly_conn',
           'admin_readonly_conn', 'developer_readonly_conn', 'system_readonly_conn',
           "_real_write_conn", "guest_write_conn", "user_write_conn",
           "admin_write_conn", "developer_write_conn", "system_write_conn", ]


async def _real_readonly_conn() -> AsyncIterator[AsyncSession]:
    async with _real_session() as session:
        yield session


async def _real_write_conn() -> AsyncIterator[AsyncSession]:
    async with _real_session() as session:
        async with session.begin():
            yield session


async def guest_readonly_conn() -> AsyncIterator[AsyncSession]:
    async with guest_session() as session:
        yield session


async def guest_write_conn() -> AsyncIterator[AsyncSession]:
    async with guest_session() as session:
        async with session.begin():
            yield session


async def user_readonly_conn() -> AsyncIterator[AsyncSession]:
    async with user_session() as session:
        yield session


async def user_write_conn() -> AsyncIterator[AsyncSession]:
    async with user_session() as session:
        async with session.begin():
            yield session


async def admin_readonly_conn() -> AsyncIterator[AsyncSession]:
    async with admin_session() as session:
        yield session


async def admin_write_conn() -> AsyncIterator[AsyncSession]:
    async with admin_session() as session:
        async with session.begin():
            yield session


async def developer_readonly_conn() -> AsyncIterator[AsyncSession]:
    async with developer_session() as session:
        yield session


async def developer_write_conn() -> AsyncIterator[AsyncSession]:
    async with developer_session() as session:
        async with session.begin():
            yield session


async def system_readonly_conn() -> AsyncIterator[AsyncSession]:
    async with system_session() as session:
        print('системная транзакция началась')
        yield session
        print("системная транзакция закончилась")


async def system_write_conn() -> AsyncIterator[AsyncSession]:
    async with system_session() as session:
        async with session.begin():
            print('системная транзакция началась')
            yield session
            print("системная транзакция закончилась")
