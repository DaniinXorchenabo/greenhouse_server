import os
from os.path import dirname,  join, split
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


# project_dir = split(split(dirname(__file__))[0])[0]
# os.chdir(project_dir)

from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry

print("%%%%%-------------", os.environ.get("PG_SUPERUSER_NAME"), __name__)
DB = PostgresEngine(
    config={
        "database": os.environ.get("PGDATABASE"),
        "user": os.environ.get("PG_SUPERUSER_NAME"),
        "password": os.environ.get("PG_SUPERUSER_PASSWORD"),
        "host": os.environ.get("PGHOST"),
        "port": os.environ.get("PGPORT"),
    }
)
print("***%%%%%-------------", os.environ.get("PG_SUPERUSER_NAME"), __name__)
try:

    readonly_DB = PostgresEngine(
        config={
            "database": os.environ.get("PGDATABASE"),
            "user": os.environ.get("PG_GUEST_NAME"),
            "password": os.environ.get("PG_GUEST_PASSWORD"),
            "host": os.environ.get("PGHOST"),
            "port": os.environ.get("PGPORT"),
        }
    )
except Exception:
    pass



# import src.db.gh.piccolo_app
# piccolo_conf = os.environ.pop("PICCOLO_CONF", None)
# APP_REGISTRY = AppRegistry(
#     apps=[
#         "gh.piccolo_app",
#         "piccolo_admin.piccolo_app"
#     ]
# )
try:
    print("!!!!!!!!!!!_-_---------------------------")
    APP_REGISTRY = AppRegistry(
        apps=[
            "src.db.gh.piccolo_app",
            "piccolo_admin.piccolo_app"
        ]
    )

except Exception as e:
    print(e)
    piccolo_conf = os.environ.pop("PICCOLO_CONF", None)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    APP_REGISTRY = AppRegistry(
        apps=[
            "gh.piccolo_app",
            "piccolo_admin.piccolo_app"
        ]
    )
    # os.environ["PICCOLO_CONF"] = piccolo_conf

