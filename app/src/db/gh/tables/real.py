from enum import Enum
from typing import Union

from tortoise.models import Model
from tortoise.fields import UUIDField, CharField, TextField,\
    ForeignKeyField, ReverseRelation
# from tortoise.router import router
# from tortoise.transactions import get_connection
#
# from src.db.gh.tables.mixins import ScopeField
#
#
# class Scopes(str, Enum):
#     guest = 'g'
#     user = 'u'
#     admin = 'a'
#     dev = 'd'
#     system = 's'
#
#
# class ScopeField(Model):
#     _scopes = CharField(50, null=False, default='',
#                         description="Разрешения для пользователя, приписанные нотацией OAuth2")
#
#     @property
#     def scopes(self) -> set[Scopes]:
#         return set((Scopes(i) for i in self._scopes))
#
#     @scopes.setter
#     def scopes(self, new: set[Union[Scopes, str]]):
#         self._scopes = ''.join((Scopes(i) for i in new))
#
#     class Meta:
#         abstract = True
#
# # class BaseSuperuser(Model):
# #
# #     @classmethod
# #     def _choose_db(cls, for_write: bool = False):
# #         """
# #         Return the connection that will be used if this query is executed now.
# #
# #         :param for_write: Whether this query for write.
# #         :return: BaseDBAsyncClient:
# #         """
# #         return get_connection("default")
#
#
class User(Model):
    id = UUIDField(pk=True)
    username = CharField(50, unique=True, null=False)
    name = CharField(100, null=True)
    surname = CharField(100, null=True)
    hashed_password = CharField(4096, null=False)
    email = CharField(100, unique=True)
    gh_user: ReverseRelation["GhUser"]

    def __str__(self):
        return self.id


class Greenhouse(Model):
    id = UUIDField(pk=True)
    name = CharField(50, null=True)
    gh_user: ReverseRelation["GhUser"]

    def __str__(self):
        return self.id


class GhUser(Model):
    id = UUIDField(pk=True)
    gh_id = ForeignKeyField("real.Greenhouse", related_name='gh_user')
    user_id = ForeignKeyField("real.User", related_name='gh_user')

    def __str__(self):
        return self.gh_id


# # class User(Table, tablename="base_user", db=system_engine):
# #
# #     id = UUID(primary_key=True, required=True, unique=True)
# #     name = Varchar(required=True)
# #     surname = Varchar(required=True)
# #     username = Varchar(required=True, unique=True, help_text="Логин пользователя")
# #     hashed_password = Varchar(required=True, length=4096, help_text="хэш пароля")
# #     email = Varchar(unique=True)
# #     scopes = Array(base_column=Varchar(1, choices=Scopes, default=Scopes.guest),
# #                    required=True,
# #                    default=[],
# #                    help_text="Разрешения для пользователя, приписанные нотацией OAuth2")
#
# # __models__ = ["src.db.gh.tables.real.GhUser", "src.db.gh.tables.real.Greenhouse", "src.db.gh.tables.real.User"]