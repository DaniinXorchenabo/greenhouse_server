import os
from os.path import dirname, join, split

if os.environ.get("PG_SUPERUSER_NAME") is None:
    from dotenv import load_dotenv

    path = dirname(__file__)
    while "app" in (path := split(path)[0]):
        print(path)

    dotenv_path = join(path, '.env')
    print(dotenv_path, __file__)
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        print("В корне проекта обязательно должен быть файл .env!!!!")
        raise FileNotFoundError("\n.env file must be in project root\n")
os.environ.update(
    {key.split("#")[0].replace(" ", ""): val.split("#")[0].replace(" ", "") for key, val in os.environ.items()})
print("%%%%%-------------", os.environ.get("PG_SUPERUSER_NAME"), __name__)

from tortoise import Tortoise

print("**&&&&")

# from src.db.gh.tables.real import
# from
# from src.db.gh.migrations


async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        {
            'connections': {
                # Dict format for connection
                'default': {
                    'engine': 'tortoise.backends.asyncpg',
                    'credentials': {
                        "database": os.environ.get("PGDATABASE"),
                        "user": os.environ.get("PG_SUPERUSER_NAME"),
                        "password": os.environ.get("PG_SUPERUSER_PASSWORD"),
                        "host": os.environ.get("PGHOST"),
                        "port": os.environ.get("PGPORT"),
                    }
                },
            },
            'apps': {
                'gh': {
                    'models': ['__main__'],
                    # If no default_connection specified, defaults to 'default'
                    'default_connection': 'default',
                },
                "models": {
                    "models": ["src.db.gh.tables.real", "aerich.models"],
                    "default_connection": "default",
                },
            },
            # "apps":
            # },
            # 'routers': ['path.router1', 'path.router2'],
            'use_tz': False,
            'timezone': 'UTC'
        }
    )

    # Generate the schema
    await Tortoise.generate_schemas()
