from piccolo.apps.migrations.auto import MigrationManager
from piccolo.columns.column_types import Varchar
from piccolo.columns.indexes import IndexMethod


ID = "2021-09-11T20:55:14:024000"
VERSION = "0.45.1"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="gh", description=DESCRIPTION
    )

    manager.add_table("MyUser", tablename="my_user")

    manager.add_column(
        table_class_name="MyUser",
        tablename="my_user",
        column_name="name",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
        },
    )

    return manager
