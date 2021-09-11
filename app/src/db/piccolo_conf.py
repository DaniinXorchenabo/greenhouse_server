import os
from os.path import dirname,  join, split
if os.environ.get("PG_SUPERUSER_NAME") is None:
    from dotenv import load_dotenv



    dotenv_path = join(split(split(split(dirname(__file__))[0])[0])[0], '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        print("В корне проекта обязательно должен быть файл .env!!!!")
        FileNotFoundError("\n.env file must be in project root\n")


# project_dir = split(split(dirname(__file__))[0])[0]
# os.chdir(project_dir)

from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry

print("-------------", os.environ.get("PG_SUPERUSER_NAME"), __name__)
DB = PostgresEngine(
    config={
        "database": os.environ.get("PGDATABASE"),
        "user": os.environ.get("PG_SUPERUSER_NAME"),
        "password": os.environ.get("PG_SUPERUSER_PASSWORD"),
        "host": os.environ.get("PGHOST"),
        "port": os.environ.get("PGPORT"),
    }
)

# DB = PostgresEngine(
#     config={
#         "database": "greenhouse_server_db" or os.environ.get("PGDATABASE"),
#         "user": "admin" or os.environ.get("PG_SUPERUSER_NAME"),
#         "password": "12345678" or os.environ.get("PG_SUPERUSER_PASSWORD"),
#         "host": "localhost" or os.environ.get("PGHOST"),
#         "port": "5432" or os.environ.get("PGPORT"),
#     }
# )


# import src.db.gh.piccolo_app
try:
    APP_REGISTRY = AppRegistry(
        apps=[
            "src.db.gh.piccolo_app",
            "piccolo_admin.piccolo_app"
        ]
    )

except ModuleNotFoundError as e:
    print("$$$$$$$$$$$$$$$$$", e, [e])
    piccolo_conf = os.environ.pop("PICCOLO_CONF", None)
    APP_REGISTRY = AppRegistry(
        apps=[
            "gh.piccolo_app",
            "piccolo_admin.piccolo_app"
        ]
    )
    # os.environ["PICCOLO_CONF"] = piccolo_conf

