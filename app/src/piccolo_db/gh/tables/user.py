from enum import Enum

from piccolo.columns import Varchar, UUID
from piccolo.table import Table
from piccolo.columns import Varchar, Array, UUID
from piccolo.table import Table
from piccolo.columns import Varchar, ForeignKey, ForeignKeyMeta
from piccolo.columns.reference import LazyTableReference
from piccolo.columns.base import Column, ForeignKeyMeta, OnDelete, OnUpdate

from src.piccolo_db.piccolo_conf import user_engine
from src.utils.enums import Scopes


class User(Table, tablename="base_user", db=user_engine):

    id = UUID(primary_key=True, required=True, unique=True)
    name = Varchar(required=True)
    surname = Varchar(required=True)
    username = Varchar(required=True, unique=True, help_text="Логин пользователя")
    email = Varchar(unique=True)



class Greenhouse(Table, tablename="greenhouse"):
    id = UUID(primary_key=True, required=True, unique=True)


class UserGreenhouse(Table, tablename="user_greenhouse"):
    id = UUID(primary_key=True)
    # user = ForeignKey(references=LazyTableReference(
    #     table_class_name="User", app_name="gh",
    #     module_path="src.piccolo_db.gh.tables.superuser",
    # ), on_delete=OnDelete.cascade,
    #     on_update=OnUpdate.cascade,
    #     primary_key=False)
    # gh = ForeignKey(LazyTableReference(
    #     table_class_name="Greenhouse", app_name="gh",
    #     module_path="src.piccolo_db.gh.tables.superuser",
    # ), on_delete=OnDelete.cascade, on_update=OnUpdate.cascade,
    #     primary_key=False)

