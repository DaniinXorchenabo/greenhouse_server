from enum import Enum

from piccolo.columns import Varchar, Array, UUID
from piccolo.table import Table
from piccolo.columns import Varchar, ForeignKey, ForeignKeyMeta
from piccolo.columns.reference import LazyTableReference
from piccolo.columns.base import Column, ForeignKeyMeta, OnDelete, OnUpdate


class Scopes(str, Enum):
    guest = 'g'
    user = 'u'
    admin = 'a'
    dev = 'd'
    system = 's'


class User(Table, tablename="base_user"):
    id = UUID(primary_key=True, required=True, unique=True)
    name = Varchar(required=True)
    surname = Varchar(required=True)
    username = Varchar(required=True, unique=True, help_text="Логин пользователя")
    hashed_password = Varchar(required=True, length=4096, help_text="хэш пароля")
    email = Varchar(unique=True)
    scopes = Array(base_column=Varchar(1, choices=Scopes, default=Scopes.guest),
                   required=True,
                   default=[],
                   help_text="Разрешения для пользователя, приписанные нотацией OAuth2")


class Greenhouse(Table, tablename="greenhouse"):
    id = UUID(primary_key=True, required=True, unique=True)


class UserGreenhouse(Table, tablename="user_greenhouse"):
    id = UUID(primary_key=True)
    user = ForeignKey(references="User", null=False)
    # user = ForeignKey(references=LazyTableReference(
    #     table_class_name="User", app_name="gh",
    # ), on_delete=OnDelete.cascade,
    #     on_update=OnUpdate.cascade,
    #     primary_key=False)
    # gh = ForeignKey(LazyTableReference(
    #     table_class_name="Greenhouse", app_name="gh",
    # ), on_delete=OnDelete.cascade, on_update=OnUpdate.cascade,
    #     primary_key=False)

User.objects()