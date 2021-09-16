import os

from piccolo.apps.migrations.auto import MigrationManager
from piccolo.table import Table

ID = "2021-09-16T18:39:54:770804"
VERSION = "0.45.1"
DESCRIPTION = "Обновление доступа для ролей"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="", description=DESCRIPTION
    )

    async def run():
        schema = 'public'
        table_names = 'base_user'

        guest_settings = f"GRANT SELECT ON TABLE {table_names} TO {os.environ.get('PG_GUEST_NAME')};"
        user_settings = f"GRANT SELECT, UPDATE  ON TABLE {table_names} TO {os.environ.get('PG_USER_NAME')};"
        admin_settings = f"GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE {table_names} TO {os.environ.get('PG_ADMIN_NAME')};"
        dev_settings = f"GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE {table_names} TO {os.environ.get('PG_DEVELOPER_NAME')};"

        admin_users = f"ALTER DEFAULT PRIVILEGES IN SCHEMA {schema} GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO {os.environ.get('PG_EDIT_DB_STRUCTURE_NAME')};"
        superuser = f"GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA {schema} TO {os.environ.get('PGUSER')}"

        [await Table.raw(i).run() for i in [
            guest_settings, user_settings, admin_settings,
            dev_settings, admin_users, superuser,
        ] if not print(i)]

    manager.add_raw(run)

    return manager
