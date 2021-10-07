import os

import asyncpg
import asyncio
import ssl


from os.path import dirname,  join, split


from src.utils.files import check_environment_params_loaded

check_environment_params_loaded()


async def main():
    user = os.environ.get("PG_SUPERUSER_NAME")
    pas = os.environ.get("PG_SUPERUSER_PASSWORD")
    host = os.environ.get("PGHOST")
    port = os.environ.get("PGPORT")
    db = os.environ.get("PGDATABASE")
    # host = "host.docker.internal"
    con = await asyncpg.connect(dsn=f"postgres://{user}:{pas}@{host}:{port}/{db}")
    # con = await asyncpg.connect(dsn=f"postgres://{user}:{pas}@{host}:{port}/{db}")
    # **{
    #     "database": os.environ.get("PGDATABASE"),
    #     "user": os.environ.get("PG_SUPERUSER_NAME"),
    #     "password": os.environ.get("PG_SUPERUSER_PASSWORD"),
    #     "host": os.environ.get("PGHOST"),
    #     "port": os.environ.get("PGPORT"),
    # })
    await con.close()
    print("--------------------success")


asyncio.run(main())