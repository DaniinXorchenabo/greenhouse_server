"""delete default access for public role

Revision ID: d4ba5d8346da
Revises: 7fa5740b540f
Create Date: 2021-10-09 20:23:50.026905

"""
import os

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4ba5d8346da'
down_revision = '7fa5740b540f'
branch_labels = None
depends_on = None


def upgrade():
    # =======! Пользователь для миграций !=======
    op.execute(f"""GRANT CONNECT ON DATABASE {os.environ.get('PGDATABASE')}
                    TO {os.environ.get('PG_MIGRATION_ROLE_NAME')};""")
    op.execute(f"""GRANT USAGE, CREATE ON SCHEMA public TO {os.environ.get('PG_MIGRATION_ROLE_NAME')};""")
    op.execute(f"""ALTER DEFAULT PRIVILEGES IN SCHEMA public
                    GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO {os.environ.get('PG_MIGRATION_ROLE_NAME')};""")

    # =======! Суперпользователь, инициализированный при создании БД !=======
    [op.execute(f"""ALTER USER {os.environ.get('PG_SUPERUSER_NAME')} WITH {i}""")
     for i in ["SUPERUSER", "LOGIN", "CREATEDB", "CREATEROLE", "INHERIT", "REPLICATION"]]
    op.execute(f"""GRANT CONNECT ON DATABASE {os.environ.get('PGDATABASE')}
                    TO {os.environ.get('PG_SUPERUSER_NAME')};""")
    op.execute(f"""GRANT USAGE, CREATE ON SCHEMA public TO {os.environ.get('PG_SUPERUSER_NAME')};""")
    op.execute(f"""ALTER DEFAULT PRIVILEGES IN SCHEMA public
                    GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO {os.environ.get('PG_SUPERUSER_NAME')};""")

    # =======! удаление прав для PUBLIC роли !=======
    op.execute("""REVOKE CREATE ON SCHEMA public FROM PUBLIC;""")
    op.execute(f"""REVOKE ALL ON DATABASE {os.environ.get('PGDATABASE')} FROM PUBLIC;""")


def downgrade():
    # =======! Возвращение прав PUBLIC роли !=======
    op.execute("""GRANT USAGE, CREATE ON SCHEMA public TO PUBLIC;""")
    op.execute(f"""GRANT CONNECT ON DATABASE {os.environ.get('PGDATABASE')} TO PUBLIC;""")

    # =======! Удаление привилегий для роли миграций !=======
    op.execute("""REVOKE USAGE, CREATE ON SCHEMA public FROM PUBLIC;""")