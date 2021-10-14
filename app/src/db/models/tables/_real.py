import os
from uuid import uuid4

from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.selectable import Select


from src.db.models.before_connect.connect_utils import base_connect_dict
from src.utils.files import check_environment_params_loaded
from src.db.models.orm_model_expansion.user import ScopesForUser, MapperOfUser


__all__ = ["real_engine_config",
           "BaseOfRealDB",
           "User"]
check_environment_params_loaded()
real_engine_config = {
    "database": os.environ.get("PGDATABASE"),
    "username": os.environ.get("PG_SUPERUSER_NAME"),
    "password": os.environ.get("PG_SUPERUSER_PASSWORD"),
    "host": os.environ.get("PGHOST"),
    "port": os.environ.get("PGPORT"),
    "drivername": "postgresql+asyncpg"

}
print(*real_engine_config.items(), sep='\n')

_Current_Base = BaseOfRealDB = declarative_base(name="BaseOfRealDB")


class User(_Current_Base, ScopesForUser, MapperOfUser):
    __tablename__ = 'user_'
    # __bind_key__ = "real"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(100), nullable=False)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    hashed_password = Column(String(4096), nullable=False)
    email = Column(String(100), nullable=False)
    _scopes = Column(ARRAY(String(1)), nullable=False, default=[])

    __table_args__ = (
        UniqueConstraint('username'),
        UniqueConstraint('email'),
    )

    def __repr__(self):
        return f"_real.User({self.username}, id={str(self.id)[:6]})"

