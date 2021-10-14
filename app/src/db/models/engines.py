from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.engine.url import URL

from src.db.models.before_connect.connect_utils import base_connect_dict

from src.db.models.tables._real import real_engine_config
from src.db.models.tables.guest import guest_engine_config
from src.db.models.tables.user import user_engine_config
from src.db.models.tables.admin import admin_engine_config
from src.db.models.tables.developer import developer_engine_config
from src.db.models.tables.system import system_engine_config


__all__ = ["_real_engine", "guest_engine", "user_engine",
           "admin_engine", "developer_engine", "system_engine"]

_real_engine: AsyncEngine = create_async_engine(URL(**real_engine_config), **base_connect_dict)
guest_engine: AsyncEngine = create_async_engine(URL(**guest_engine_config), **base_connect_dict)
user_engine: AsyncEngine = create_async_engine(URL(**user_engine_config), **base_connect_dict)
admin_engine: AsyncEngine = create_async_engine(URL(**admin_engine_config), **base_connect_dict)
developer_engine: AsyncEngine = create_async_engine(URL(**developer_engine_config), **base_connect_dict)
system_engine: AsyncEngine = create_async_engine(URL(**system_engine_config), **base_connect_dict)
