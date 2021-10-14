"""create roles in DB

Revision ID: 7fa5740b540f
Revises: ed2f911d6c5b
Create Date: 2021-10-08 23:40:43.241882

"""
import os

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7fa5740b540f'
down_revision = 'ed2f911d6c5b'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(f"""CREATE ROLE {os.environ.get('PG_GUEST_NAME')} WITH
                            LOGIN
                            NOSUPERUSER
                            NOCREATEDB
                            NOCREATEROLE
                            NOINHERIT
                            NOREPLICATION
                            CONNECTION LIMIT -1
                            PASSWORD '{os.environ.get('PG_GUEST_PASSWORD')}';
                            """)
    op.execute(f"""CREATE ROLE {os.environ.get('PG_USER_NAME')} WITH
                                LOGIN
                                NOSUPERUSER
                                NOCREATEDB
                                NOCREATEROLE
                                NOINHERIT
                                NOREPLICATION
                                CONNECTION LIMIT -1
                                PASSWORD '{os.environ.get('PG_USER_PASSWORD')}';
                                """)
    op.execute(f"""CREATE ROLE {os.environ.get('PG_ADMIN_NAME')} WITH
                                LOGIN
                                NOSUPERUSER
                                NOCREATEDB
                                NOCREATEROLE
                                NOINHERIT
                                REPLICATION
                                CONNECTION LIMIT -1
                                PASSWORD '{os.environ.get('PG_ADMIN_PASSWORD')}';
                                """)

    op.execute(f"""CREATE ROLE {os.environ.get('PG_DEVELOPER_NAME')} WITH
                            LOGIN
                            NOSUPERUSER
                            NOCREATEDB
                            NOCREATEROLE
                            NOINHERIT
                            REPLICATION
                            CONNECTION LIMIT -1
                            PASSWORD '{os.environ.get('PG_DEVELOPER_PASSWORD')}';
                            """)
    op.execute(f"""CREATE ROLE {os.environ.get('PG_EDIT_DB_STRUCTURE_NAME')} WITH
                            LOGIN
                            NOSUPERUSER
                            NOCREATEDB
                            NOCREATEROLE
                            NOINHERIT
                            REPLICATION
                            CONNECTION LIMIT -1
                            PASSWORD '{os.environ.get('PG_EDIT_DB_STRUCTURE_PASSWORD')}';
                            """)
    op.execute(f"""CREATE ROLE {os.environ.get('PG_MIGRATION_ROLE_NAME')} WITH
                            LOGIN
                            NOSUPERUSER
                            CREATEDB
                            CREATEROLE
                            NOINHERIT
                            REPLICATION
                            CONNECTION LIMIT -1
                            PASSWORD '{os.environ.get('PG_MIGRATION_ROLE_PASSWORD')}';
                            """)


def downgrade():
    [op.execute(f"""DROP ROLE IF EXISTS {os.environ.get(i)}""") for i in [
        "PG_GUEST_NAME", "PG_USER_NAME", "PG_ADMIN_NAME",
        "PG_DEVELOPER_NAME", "PG_EDIT_DB_STRUCTURE_NAME",
        "PG_MIGRATION_ROLE_NAME"]]
