from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.engine.url import URL

from src.sqlalchemy.db.before_connect.connect_utils import base_connect_dict
from src.sqlalchemy.db.tables._real import real_engine_config


__all__ = ["_real_engine"]

_real_engine: AsyncEngine = create_async_engine(URL(**real_engine_config), **base_connect_dict)
