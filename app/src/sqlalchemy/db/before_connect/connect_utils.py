import os

from src.utils.files import check_environment_params_loaded

__all__ = ["base_connect_dict", "migration_engine_config"]

base_connect_dict: dict = {}

check_environment_params_loaded()

migration_engine_config = {
    "database": os.environ.get("PGDATABASE"),
    "username": os.environ.get("PG_MIGRATION_ROLE_NAME"),
    "password": os.environ.get("PG_MIGRATION_ROLE_PASSWORD"),
    "host": os.environ.get("PGHOST"),
    "port": os.environ.get("PGPORT"),
    "drivername": "postgresql+asyncpg"

}