from enum import Enum
from typing import Union

from tortoise.models import Model
from tortoise.fields import UUIDField, CharField, TextField

from src.utils.enums import Scopes


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