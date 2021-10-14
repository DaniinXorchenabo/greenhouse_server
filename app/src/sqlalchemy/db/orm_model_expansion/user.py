from uuid import UUID
from typing import Awaitable, Optional, Any

from sqlalchemy import update as sqlalchemy_update, delete
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.selectable import Select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.result import ChunkedIteratorResult, Result


from src.utils.enums import Scopes


class ScopesForUser(object):

    @property
    def scopes(self):
        return {Scopes(i) for i in self._scopes}

    @scopes.setter
    def scopes(self, value):
        self._scopes = {Scopes(i) for i in value}


class MapperOfUser(object):
    id: UUID
    username: str

    @classmethod
    async def update(cls, session: AsyncSession, id_: UUID, **kwargs):
        query = sqlalchemy_update(cls).where(cls.id == id_).values(
            **kwargs).execution_options(synchronize_session="fetch")
        await session.execute(query)
        await session.commit()

    @classmethod
    async def get_via_username(cls, _session: sessionmaker, username: str) -> Awaitable[Optional[Any]]:
        async with _session() as session:
            session: AsyncSession
            query: Select = select(cls).where(cls.username == username)
            res: Result = await session.execute(query)
            print(type(res))
            user_ = res.scalars().first()
            print("**_------------", user_, [user_], type(user_))
            return user_

    @classmethod
    async def get_via_id(cls, _session: sessionmaker, id_: UUID) -> Awaitable[Optional[Any]]:
        async with _session() as session:
            session: AsyncSession
            query: Select = select(cls).where(cls.id == id_)
            res: Result = await session.execute(query)
            user_ = res.scalars().first()
            return user_

    @classmethod
    async def all(cls, _session: sessionmaker):
        print(f'get all {cls.__name__}')

        async with _session() as session:
            session: AsyncSession
            res: Result = await session.execute(select(cls))

            users = res.scalars().all()
            print("**_------------", users, type(users))
            return users

    @classmethod
    def create(cls, session: AsyncSession, **kwargs) -> Awaitable:
        session.add(cls(**kwargs))
        return session.commit()

    def update_myself(self, session: AsyncSession, values: dict[str, Any]):
        q = sqlalchemy_update(self.__class__).where(self.__class__.id == self.id).values(**values)
        q.execution_options(synchronize_session="fetch")
        return session.execute(q)

    @classmethod
    def delete(cls, session: AsyncSession, id_: UUID) -> Awaitable:
        q = delete(cls).where(cls.id == id_)
        return session.execute(q)
