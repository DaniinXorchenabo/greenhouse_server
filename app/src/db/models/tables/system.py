import os
from uuid import uuid4

from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import create_async_engine

from src.db.models.before_connect.connect_utils import base_connect_dict
from src.utils.files import check_environment_params_loaded
from src.db.models.orm_model_expansion.user import ScopesForUser, MapperOfUser


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


class User(_Current_Base, ScopesForUser, MapperOfUser):
    __tablename__ = 'user_'
    # __bind_key__ = "real"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(100), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    hashed_password = Column(String(4096), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    _scopes = Column(ARRAY(String(1)), nullable=False, default=[])

    def __repr__(self):
        return f"ststem.User({self.username}, id={str(self.id)[:6]})"