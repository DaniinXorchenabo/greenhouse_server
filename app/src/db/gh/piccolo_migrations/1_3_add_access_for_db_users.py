import os

from piccolo.apps.migrations.auto import MigrationManager
from piccolo.table import Table

ID = "2021-09-15T18:53:10:746304"
VERSION = "0.45.1"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="", description=DESCRIPTION
    )

    async def run():
        schema = 'public'
        roles = ["PG_GUEST_NAME", "PG_USER_NAME", "PG_ADMIN_NAME", "PG_DEVELOPER_NAME",
                 "PG_EDIT_DB_STRUCTURE_NAME", "PGUSER"
                 ]
        connect_to_db = [f"GRANT CONNECT ON DATABASE {os.environ.get('PGDATABASE')} TO {os.environ.get(i)};"
                         for i in roles]

        access_to_schema = [f"GRANT USAGE ON SCHEMA {schema} TO {os.environ.get(i)};" for i in roles]

        [await Table.raw(i).run() for i in connect_to_db]
        [await Table.raw(i).run() for i in access_to_schema]

        guest_settings = f"GRANT SELECT ON TABLE my_user TO {os.environ.get('PG_GUEST_NAME')};"
        user_settings = f"GRANT SELECT, UPDATE  ON TABLE my_user TO {os.environ.get('PG_USER_NAME')};"
        admin_settings = f"GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE my_user TO {os.environ.get('PG_ADMIN_NAME')};"
        dev_settings = f"GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE my_user TO {os.environ.get('PG_DEVELOPER_NAME')};"

        create_tables = [f"GRANT USAGE, CREATE ON SCHEMA {schema} TO {os.environ.get(i)};" for i in
                         ["PG_EDIT_DB_STRUCTURE_NAME", "PGUSER"]]
        admin_users = f"ALTER DEFAULT PRIVILEGES IN SCHEMA {schema} GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO {os.environ.get('PG_EDIT_DB_STRUCTURE_NAME')};"
        superuser = f"GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA {schema} TO {os.environ.get('PGUSER')}"

        # ALL TABLES
        # guest_option = f"GRANT SELECT ON my_user IN SCHEMA {schema} TO {os.environ.get('PG_GUEST_NAME')};"
        remark = f"REVOKE CREATE ON SCHEMA {schema} FROM PUBLIC;"
        remark_db = f"REVOKE ALL ON DATABASE {os.environ.get('PGDATABASE')} FROM PUBLIC;"

        [await Table.raw(i).run() for i in [
            guest_settings, user_settings, admin_settings,
            dev_settings,
            *create_tables, admin_users, superuser,
            remark, remark_db
        ] if not print(i)]


    manager.add_raw(run)

    return manager
