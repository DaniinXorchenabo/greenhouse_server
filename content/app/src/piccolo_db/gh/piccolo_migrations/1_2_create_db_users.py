import os

from piccolo.apps.migrations.auto import MigrationManager
from piccolo.table import Table

ID = "2021-09-12T00:13:57:182359"
VERSION = "0.45.1"
DESCRIPTION = "Настройка ролей в postgres"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="", description=DESCRIPTION
    )

    async def run():
        schema = 'public'

        create_guest = f"""CREATE ROLE {os.environ.get('PG_GUEST_NAME')} WITH
                            LOGIN
                            NOSUPERUSER
                            NOCREATEDB
                            NOCREATEROLE
                            NOINHERIT
                            NOREPLICATION
                            CONNECTION LIMIT -1
                            PASSWORD '{os.environ.get('PG_GUEST_PASSWORD')}';
                            """
        create_user = f"""CREATE ROLE {os.environ.get('PG_USER_NAME')} WITH
                            LOGIN
                            NOSUPERUSER
                            NOCREATEDB
                            NOCREATEROLE
                            NOINHERIT
                            NOREPLICATION
                            CONNECTION LIMIT -1
                            PASSWORD '{os.environ.get('PG_USER_PASSWORD')}';
                            """
        create_admin = f"""CREATE ROLE {os.environ.get('PG_ADMIN_NAME')} WITH
                            LOGIN
                            NOSUPERUSER
                            NOCREATEDB
                            NOCREATEROLE
                            NOINHERIT
                            REPLICATION
                            CONNECTION LIMIT -1
                            PASSWORD '{os.environ.get('PG_ADMIN_PASSWORD')}';
                            """
        create_dev = f"""CREATE ROLE {os.environ.get('PG_DEVELOPER_NAME')} WITH
                            LOGIN
                            NOSUPERUSER
                            NOCREATEDB
                            NOCREATEROLE
                            NOINHERIT
                            REPLICATION
                            CONNECTION LIMIT -1
                            PASSWORD '{os.environ.get('PG_DEVELOPER_PASSWORD')}';
                            """
        create_gh_server = f"""CREATE ROLE {os.environ.get('PG_EDIT_DB_STRUCTURE_NAME')} WITH
                            LOGIN
                            NOSUPERUSER
                            CREATEDB
                            CREATEROLE
                            NOINHERIT
                            REPLICATION
                            CONNECTION LIMIT -1
                            PASSWORD '{os.environ.get('PG_EDIT_DB_STRUCTURE_PASSWORD')}';
                            """

        await Table.raw(create_guest).run()
        await Table.raw(create_user).run()
        await Table.raw(create_admin).run()
        await Table.raw(create_dev).run()
        await Table.raw(create_gh_server).run()

        # roles = ["PG_GUEST_NAME", "PG_USER_NAME", "PG_ADMIN_NAME", "PG_DEVELOPER_NAME",
        #     "PG_EDIT_DB_STRUCTURE_NAME", "PGUSER"
        # ]
        # connect_to_db = [f"GRANT CONNECT ON DATABASE {os.environ.get('PGDATABASE')} TO {os.environ.get(i)};"
        #                  for i in roles]
        #
        # access_to_schema = [f"GRANT USAGE ON SCHEMA {schema} TO {os.environ.get(i)};" for i in roles]
        #
        # [await Table.raw(i).run() for i in connect_to_db]
        # [await Table.raw(i).run() for i in access_to_schema]
        #
        # guest_settings = f"GRANT SELECT ON TABLE my_user TO {os.environ.get('PG_GUEST_NAME')};"
        # user_settings = f"GRANT SELECT, UPDATE  ON TABLE my_user TO {os.environ.get('PG_USER_NAME')};"
        # admin_settings = f"GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE my_user TO {os.environ.get('PG_ADMIN_NAME')};"
        # dev_settings = f"GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE my_user TO {os.environ.get('PG_DEVELOPER_NAME')};"
        #
        # create_tables = [f"GRANT USAGE, CREATE ON SCHEMA {schema} TO {os.environ.get(i)};" for i in ["PG_EDIT_DB_STRUCTURE_NAME", "PGUSER"]]
        # admin_users = f"ALTER DEFAULT PRIVILEGES IN SCHEMA {schema} GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO {os.environ.get('PG_EDIT_DB_STRUCTURE_NAME')};"
        # superuser = f"GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA {schema} TO {os.environ.get('PGUSER')}"
        #
        # # ALL TABLES
        # # guest_option = f"GRANT SELECT ON my_user IN SCHEMA {schema} TO {os.environ.get('PG_GUEST_NAME')};"
        # remark = f"REVOKE CREATE ON SCHEMA {schema} FROM PUBLIC;"
        # remark_db = f"REVOKE ALL ON DATABASE {os.environ.get('PGDATABASE')} FROM PUBLIC;"

    manager.add_raw(run)

    return manager
