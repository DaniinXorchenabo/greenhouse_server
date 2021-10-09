"""add access in other roles

Revision ID: 33f721b3f674
Revises: d4ba5d8346da
Create Date: 2021-10-09 21:14:27.702182

"""
import os

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '33f721b3f674'
down_revision = 'd4ba5d8346da'
branch_labels = None
depends_on = None


def upgrade():
    [(op.execute(f"GRANT CONNECT ON DATABASE {os.environ.get('PGDATABASE')} TO {os.environ.get(i)};"),
      op.execute(f"""GRANT USAGE ON SCHEMA public TO {os.environ.get(i)};"""))
     for i in ["PG_GUEST_NAME", "PG_USER_NAME", "PG_ADMIN_NAME",
               "PG_DEVELOPER_NAME", "PG_EDIT_DB_STRUCTURE_NAME", ]]


def downgrade():
    [op.execute(f"""REVOKE ALL ON DATABASE {os.environ.get('PGDATABASE')} FROM {os.environ.get(i)};""")
     for i in ["PG_GUEST_NAME", "PG_USER_NAME", "PG_ADMIN_NAME",
               "PG_DEVELOPER_NAME", "PG_EDIT_DB_STRUCTURE_NAME", ]]
