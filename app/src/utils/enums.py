from enum import Enum

__all__ = ["Scopes"]


class Scopes(str, Enum):
    guest = 'g'
    user = 'u'
    admin = 'a'
    dev = 'd'
    system = 's'