from tortoise.fields import UUIDField, CharField, ForeignKeyField, ReverseRelation
from tortoise.transactions import get_connection
from tortoise.models import MetaInfo
from tortoise.models import Model as StandartTortoiseBaseModel

from src.db.gh.utils.mixins import ScopeField, Model as TortoiseBaseModel

Model = StandartTortoiseBaseModel
# class Model(StandartTortoiseBaseModel):
#     pass
    # _meta = MetaInfo(None)
    # StandartTortoiseBaseModel._meta.default_connection = "default"

    # @classmethod
    # def _choose_db(cls, for_write: bool = False):
    #     return cls.is_transaction or get_connection("default")


class User(ScopeField, Model):
    id = UUIDField(pk=True)
    username = CharField(50, unique=True, null=False)
    name = CharField(100, null=True)
    surname = CharField(100, null=True)
    hashed_password = CharField(4096, null=False)
    email = CharField(101, unique=True)
    gh_user: ReverseRelation["GhUser"]

    def __str__(self):
        return self.id


User._meta.default_connection = "default"

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
