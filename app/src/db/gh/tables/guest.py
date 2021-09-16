from enum import Enum

from piccolo.columns import Varchar
from piccolo.table import Table

from src.db.piccolo_conf import guest_engine


class Scopes(str, Enum):
    guest = 'g'
    user = 'u'
    admin = 'a'
    dev = 'd'


class User(Table, tablename="base_user", db=guest_engine):

    name = Varchar(required=True)
    surname = Varchar(required=True)
    username = Varchar(required=True, unique=True, help_text="Логин пользователя")