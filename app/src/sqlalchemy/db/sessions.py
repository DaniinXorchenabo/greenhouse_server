from typing import Type
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from src.sqlalchemy.db.engines import _real_engine


__all__ = ["_real_session"]

_real_session: sessionmaker = sessionmaker(_real_engine, expire_on_commit=False, class_=AsyncSession)