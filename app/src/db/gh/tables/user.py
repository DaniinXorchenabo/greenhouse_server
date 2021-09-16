from enum import Enum

from piccolo.table import Table
from piccolo.columns import Varchar, Boolean, Array, UUID

from src.db.piccolo_conf import user_engine


class Scopes(str, Enum):
    guest = 'g'
    user = 'u'
    admin = 'a'
    dev = 'd'


class User(Table, tablename="base_user", db=user_engine):

    id = UUID(primary_key=True, required=True, unique=True)
    name = Varchar(required=True)
    surname = Varchar(required=True)
    username = Varchar(required=True, unique=True, help_text="Логин пользователя")
    email = Varchar(unique=True)



