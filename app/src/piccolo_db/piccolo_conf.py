import os
from os.path import dirname,  join, split

from src.utils.files import check_environment_params_loaded

check_environment_params_loaded()

from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry


os.environ.update({key.split("#")[0].replace(" ", ""): val.split("#")[0].replace(" ", "") for key, val in os.environ.items()})
print("%%%%%-------------", os.environ.get("PG_SUPERUSER_NAME"), __name__)
# try:
#     DB = PostgresEngine(
#         config={
#             "database": os.environ.get("PGDATABASE"),
#             "user": os.environ.get("PG_SUPERUSER_NAME"),
#             "password": os.environ.get("PG_SUPERUSER_PASSWORD"),
#             "host": os.environ.get("PGHOST"),
#             "port": os.environ.get("PGPORT"),
#         }
#     )
# except Exception:
#     DB = PostgresEngine(os.environ.get("DATABASE_URL", ""))
print("***%%%%%-------------", os.environ.get("PG_SUPERUSER_NAME"), __name__)
try:
    pass
    # guest_engine = PostgresEngine(
    #     config={
    #         "database": os.environ.get("PGDATABASE"),
    #         "user": os.environ.get("PG_GUEST_NAME"),
    #         "password": os.environ.get("PG_GUEST_PASSWORD"),
    #         "host": os.environ.get("PGHOST"),
    #         "port": os.environ.get("PGPORT"),
    #     }
    # )
    # user_engine = PostgresEngine(
    #     config={
    #         "database": os.environ.get("PGDATABASE"),
    #         "user": os.environ.get("PG_USER_NAME"),
    #         "password": os.environ.get("PG_USER_PASSWORD"),
    #         "host": os.environ.get("PGHOST"),
    #         "port": os.environ.get("PGPORT"),
    #     }
    # )
    # admin_engine = PostgresEngine(
    #     config={
    #         "database": os.environ.get("PGDATABASE"),
    #         "user": os.environ.get("PG_ADMIN_NAME"),
    #         "password": os.environ.get("PG_ADMIN_PASSWORD"),
    #         "host": os.environ.get("PGHOST"),
    #         "port": os.environ.get("PGPORT"),
    #     }
    # )
    # developer_engine = PostgresEngine(
    #     config={
    #         "database": os.environ.get("PGDATABASE"),
    #         "user": os.environ.get("PG_DEVELOPER_NAME"),
    #         "password": os.environ.get("PG_DEVELOPER_PASSWORD"),
    #         "host": os.environ.get("PGHOST"),
    #         "port": os.environ.get("PGPORT"),
    #     }
    # )
    # system_engine = PostgresEngine(
    #     config={
    #         "database": os.environ.get("PGDATABASE"),
    #         "user": os.environ.get("PG_EDIT_DB_STRUCTURE_NAME"),
    #         "password": os.environ.get("PG_EDIT_DB_STRUCTURE_PASSWORD"),
    #         "host": os.environ.get("PGHOST"),
    #         "port": os.environ.get("PGPORT"),
    #     }
    # )
except Exception:
    guest_engine = user_engine = admin_engine = developer_engine = system_engine = DB

try:
    print("!!!!!!!!!!!_-_---------------------------")
    APP_REGISTRY = AppRegistry(
        apps=[
            "src.piccolo_db.gh.piccolo_app",
            "piccolo_admin.piccolo_app"
        ]
    )

except Exception as e:
    print("try import as gh.piccolo_app", [e])
    piccolo_conf = os.environ.pop("PICCOLO_CONF", None)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    APP_REGISTRY = AppRegistry(
        apps=[
            "gh.piccolo_app",
            "piccolo_admin.piccolo_app"
        ]
    )
    # os.environ["PICCOLO_CONF"] = piccolo_conf

