from enum import Enum

from piccolo.columns import Varchar, Array, UUID
from piccolo.table import Table
from piccolo.columns import Varchar, Array, UUID
from piccolo.table import Table
from piccolo.columns import Varchar, ForeignKey, ForeignKeyMeta
from piccolo.columns.reference import LazyTableReference
from piccolo.columns.base import Column, ForeignKeyMeta, OnDelete, OnUpdate

from src.piccolo_db.piccolo_conf import system_engine
from src.utils.enums import Scopes


class User(Table, tablename="base_user", db=system_engine):

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


