"""add access to User table for all roles

Revision ID: 92f95fabe941
Revises: 33f721b3f674
Create Date: 2021-10-09 21:44:45.992534

"""
import os

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '92f95fabe941'
down_revision = '33f721b3f674'
branch_labels = None
depends_on = None


def upgrade():
    table = "user_"
    op.execute(f"""GRANT SELECT ON TABLE {table} TO {os.environ.get('PG_GUEST_NAME')};""")
    op.execute(f"""GRANT SELECT, UPDATE ON TABLE {table} TO {os.environ.get('PG_USER_NAME')};""")
    op.execute(f"""GRANT SELECT, UPDATE ON TABLE {table} TO {os.environ.get('PG_ADMIN_NAME')};""")
    op.execute(f"""GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE {table} TO {os.environ.get('PG_DEVELOPER_NAME')};""")
    op.execute(f"""GRANT ALL ON TABLE {table} TO {os.environ.get('PG_EDIT_DB_STRUCTURE_NAME')};""")
    op.execute(f"""GRANT ALL  ON TABLE {table} TO {os.environ.get('PG_MIGRATION_ROLE_NAME')};""")
    op.execute(f"""GRANT ALL  ON TABLE {table} TO {os.environ.get('PG_SUPERUSER_NAME')};""")


def downgrade():
    table = "user_"
    op.execute(f"""REVOKE SELECT ON {table} FROM {os.environ.get('PG_GUEST_NAME')};""")
    op.execute(f"""REVOKE SELECT, UPDATE ON {table} FROM {os.environ.get('PG_USER_NAME')};""")
    op.execute(f"""REVOKE SELECT, UPDATE ON {table} FROM {os.environ.get('PG_ADMIN_NAME')};""")
    op.execute(f"""REVOKE SELECT, INSERT, UPDATE, DELETE ON {table} FROM {os.environ.get('PG_DEVELOPER_NAME')};""")
    op.execute(f"""REVOKE ALL ON {table} FROM {os.environ.get('PG_EDIT_DB_STRUCTURE_NAME')};""")
    # op.execute(f"""REVOKE SELECT ON {table} FROM {os.environ.get('PG_MIGRATION_ROLE_NAME')};""")
    # op.execute(f"""REVOKE SELECT ON {table} FROM {os.environ.get('PG_SUPERUSER_NAME')};""")
