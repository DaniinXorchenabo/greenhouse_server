import os
from uuid import uuid4

from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import create_async_engine

from src.sqlalchemy.db.before_connect.connect_utils import base_connect_dict
from src.utils.files import check_environment_params_loaded

__all__ = ["system_engine_config",
           "BaseOfSystemDB",
           "User"]
check_environment_params_loaded()
system_engine_config = {
    "database": os.environ.get("PGDATABASE"),
    "username": os.environ.get("PG_EDIT_DB_STRUCTURE_NAME"),
    "password": os.environ.get("PG_EDIT_DB_STRUCTURE_PASSWORD"),
    "host": os.environ.get("PGHOST"),
    "port": os.environ.get("PGPORT"),
    "drivername": "postgresql+asyncpg"

}

_Current_Base = BaseOfSystemDB = declarative_base(name="BaseOfSystemDB")


class User(_Current_Base):
    __tablename__ = 'user_'
    # __bind_key__ = "real"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    def __repr__(self):
        return "".format(self.id)
