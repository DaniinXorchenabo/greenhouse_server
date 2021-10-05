from piccolo.apps.migrations.auto import MigrationManager
from piccolo.columns.column_types import ForeignKey


ID = "2021-10-06T00:15:16:400105"
VERSION = "0.49.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="gh", description=DESCRIPTION
    )

    manager.alter_column(
        table_class_name="UserGreenhouse",
        tablename="user_greenhouse",
        column_name="user_id",
        params={"null": False},
        old_params={"null": True},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
    )

    manager.alter_column(
        table_class_name="UserGreenhouse",
        tablename="user_greenhouse",
        column_name="gh_id",
        params={"null": False},
        old_params={"null": True},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
    )

    return manager
