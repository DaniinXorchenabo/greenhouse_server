import os

from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry


DB = PostgresEngine(
    config={
        "database": os.environ.get("PGDATABASE"),
        "user": os.environ.get("PG_SUPERUSER_NAME"),
        "password": os.environ.get("PG_SUPERUSER_PASSWORD"),
        "host": os.environ.get("PGHOST"),
        "port": os.environ.get("PGPORT"),
    }
)

APP_REGISTRY = AppRegistry(
    apps=["gh.piccolo_app", "piccolo_admin.piccolo_app"]
)
