from enum import Enum
from typing import Union, Optional

from tortoise.fields import UUIDField, CharField, TextField
from tortoise.transactions import get_connection
from tortoise.backends.base.client import BaseDBAsyncClient
from tortoise.exceptions import ConfigurationError


from src.utils.enums import Scopes

from tortoise.models import Model as TortoiseBaseModel
import tortoise.models


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

    @property
    def db(self) -> BaseDBAsyncClient:
        try:
            return self.is_transaction or get_connection("default")
        except (ConfigurationError, KeyError):
            pass
        try:
            return tortoise.models.current_transaction_map[self.default_connection].get()
        except KeyError:
            raise ConfigurationError("No DB associated to model")


class ScopeField(TortoiseBaseModel):
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

