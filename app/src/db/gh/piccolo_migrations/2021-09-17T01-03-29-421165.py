from piccolo.apps.migrations.auto import MigrationManager


ID = "2021-09-17T01:03:29:421165"
VERSION = "0.49.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="gh", description=DESCRIPTION
    )

    manager.rename_column(
        table_class_name="User",
        tablename="base_user",
        old_column_name="pass_hash",
        new_column_name="hashed_password",
    )

    return manager
