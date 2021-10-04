from enum import Enum
from typing import Union, Optional

from tortoise.fields import UUIDField, CharField, TextField
from tortoise.transactions import get_connection
from tortoise.backends.base.client import BaseDBAsyncClient

from src.utils.enums import Scopes

from tortoise.models import Model as TortoiseBaseModel


class Model(TortoiseBaseModel):
    is_transaction: Optional[BaseDBAsyncClient] = None

    @classmethod
    def _choose_db(cls, for_write: bool = False):
        """
        Return the connection that will be used if this query is executed now.

        :param for_write: Whether this query for write.
        :return: BaseDBAsyncClient:
        """
        return cls.is_transaction or get_connection("default")


class ScopeField(Model):
    _scopes = CharField(50, null=False, default='',
                        description="Разрешения для пользователя, приписанные нотацией OAuth2")

    @property
    def scopes(self) -> set[Scopes]:
        return set((Scopes(i) for i in self._scopes))

    @scopes.setter
    def scopes(self, new: set[Union[Scopes, str]]):
        self._scopes = ''.join((Scopes(i) for i in new))

    class Meta:
        abstract = True

