from enum import Enum

from piccolo.columns import Varchar, UUID
from piccolo.table import Table

from src.db.piccolo_conf import admin_engine


class Scopes(str, Enum):
    guest = 'g'
    user = 'u'
    admin = 'a'
    dev = 'd'


class User(Table, tablename="base_user", db=admin_engine):

    id = UUID(primary_key=True, required=True, unique=True)
    name = Varchar(required=True)
    surname = Varchar(required=True)
    username = Varchar(required=True, unique=True, help_text="Логин пользователя")
    email = Varchar(unique=True)
