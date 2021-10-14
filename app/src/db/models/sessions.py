from typing import Type
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from src.db.models.engines import _real_engine, guest_engine, user_engine
from src.db.models.engines import admin_engine, developer_engine, system_engine


__all__ = ["_real_session", "guest_session", "user_session",
           "admin_session", "developer_session", "system_session"]

_real_session: sessionmaker = sessionmaker(_real_engine, expire_on_commit=False, class_=AsyncSession)
guest_session: sessionmaker = sessionmaker(guest_engine, expire_on_commit=False, class_=AsyncSession)
user_session: sessionmaker = sessionmaker(user_engine, expire_on_commit=False, class_=AsyncSession)
admin_session: sessionmaker = sessionmaker(admin_engine, expire_on_commit=False, class_=AsyncSession)
developer_session: sessionmaker = sessionmaker(developer_engine, expire_on_commit=False, class_=AsyncSession)
system_session: sessionmaker = sessionmaker(system_engine, expire_on_commit=False, class_=AsyncSession)
