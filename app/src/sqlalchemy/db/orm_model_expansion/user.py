from uuid import UUID
from typing import Awaitable, Optional, Any

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import update as sqlalchemy_update
from sqlalchemy.future import select
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.selectable import Select

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
    def get_via_username(cls, session: AsyncSession, username: str) -> Awaitable[Optional[Any]]:
        query: Select = select(cls).where(cls.username == username).first()
        return session.execute(query)
