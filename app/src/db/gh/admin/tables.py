from tortoise.fields import UUIDField, CharField, ForeignKeyField, ReverseRelation
from tortoise.transactions import get_connection
from src.db.gh.utils.mixins import ScopeField, Model as TortoiseBaseModel


class Model(TortoiseBaseModel):

    @classmethod
    def _choose_db(cls, for_write: bool = False):
        """
        Return the connection that will be used if this query is executed now.

        :param for_write: Whether this query for write.
        :return: BaseDBAsyncClient:
        """
        return cls.is_transaction or get_connection("default")


class User(Model, ScopeField):
    id = UUIDField(pk=True)
    username = CharField(50, unique=True, null=False)
    name = CharField(100, null=True)
    surname = CharField(100, null=True)
    hashed_password = CharField(4096, null=False)
    email = CharField(101, unique=True)
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
    gh_id = ForeignKeyField("gh_real.Greenhouse", related_name='gh_user')
    user_id = ForeignKeyField("gh_real.User", related_name='gh_user')

    def __str__(self):
        return self.id
