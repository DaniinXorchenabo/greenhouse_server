import asyncio
import os
from logging.config import fileConfig

import asyncpg
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.engine.create import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import create_async_engine
import sqlalchemy

from alembic import context

# from src.utils.db import get_migration_url
from src.utils.files import check_environment_params_loaded
from src.sqlalchemy.db.tables._real import real_engine_config

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)


# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

from src.sqlalchemy.db.tables._real import BaseOfRealDB
from src.sqlalchemy.db.before_connect.connect_utils import migration_engine_config

target_metadata = BaseOfRealDB.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    check_environment_params_loaded()
    # url = URL(**real_engine_config)
    try:
        url = URL(**migration_engine_config)
        context.configure(
            url=url,
            target_metadata=target_metadata,
            literal_binds=True,
            dialect_opts={"paramstyle": "named"},
        )

        with context.begin_transaction():
            context.run_migrations()
    except (asyncpg.exceptions.InvalidPasswordError, sqlalchemy.exc.ProgrammingError):
        url = URL(**real_engine_config)
        context.configure(
            url=url,
            target_metadata=target_metadata,
            literal_binds=True,
            dialect_opts={"paramstyle": "named"},
        )

        with context.begin_transaction():
            context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # connectable = AsyncEngine(
    #     engine_from_config(
    #         config.get_section(config.config_ini_section),
    #         prefix="sqlalchemy.",
    #         poolclass=pool.NullPool,
    #         future=True,
    #     )
    # )
    # url = get_migration_url()

    # url = URL(**real_engine_config)
    try:
        assert False
        url = URL(**migration_engine_config)
        connectable: AsyncEngine = AsyncEngine(create_engine(url, **{"poolclass": pool.NullPool, "future": True, }))
        async with connectable.connect() as connection:
            await connection.run_sync(do_run_migrations)
    except (asyncpg.exceptions.InvalidPasswordError, sqlalchemy.exc.ProgrammingError, AssertionError) as e:
        # raise e from e
        print("------------------ERROR. I'm using super_user role!!!!!!")
        url = URL(**real_engine_config)
        connectable: AsyncEngine = AsyncEngine(create_engine(url, **{"poolclass": pool.NullPool, "future": True, }))
        async with connectable.connect() as connection:
            await connection.run_sync(do_run_migrations)


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
