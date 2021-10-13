from collections import namedtuple
from typing import NamedTuple, Type

from src.sqlalchemy.db.tables import _real as _real_module
from src.sqlalchemy.db.tables._real import User as _real_User


__all__ = ['_tables_type', '_real']

_tables_type = namedtuple("_tables", ["User"])


class _Real(NamedTuple):
    User: Type[_real_User] = _real_User


_real = _Real()




