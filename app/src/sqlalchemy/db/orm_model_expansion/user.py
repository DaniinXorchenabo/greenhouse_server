from uuid import UUID
from typing import Awaitable, Optional, Any, Union, AsyncIterator

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import update as sqlalchemy_update
from sqlalchemy.future import select
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.selectable import Select
from sqlalchemy.orm import sessionmaker


from src.utils.enums import Scopes
from src.sqlalchemy.db.schemes._real import CreateUser



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
    async def get_via_username(
            cls,
            _session: sessionmaker,
            username: str) -> Awaitable[Optional[Any]]:

        async with _session() as session:

            query: Select = select(cls).where(cls.username == username)
            print("*&--------", query, [query])
            res = await session.execute(query)
            # print("^%$-----", res)
            user_ = res.scalars().first()
            print("**_------------", user_, [user_], type(user_))
            return user_

    @classmethod
    def create(cls, session: AsyncSession, **kwargs) -> Awaitable:
        session.add(cls(**kwargs))
        return session.commit()
